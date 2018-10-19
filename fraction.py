# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 19:25:05 2018

@author: Lihao
"""
import sympy as sm

class fraction(object):
    def __init__(self, top, bottom):
        try:
            top = sm.simplify(top)
            bottom = sm.simplify(bottom)
            top = str(top)
            bottom = str(bottom)
    
            self.top = top
            self.bottom = bottom
            
        except:
            print("Something went wrong, Please fellow python standard notation.")
            return None
        
    def __str__(self):
        nume = "(" + self.top + ")"
        demo = "(" + self.bottom + ")"
        return nume +'/' + demo
    
    def __eq__(self, other):
        if self.top == other.top and self.bottom == other.bottom:
            return True
        else:
            return False
    
    def __mul__(self, other):
        nume = self.paren()[0] + '*' + other.paren()[0]
        demo = self.paren()[1] + '*' + other.paren()[1]
        
        try:
            nume = str(sm.simplify(nume))
            demo = str(sm.simplify(demo))
            
            return fraction(nume, demo)
        except:
            print("Something is wrong, try again with different notation please.")
            return None
        
    def paren(self):
        nume = "(" + self.top + ')'
        deno = "(" + self.bottom + ')'
         
        return (nume, deno)
    
    def __add__(self, other):
        terms = fraction.adder(self, other)
        deno = terms[0]
        numer = terms[1] + '+' + terms[2]
        try:
            deno = str(sm.simplify(deno))
            numer = str(sm.simplify(numer))
            
            return fraction(numer, deno)
        except:
            print("Something was wrong with addition")
            return None
        
    def adder(self, other):
        selftop = self.paren()[0]
        selfbottom = self.paren()[1]
        
        othertop = other.paren()[0]
        otherbottom = other.paren()[0]
        
        deno = selfbottom + '*' + otherbottom
        term1 = selftop + '*' + otherbottom
        term2 = othertop + '*' + selfbottom
        
        return (deno, term1, term2)
    
    def __sub__(self, other):
        terms = fraction.adder(self, other)
        numer = terms[1] + '-' + terms[2]
        denom = terms[0]
        
        try:
            top = str(sm.simplify(numer))
            bottom = str(sm.simplify(denom))
            
            return fraction(top, bottom)
        
        except:
            print("Something wrong with the sub.")
            return None
        
    def get_numer(self):
        return str(self.top)
    
    def get_denom(self):
        return str(self.bottom)
    
    def set_numer(self, numer = ''):
        
        self.top = numer
        return self
    
    def set_denom(self, denom):
        try:
            denom = str(denom)
            if denom != '0':
                self.bottom = denom
                return self
            else:
                print("Division by Zero")
                return None
        except:
            print("Soemthing was wrong with set_denom.")
            
    def reset(self):
        numer = str(sm.simplify(self.top))
        denom = str(sm.simplify(self.bottom))
        
        return fraction(numer, denom)
            
            
    def __division__(self, other):
        numer1 = self.paren()[0]
        denom1 = self.paren()[1]
        numer2 = other.paren()[0]
        denom2 = other.paren()[1]
        
        new_numer = numer1 + '*' + denom2
        new_denom = denom1 + '*' + numer2
        
        try:
            top = str(sm.simplify(new_numer))
            bottom = str(sm.simplify(new_denom))
            
            return fraction(top, bottom)
        except:
            print("something was wrong here")
            return None
        
        
    def evaluate(self, value):
        numer = str(sm.simplify(self.top))
        denom = str(sm.simplify(self.bottom))
        
        x = value
        numerval = eval(numer)
        denomval = eval(denom)
        
        return numerval/denomval
        
        
        
        