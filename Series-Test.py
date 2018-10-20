# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:15:27 2018
Still working on it.

@author: Lihao
"""

#This program contains some functions that can determine whether a serie is conv or div.


import sympy as sm
from math import *
import random as rd
from improper import type1a
from sequence import *


class seriesPool(object):
    series_pool = [("1/x", "div"), ("1/x**2", "conv"), ("1/x**(1/2)", "div"), ("x", "div"), ("(5/3)**x", "div"), ("(1/4)**x", "conv")]
    
    
    def getHelp():
        print("Description of this class")
        return None
    
    def add_series(function, fate):
        try:
            series = str(sm.simplify(function))
            bar = (series, fate)
            seriesPool.series_pool.append(bar)
            return None
        
        except:
            print("Can not simplify this function, please try again. ")
            return None
        
    def get_series():
        theSerie = rd.choice(seriesPool.series_pool)
        return theSerie
    
    def get_All():
        cpy = seriesPool.series_pool.copy()
        return cpy
    
    def load_series(filename):
        '''
        This function loads series into the series_pool list.
        The file has to be txt file, and it must fellow some 
        standard---> Each data set is seperated by a simicolon.
        '''
        if ".txt" not in filename:
            if '.' in filename:
                return "Invalid file type"
            else:
                filename = filename + '.txt'

        try:
            file = open(filename, 'r')
            raw_data = file.read().split(";")
            
            for data in raw_data:
                items = data.split()
                
                if len(items) != 2:
                    print("The data has some problems. Please fellow the standards"\
                          + "each data set is seperated by a simicolon. And each data set contains only two elements.")
                    return None
                
                serie = str(sm.simplify(items[0]))
                fate = items[1].replace(' ', '')
                fate = fate.lower()
                
                if fate != 'conv' or fate != 'div':
                    if fate == 'convergent':
                        fate = 'conv'
                    elif fate == 'divergent':
                        fate = 'div'
                        
                    else:
                        print("It can only be div or conv. ")
                        return None
                    
                seriesPool.add_serie(serie, fate)
                
                
        finally:
            print("Close file")
            file.close()

class evaluate(object):
    '''
    this class contains some function that can evaluate series and sequences,
    for example, it can determines whether a serie is bigger or small than other, or determine wheter a serie is positive or negative.
    '''
    def getHelp():
        print("Description of this class. ")
        return None
    
    def isPositive(serie):
        '''
        This function return a boolean. If the serie is positive for all k, then true, return False otherwise.
        It will calculate the first 100th term of that function's sequence, it all values are positive, the serie must also be positive.
        '''
        func = serie
        try:
            func = str(sm.simplify(func))
        except:
            print("Can not simplify the function. ")
            return None
        
        for x in range(100):
            value = 0
            
            try:
                value = eval(func)
            except:
                value = sm.limit(func, 'x', x)
            
            if value >= 0:
                continue
            
            else:
                print("Failed brute force test, go to other test")
                return evaluate.isPositive(serie)
        #Random testing. 
        for i in range(10):
            x = rd.randint(1000, 5000)
            
            try:
                value = eval(func)
            except:
                value = sm.limit(func, 'x', x)
            
            if value >= 0:
                continue
            
            else:
                print("Failed brute force test, go to other test")
                return evaluate.isPositive(serie)
            
        return True
    
    def positiveTest2(serie):
        pass
    
    def isBigger(serie1, serie2):
        '''
        This function will return True, if serie1 is bigger than serie2, False, if serie2 is bigger.
        It will use brutal force method to compute the first 100th terms of the serie.
        '''
        
        for x in range(100):
            value1 = evaluate.eva(serie1, x)
            value2 = evaluate.eva(serie2, x)
            
            if value1 >= value2:
                continue
            
            else:
                print("Serie2 is bigger than serie1. ")
                return False
         
        print("Serie One is bigger than serie two")
        return True
                
    
    """
    def eva(serie, x): 
        '''
        This function evaluate a serie at k value. 
        k must be an interger, return a float.
        '''
        if x == 1:
            value = 0
            try:
                value = eval(serie)
            except:
                value = float(sm.limit(serie, 'x', 1))
                
            return value
        
        else:
            value = 0
            try:
                value = eval(serie)
            except:
                value = float(sm.limit(serie, 'x', x))
            
            return value + evaluate.eva(serie, x - 1)
      """

    def eva(serie, num):
        
        value = 0
        x = 1
        
        for i in range(num):
            try:
                value = value + eval(serie)
            except:
                value = value + float(sm.limit(serie, "x", x))
            finally:
                x = x + 1
       
        return value         
            
        
        
def paren(term):
    term = str(term)
    term = '(' + term + ')'
    
    return term


def LCT(inputSer):
    '''
    Limit comparison test, return a tuple.
    '''
    ak = inputSer
    series = seriesPool.get_All()
    
    for serie in series:
        bk = serie[0]
        bkFate = serie[1]
        lim = paren(bk) + '/' + paren(ak)
        
        try:
            l = str(sm.limit(lim, 'x', 'oo'))
            if l != 'oo' and l != '0':
                return (bkFate, "No sum", "LCT")
            else:
                continue
        except:
            print("An exception has been rised, Go to TFD. ")
            return TFD(inputSer)
    print("Go to TFD")
    return TFD(inputSer)
        
    
def TFD(series):
    try:
        fate = str(sm.limit(series, 'x', 'oo'))
        if fate == '0':
            print("Go to Ratio Test")
            return Ratio(series)
        
        else:
            return ("Div", "No sum", 'TFD')
    
    except:
        print("An exception has been rised, go to Ratio test")
        #return Ratio(series)
    
def Ratio(serie):
    '''
    Ration test, return a tuple, can only be used when a serie is positive.
    '''
    
    ak = paren(serie)
    ak1 = ak.replace("x", "(x + 1)")
    lim = ak1 + '/' + ak
    
    try:
        R = str(sm.limit(lim, 'x', 'oo'))
        R = float(R)
    except:
        print("Go to RCT, an exceptation has been raised. ")
        return RCT(serie)
    
    if R < 1:
        return ('conv', sumof(serie), 'Ratio')
    
    elif R > 1:
        return ('div', 'No sum', 'Ratio')
    
    elif abs(R - 1) < 0.01:
        print("Go to RCT")
        return RCT(serie)
            
def RCT(inputSer):
    '''
    Direct comparison test, 
    return a tuple contains conv/div, method, and the possible sum of that series.
    '''
    ak = inputSer
    series = seriesPool.get_All()
    
    for func in series:
        
        try:
            bk = func[0]
            fate = func[1]
            flag = evaluate.isBigger(bk, ak)
        except:
            print("An exception has been rised, go to Root test")
            return Root(inputSer)
        
        if fate == "div" and flag == False:
            return ("div", "No sum", "RCT") 
        
        elif fate == 'conv' and flag:
            return ("conv", "No sum", "RCT")
            
    print("Go to Root Test. ")
    return Root(inputSer)        
        
        


def Root(serie):
    ak = paren(serie) + '**(1/x)'
    try: 
        R = str(sm.limit(ak, 'x', 'oo'))
        R = float(R)
        if R == 1:
            print("Go to integral test")
            return ICT(serie)
        
        elif R < 1:
            return ("Conv", "No sum", "Root Test")
        
        elif R > 1:
            return ("Div", "No sum", "Root Test")
    except:
        print("An exception has been raised, go to ICT! ")
        return ICT(serie)


def ICT(serie):
    '''
    Integral comparison test. 
    Take a series as the only one argument 
    Ruturn their items. The the conv/div of the serie, the sum, and the method used to determined the series.
    
    '''
    func = str(sm.simplify(serie))
    flag = seq.isIncreasing(func)
    
    if flag:
        print("Can not apply Integral test, Go to GST.")
        return GST(serie)
    
    lim = type1a(func, 1)
    if lim == 'oo' or lim == '-oo':
        return ("div", "No sum", "ICT")
    
    else:
        return("conv", "No sum", "ICT")
    
        


def sumof(serie):
    pass

def GST(inputSer):
    
    terms = []
    for x in range(1, 5):
        try:
            value = sm.limit(inputSer, "x", x)
            term = float(value)
        except:
            term = eval(inputSer)
        terms.append(term)
    
    print(terms)
    r = terms[1]/terms[0]
    a = terms[0]
    num = abs (terms[1]/terms[0] - terms[2]/(terms[0]*terms[1]) )
    num2 = abs (terms[2] - terms[3]/r)
    
    if num < 0.01 and num2 < 0.01:
        sum1 = a/(1 - r)
        return ("conv", sum1 , "GST")
    
    else:
        return ("Div", "No sum", "GST")

def partialSum(serie):
    pass


def test(series):
    series = str(sm.simplify(series))
    result = LCT(series)
    
    fate = result[0]
    sumofseries = result[1]
    method = result[2]
    
    dic = {"sum":sumofseries, "fate": fate, "method":method}
    return dic


def AtST(Ser):
    """
    Alternating serie test can determine the conv/div of an alternating series.
    It will return a string that state that series' conv/div. It can be 'conditional conv', 'absolute conv', or 'div'
    """

    absulote = Ser.replace("-", "")
    result = test(absulote)
    
    if result[1] == "conv":
        return "absolute convegent"
    else:
        #Other method.
        pass
    
class autoTest(object):
    '''
    This class can help testing the series_test function.
    It consist of three parts. The class variables which are the inputs with the correct outputs
    The adder parts, which is some methods that can add data to the class variables
    And the last part is the testing parts, which is a method that can test
    
    
    '''
    dataPool = {"1/x":("div", "No sum"), "1/x^2": ("conv", "No sum")}
    keys = ["1/x", '1/x^2']
    
    def get_data():
        key = rd.choice(autoTest.dataPool)
        inputs = key
        outputs = autoTest.dataPool[key]
        
        return (inputs, outputs)
    
    def add_data(inputs, output):
        '''
        Add data to the class var, it takes a string as the first argument.
        and a tuple contains two strings as its second argument
        '''
        try:
            inputs = str(sm.simplify(inputs))
        except:
            print("Can not simplify the input wiht sympy library. ")
            return None
        
        if type(output) != tuple or len(output) != 2:
            print("The second argument does conform with the standard. ")
            return None
        
        autoTest.keys.append(inputs)
        autoTest.dataPool[inputs] = output
        return None
    
    def getHelp():
        print("Description of this class. ")
        return None
    

    def load_data(filename):
        '''
        This method can load data from a txt file. 
        The txt file has to fellow certain standard.
        Each data set has to be seperated by a simicolon.
        And in each data set, items are seperate by commas.
        '''
        if ".txt" not in filename:
            filename = filename + ".txt"
        
        try:
            dataFile = open(filename, 'r')
        
        except IOError:
            print("Please enter the correct file name, and make sure it is a txt file.")
            return None
        
        try:
            rawData = dataFile.read()
        except:
            print("Can not read the file. Please make it fellows the standard")
            dataFile.close()
            return None
        
        finally:
            dataFile.close()
            
        dataSets = rawData.split(";")
        
        counter = 0
        for data in dataSets:
            data = data.replace(" ", '')
            items = data.split(",")
            
            if len(items) != 3:
                counter += 1
                print("Invalid data, skip to the next data set->> Index:", counter)
                continue
            
            #Load the data into class variable, 
            serie = items[0]
            fate = items[1].lower()
            serieSum = items[2]
            
            if 'x' not in serie:
                print("Skip, invalid variables")
                continue
            
            if fate != "conv" and fate != "div":
                print("The function does not support alternating serie test.")
                continue
            
            autoTest.keys.append(serie)
            autoTest.dataPool[serie] = (fate, serieSum)
        
        return None
    def Unit_test(function):
        pass 
    def Integrated_test():
        pass 



def auto_test(filename):
    if ".txt" not in filename:
        filename = filename + ".txt"
        
    file = open(filename, 'r')
    
    try:
        header1 = file.readline()
        nums = header1.split("$")
        
        input_num = int(nums[0])
        output_num = int(nums[1])
        
        items = file.read().split(";")
        inputs = []
        outputs = []
        
        for item in items:
            
            item.replace("{", '')
            item.replace("}", '')
            
            term = item.split(",")
            
            if len(term) != input_num + output_num:
                return "Something is wrong!"
            
            i = term[:input_num]
            o = term[input_num:]
            
            inputs.append(i)
            outputs.append(o)
        
        return (inputs, outputs)
            
    finally:
        print("Close File! ")
        file.close()             
    
                    
def write():
    
    filename = input("Please enter the filename here: ")
    if ".txt" not in filename:
        filename = filename + ".txt"
        
    file = open(filename, "w")
    
    try:
        num1 = int(input("How many inputs is there: "))
        num2 = int(input("How many outputs are there: "))
    
        header = str(num1) + "$" + str(num2) + "\n"
    
        file.write(header)
        
        print("Enter stop to break the loop: ")
        while True:
            foo = []
            
            for i in range(num1):
                print("Please enter the", i + 1, "input: ", end = '')
                input1 = input("")
                if input1 == 'stop':
                    break
                foo.append(input1)
                
            if "stop" in foo:
                break
            
            for j in range(num1):
                print("Please enter the", i + 1, "output: ", end = '')
                output = input("")
                if output == 'stop':
                    break
                foo.append(output)
                
            if "stop" in foo:
                break
            
            bar = ''
            for k in range(len(foo)):
                bar = bar + str(foo[k]) + ','
            bar = "{" + bar + "}"
            
            file.write(bar)
            

    finally:
        print("Close the file.")
        file.close()              
            
        
        
    
    
