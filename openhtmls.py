#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:22:34 2017

@author: sherlok (Marios Kefalas)

This script goes through a directory with
html files and retains the body of the htmls
by invoking htmls.py

It returns a data frame with all the bodies of the
html files.

"""

#### import modules and packages ####
import os
# import io
import pandas as pd
# from Emails import Emails
from htmls import htmls

def openhtmls(path):
    
    d = []
#    names = []
    
    #### diving into the directory ####
    for root, dir_names, file_names in os.walk(path):
       for file_name in file_names:
           
            x = os.path.join(root,file_name)
            #### invoking htmls.py ####
            res = htmls(x)
            
            d.append(res)
            #names.append(x)
            
            
    Data = pd.concat(d, axis = 0, ignore_index = True)
    return Data #,names