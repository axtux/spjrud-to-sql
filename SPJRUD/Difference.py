from Relation import Relation
from functions import *


class Difference(Relation):
  def __init__(self, subrelation1, subrelation2) :
    # check and save subrelations
    self.subrelation1 = check_relation(self, subrelation1, 'subrelation1')
    self.subrelation2 = check_relation(self, subrelation2, 'subrelation2')
    
    # check that attributes are exactly the same
    self.setAttributes(check_matching_attributes(self, subrelation1.getAttributes(), subrelation2.getAttributes()))
  
  def toSQL(self):
    # query, keep 2 select because SQLite do not want () out of FROM
    return 'SELECT * FROM ('+self.subrelation1.toSQL()+') EXCEPT SELECT * FROM ('+self.subrelation2.toSQL()+')'

