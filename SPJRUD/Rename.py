from Relation import Relation, Attribute
from functions import *
from copy import deepcopy


class Rename(Relation) :
  def __init__(self, old_attr_name, new_attr_name, subrelation) :
    # check and save subrelation
    self.subrelation = check_relation(self, subrelation, 'subrelation')
    
    # copy attributes and rename one
    self.setAttributes(deepcopy(subrelation.getAttributes()))
    
    # check that new name does not exists already
    existing = self.getAttribute(new_attr_name, False)
    if existing :
      self.error('attribute name "'+new_attr_name+'" already exists in subrelation')
    
    # save new name
    attr = self.getAttribute(old_attr_name, True, 'subrelation')
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
