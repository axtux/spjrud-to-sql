from Relation import Relation
from functions import *


class Union(Relation) :
  def __init__(self, subrelation1, subrelation2) :
    # check arguments are objects of type Relation
    check_relation(subrelation1, 1)
    check_relation(subrelation2, 2)
    self.subrelation1 = subrelation1
    self.subrelation2 = subrelation2
    
    # check that attributes are exactly the same
    attributes1 = subrelation1.getAttributes()
    attributes2 = subrelation2.getAttributes()
    check_attributes_match(attributes1, attributes2)
    
    
    self.setAttributes(attributes1)
  
  def toSQL(self) :
    # query
    return 'SELECT * FROM ('+self.subrelation1.toSQL()+' UNION '+self.subrelation2.toSQL()+')'
