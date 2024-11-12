# Import models
from analysis.models import *

# Special offer related_______________________________________________________
def CreateSpecialOfferDimETL(object):
    # Create new object
    specialOfferDim = SpecialOfferDim(id=object.id,
                                      Description=object.Description,
                                      DiscountPct=object.DiscountPct)
    
    # Save object
    specialOfferDim.save()
    


def EditSpecialOfferDimETL(object):
    # Get the existed object
    specialOfferDim = SpecialOfferDim.objects.get(id=object.id)
    
    # Edit the object
    specialOfferDim.Description = object.Description
    specialOfferDim.DiscountPct = object.DiscountPct
    
    # Save new info on the object
    specialOfferDim.save()


    
def DeleteSpecialOfferDimETL(object):
    # Get the existed object
    specialOfferDim = SpecialOfferDim.objects.get(id=object.id)
    
    # Delete the database record
    specialOfferDim.delete()
    
    

# Product related_____________________________________________________________
def CreateProductDimETL(object):
    # Create new object
    productDim = ProductDim(id=object.id,
                            Name=object.Name,
                            ListPrice=object.ListPrice,
                            StandardCost=object.StandardCost)
    
    # Save object
    productDim.save()



def EditProductDimETL(object):
    # Get the existed object
    productDim = ProductDim.objects.get(id=object.id)
    
    # Edit the object
    productDim.Name             = object.Name
    productDim.StandardCost     = object.StandardCost
    productDim.ListPrice        = object.ListPrice
    
    # Save new info on the object
    productDim.save()
    


def DeleteProductDimETL(object):
    # Get the existed object
    productDim = ProductDim.objects.get(id=object.id)
    
    # Delete the database record
    productDim.delete()
    
    
    
# Employee related____________________________________________________________
def CreateEmployeeDimETL(object):
    # Create new object
    employeeDim = EmployeeDim(id=object.id,
                              Name=object.name)
    
    # Save object
    employeeDim.save()
    


def EditEmployeeDimETL(object):
    # Get the existed object
    employeeDim = EmployeeDim.objects.get(id=object.id)
    
    # Edit the object
    employeeDim.Name = object.name
    
    # Save new info on the object
    employeeDim.save()



# Customer related____________________________________________________________
def CreateCustomerDimETL(object):
    # Get territory
    territoryID     = object.Territory.id
    territoryDim    = TerritoryDim.objects.get(id=territoryID) 
    
    # Get individual name
    individualName = None
    if object.CustomerIndividual:
        individualName = object.CustomerIndividual.FirstName + " " + object.CustomerIndividual.MiddleName + " " + object.CustomerIndividual.LastName
        
    # Get store name
    storeName = None
    if object.CustomerStore:
        storeName = object.CustomerStore.Name
    
    # Create new object
    customerDim = CustomerDim(id=object.id,
                              IndividualName=individualName,
                              StoreName=storeName,
                              Territory=territoryDim)
    
    # Save object
    customerDim.save()
    
    
    
def EditCustomerDimETL(object):
    # Get territory
    territoryID     = object.Territory.id
    territoryDim    = TerritoryDim.objects.get(id=territoryID) 
    
    # Get individual name
    individualName = None
    if object.CustomerIndividual:
        individualName = object.CustomerIndividual.FirstName + " " + object.CustomerIndividual.MiddleName + " " + object.CustomerIndividual.LastName
        
    # Get store name
    storeName = None
    if object.CustomerStore:
        storeName = object.CustomerStore.Name
        
    # Get the object
    customerDim = CustomerDim.objects.get(id=object.id)
    customerDim.IndividualName = individualName
    customerDim.StoreName      = storeName
    customerDim.Territory      = territoryDim
    
    # Save the object
    customerDim.save()
    
    
    
def DeleteCustomerDimETL(object):
    # Get the existed object
    customerDim = CustomerDim.objects.get(id=object.id)
    
    # Delete the database record
    customerDim.delete()
    
    
    
# Sales order related_________________________________________________________
def CreateSalesOrderHeaderFactETL(object):
    # Get employee
    employeeID = object.Employee.id
    employee   = EmployeeDim.objects.get(id=employeeID)
    
    # Get customer
    customerID = object.Customer.id
    customer   = CustomerDim.objects.get(id=customerID)
    
    # Create new object
    salesOrderHeaderFact = SalesOrderHeaderFact(id=object.id,
                                                OrderDate=object.OrderDate,
                                                SubTotal=object.SubTotal,
                                                TaxAmt=object.TaxAmt,
                                                Freight=object.Freight,
                                                TotalDue=object.TotalDue,
                                                Employee=employee,
                                                Customer=customer)
    
    # Save object
    salesOrderHeaderFact.save()
    
    
    
def EditSalesOrderHeaderFactETL(object):
    pass
