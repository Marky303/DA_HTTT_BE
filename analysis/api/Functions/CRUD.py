# Import models
from analysis.models import *

def CreateSpecialOfferDimETL(object):
    # Create new object
    specialOfferDim = SpecialOfferDim(id=object.id,
                                      Name=object.Name,
                                      DiscountPct=object.DiscountPct)
    
    # Save object
    specialOfferDim.save()