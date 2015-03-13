# -*- coding: utf-8 -*-
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if atMe.name[0] > newFrob.name[0]:
        atMe.setBefore(newFrob)
        newFrob.setAfter(atMe)
    else:
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
