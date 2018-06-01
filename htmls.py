#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:58:11 2017

@author: (Marios Kefalas)

This script takes as input a path to an 
html document and returns its body as a
data frame

"""

#### import modules and packages ####
#import re
import string
from bs4 import BeautifulSoup
#import numpy as np
import pandas as pd


def htmls(path):
    
    # opening html file
    html = open(path, 'r')
    
    # parsing html file with beautiful soup
    soup = BeautifulSoup(html, 'html.parser')
    
    # extracting body only
    final1 = []
    try:
        txt = soup.body.get_text() #.encode('utf-8', 'ignore')  #cp1252
    except AttributeError:
        txt = soup.get_text()
#        
#    if (soup.body):
#        txt = soup.body.text #.encode('utf-8', 'ignore')  #cp1252
    printable = set(string.printable)
    final = filter(lambda x: x in printable, txt)
#        pat1 = r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'    
#        pat2 = '[\\w\\.-]+@[\\w\\.-]+' #r'[A-Za-z0-9-_]+[@\.]+[A-Za-z0-9-_]+\.+com'
#        pat3 = r'\d'
#        pat4 = r'[+%\<\>:]'
#        pat5 = r'[\r\n\t]'
#        cmb_pat = r'|'.join((pat1,pat2,pat3,pat4,pat5))
    final1.append(final) #re.sub(cmb_pat,'', final))
        
    df = pd.DataFrame({'Body': final1})
    
    return df



