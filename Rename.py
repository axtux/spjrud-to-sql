from Relation import Relation, Attribute
from copy import deepcopy


class Rename(Relation) :
  def __init__(self, old_attr_name, new_attr_name, subrelation) :
    if not isinstance(subrelation, Relation) :
      raise TypeError('subrelation argument must be of type Relation"')
    self.subrelation = subrelation
    
    # copy attributes and rename one
    self.setAttributes(deepcopy(subrelation.getAttributes()))
    attr = self.getAttribute(old_attr_name)
    attr.setName(new_attr_name)
    
  def toSQL(self) :
    old_attributes = self.subrelation.getAttributesName()
    new_attributes = self.getAttributesName()
    columns = ''
    for old_attr, new_attr in zip(old_attributes, new_attributes) :
      columns = columns+',"'+old_attr+'" AS "'+new_attr+'"'
    # remove first ","
    columns = columns[1:]
    # query
    return 'SELECT '+columns+' FROM ('+self.subrelation.toSQL()+')'