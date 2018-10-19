# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 10:10:19 2018

@author: Lihao
"""

import sympy as sm
from math import *
import pyautogui as auto
import os


def fac(num):
    """
    This function is factorial function
    """
    counter = num
    result = 1
    for i in range(counter):
        result = result * (num - i)
        
    return result

def paren(term):
    return "(" + term + ")"



#Old functions and implementation.    
def term(value, order, position):
    if value == 0:
        return "0"
    
    base = fac(order)
    result = str(value) + '*' + 'x^' + str(order) + '/' + str(base)
    
    if position == 0:
        return result
    
    else:
        var = "x-" + str(position)
        var = paren(var)
        result = result.replace("x", var)
        
        return result

def value(function, order, x):
    '''
    The function is about the slope of the tangentline.
    It takes two input, function and order.
    One output that return the value of that derivative function at that many order.
    '''
    dire = sm.diff(function, 'x', order)
    dire = str(dire)
    result = 0
    
    try:
        result = sm.limit(dire, "x", x)
        result = float(result)
    except:
        result = eval(dire)
    
    return round(result, 4)

def Taylor(function, order = 6, position = 0):
    TaylorPoly = []
    for i in range(order):
        value123 = value(function, i, position)
        term1 = term(value123, i, position)
        TaylorPoly.append(term1)
        
    result = ""
    for j in TaylorPoly:
        result = result + '+' + j
        
        
    return result

def getTaylor():
    """
    This function implment the Taylor functions, and it can interact with
    the files.
    It takes no input, and return a dictionary that use the functions as keys, and
    in each entries, is a list of the taylor polynomials/
    """
    
    file = open("functions.txt", "r")
    
    raw_data = file.read()
    file.close()
    raw_data = raw_data.strip(" \n")
    functions = raw_data.split(";")
    
    taylorPoly = {}
    for func in functions:
        polys = []
        try:
            for i in range(1, 12):
                poly = Taylor(func, i)
                polys.append(poly)
                
            taylorPoly[func] = polys
        
        except:
            continue
    
    return taylorPoly
            
def screen(funcName, order):
    pass
    
            
def export():
    """
    export the functions to the desmon graphing website, and then take picture of it.
    Then store the function in a folder.
    """
    pass
    
        