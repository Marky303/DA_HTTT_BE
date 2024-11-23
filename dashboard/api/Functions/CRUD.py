import json
from datetime import datetime, timedelta
import random
import string
from decimal import Decimal
import math
from django.db.models import Sum, F
from calendar import monthrange
from pytz import UTC  


# Import models
from sales.models import *
from analysis.models import *

# CRUD functions
def getOverviewThisMonthCRUD():
    # Get last month's date
    thirty_days_ago = datetime.now() - timedelta(days=30)
    
    # Calculate rev
    recent_orders = SalesOrderHeaderFact.objects.filter(OrderDate__gte=thirty_days_ago)
    revenue = recent_orders.aggregate(total=Sum('SubTotal'))['total']
    
    # Calculate cost
    cost = float(0)
    for order in recent_orders:        
        # Get the salesorderdetail
        salesOrderDetailLst = SalesOrderDetailFact.objects.filter(SalesOrder=order)
        
        for item in salesOrderDetailLst:
            # Get quantity
            quantity = item.OrderQty
            
            # Get cost
            singleCost = item.Product.StandardCost
            
            # Add to cost
            cost = cost + float(quantity) * float(singleCost)

    # Calculate profit
    profit = (float(revenue) if revenue else float(0)) - cost
    
    # Create result template
    result = {
        "revenue": round(float(revenue) if revenue else float(0), 1),
        "profit": round(profit, 1),
        "cost": round(cost, 1)
    }
    
    # Return the thingy
    return result



def getOverviewLastMonthsCRUD():
    # Get current UTC date
    now = datetime.now(UTC)
    
    # Create the result list
    results = []
    
    for i in range(0, 6):  
        current_month = (now.month - i - 1) % 12 + 1
        current_year = now.year + (now.month - i - 1) // 12
        
        month_start = datetime(current_year, current_month, 1, 0, 0, 0, tzinfo=UTC)
        last_day = monthrange(current_year, current_month)[1]
        month_end = datetime(current_year, current_month, last_day, 23, 59, 59, tzinfo=UTC)
        
        monthly_orders = SalesOrderHeaderFact.objects.filter(OrderDate__range=[month_start, month_end])
        
        # TEST ONLY
        # print(str(monthly_orders.query))
        
        revenue = monthly_orders.aggregate(total=Sum('SubTotal'))['total']
        
        # Calculate cost
        cost = float(0)
        for order in monthly_orders:
            # Get the sales order details
            salesOrderDetailLst = SalesOrderDetailFact.objects.filter(SalesOrder=order)
            
            for item in salesOrderDetailLst:
                # Get quantity and cost
                quantity = item.OrderQty
                singleCost = item.Product.StandardCost
                
                # Add to cost
                cost += float(quantity) * float(singleCost)
        
        # # Calculate profit
        # profit = (float(revenue) if revenue else float(0)) - cost
        
        # Add the result for the month
        results.append({
            "time": month_start.strftime("%B %Y"),  # e.g., "November 2024"
            "revenue": round(float(revenue) if revenue else float(0), 1),
            # "profit": round(profit, 1),
            "cost": round(cost, 1)
        })
    
    # Reverse the list to make it in order
    results.reverse()
    
    return results



def getTopProductsCRUD():
    # Get the 30 days ago date
    thirty_days_ago = datetime.now() - timedelta(days=30)
    
    # Filter SalesOrderDetailFact by orders placed in the last 30 days
    top_products = (
        SalesOrderDetailFact.objects
        .filter(SalesOrder__OrderDate__gte=thirty_days_ago)  
        .values('Product__id', 'Product__Name')  
        .annotate(total_revenue=Sum('LineTotal'))  
        .order_by('-total_revenue')[:3]  
    )
    
    # Result template
    result = [
        {
            "id": product['Product__id'],
            "name": product['Product__Name'],
            "revenue": float(product['total_revenue'])
        }
        for product in top_products
    ]
    
    return result



def getTopTerritoryCRUD():
    thirty_days_ago = datetime.now() - timedelta(days=30)
    
    sales_orders = SalesOrderHeaderFact.objects.filter(OrderDate__gte=thirty_days_ago)
    
    territories_data = (
        sales_orders
        .values('Customer__Territory__id', 'Customer__Territory__Name')  # Group by Territory ID and Name
        .annotate(
            total_revenue=Sum('SubTotal'),  # Calculate revenue
            total_cost=Sum(
                F('salesorderdetailfact__OrderQty') * F('salesorderdetailfact__Product__StandardCost')  # Calculate cost
            ),
        )
    )
    
    # # Calculate profit for each territory
    # for territory in territories_data:
    #     territory['profit'] = float(territory['total_revenue']) - float(territory['total_cost'] or 0)
    
    # Sort by revenue and get 3 highest
    top_territories = sorted(territories_data, key=lambda x: x['total_revenue'], reverse=True)[:3]
    
    # Create result template
    result = [
        {
            "territory_id": territory['Customer__Territory__id'],
            "territory_name": territory['Customer__Territory__Name'],
            "revenue": round(float(territory['total_revenue']), 2),
            "cost": round(float(territory['total_cost'] or 0), 2),
            # "profit": round(float(territory['profit']), 2),
        }
        for territory in top_territories
    ]
    
    return result