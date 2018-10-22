# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:26:56 2018

@author: Lihao

This class can calculate the Center of mass of an object.
It also contains some methods duel with store the result.
"""
"""
    Welcome My friends from github.
    Suggestions are welcome Here
    
    ###
"""



import os

class CenterOfMass(object):
    COM = {"TotalMass":0, "coord":(0,0,0)}
    massPoints = []
    
    def getHelp(func=''):
        print("Description of this class.")
        func = str(func)
        
        if func.lower() == "addmasspoint":
            print("Add Mass methods can check and add data of a mass point to the class var.")
            
        elif func.lower() == "calculate":
            print("The calculate methods calculate the COM of those mass point. It will return a dictionary that contains the tatol math, and the coords of the COM.")
            
        elif func.lower() == "addc":
            print("Add and calculates the center of mass at the same time.")
            
        return None
    
    def addMassPoint(Mass,Coord=(0,0,0)):
        """
        Excepted a float as the first input, and a tuple of float as its second output.
        This methods add a mass point to the class var, and it will not return a value.
        """
        massPoint = {"mass":0, "coord":()}
        massPoint['mass'] = float(Mass)
        massPoint['coord'] = Coord
        
        CenterOfMass.massPoints.append(massPoint)
        return None
    
    def reset():
        #Reset every class variables to the initial value.
        CenterOfMass.COM["TotalMass"] = 0
        CenterOfMass.COM["coord"] = (0,0,0)
        
        CenterOfMass.massPoints.clear()
        return None
    
    def printCOM():
        #Print out the Center of Mass
        
        tatol = CenterOfMass.COM["TotalMass"]
        coord = CenterOfMass.COM["coord"]
        
        print("Tatol Mass-->", tatol,"\nCoordinate-->",coord)
        return None
    
    def getCOM():
        #Return a dictionary that it contains the Tatol Mass and the Coordinate of the center of the mass.
        dic = CenterOfMass.COM.copy()
        return dic

    def calculate():
        #This method calculate the center of mass from the class variable and store to the COM class vari.
        
        mPoints = CenterOfMass.massPoints.copy() 
        
        x_mass = 0
        y_mass = 0
        z_mass = 0
        TotalMass = 0
        
        for i in range(len(CenterOfMass.massPoints)):
            
            Coord = mPoints[i]["coord"]
            Mass_i = mPoints[i]["mass"]
            
            TotalMass += Mass_i
            x_mass = x_mass + Coord[0]*Mass_i
            y_mass = y_mass + Coord[1]*Mass_i
            z_mass = z_mass + Coord[2]*Mass_i
        
        x_coord = round(x_mass/TotalMass, 4)
        y_coord = round(y_mass/TotalMass, 4)
        z_coord = round(z_mass/TotalMass, 4)
        TotalMass = round(TotalMass, 4)
        
        COM_coord = (x_coord, y_coord, z_coord)
        CenterOfMass.COM["TotalMass"] = TotalMass
        CenterOfMass.COM["coord"] = COM_coord
        
        return None
    
    def addC(mass, coord=(0,0,0)):
        #Add and calculate the result.
        CenterOfMass.addMassPoint(mass, coord)
        M = mass + CenterOfMass.COM["TotalMass"]
        CenterOfMass.COM["TotalMass"] = M
        
        x_shift = round(mass*coord[0]/M, 4)
        y_shift = round(mass*coord[1]/M, 4)
        z_shift = round(mass*coord[2]/M, 4)
        
        CenterOfMass.COM["coord"][0] += x_shift
        CenterOfMass.COM["coord"][1] += y_shift
        CenterOfMass.COM["coord"][2] += z_shift
        
        return None
        
    def load(filename, file_path=None):
        #Loading standards ---> "mass, x coord, y coord, z coord;"
        
        if ".txt" not in filename:
            
            if '.' in filename:
                print("Can not read text file. ")
                return None
            else:
                filename = filename + ".txt"
                
        
        if file_path == None:
            
            try:
                file = open(filename, "r")
            
            except IOError:
                print("Can not open the file")
                return None
            
        else:
            try:
                os.chdir(file_path)
                file = open(filename, "r")
                    
            except IOError:
                print("Can not open the file")
                return None
            
            except:
                print("Other errors, It can be a invadld path.")
                return None
            
        try:
            raw_data = file.read()
        except:
            print("Can not read the file.")
        
        file.close()
        
        #For data to works, it must fellow some standards.
        raw_data = raw_data.strip(" \n")
        data_set = raw_data.split(";")
        
        for data in data_set:
            components = data.split(",")
            if len(components) != 4:
                print("Invalid data set, skip this components")
                continue 
            
            mass1 = float(components[0])
            x = float(components[1])
            y = float(components[2])
            z = float(components[3])
            
            CenterOfMass.addMassPoint(mass1, (x, y, z))
            
        CenterOfMass.calculate()
        print("Loading complete! ")
        return None
        
                
            
        
            
    
    def store(file_name, filePath=None):
        
        if filePath == None:
            file = open(file_name, "w")
        
        else:
            
            try:
                os.chdir(filePath)
                file = open(file_name, "w")
                
            except:
                print("Invalid file path.")
                return None
        
        COM  = CenterOfMass.getCOM()
        massPoints = CenterOfMass.massPoints.copy()
        #Write The Center of Mass.
        storedCOM = "Tatol Mass----->>>" + str(COM["TotalMass"]) + "\nThe Coordinate of the Center Of Mass------>>>" + str(COM["coord"]) + "\n\n"
        file.write(storedCOM)
        file.write("--------------------------------Here are the mass points--------------------------\n")
        
        for i in range(len(massPoints)):
            mass_i = massPoints[i]["mass"]
            coordinate = massPoints[i]["coord"]
            
            content = "The mass" + str(i + 1) + "------->>>" + "The mass is: " + str(mass_i) + ',  ' + "The Coordinate is: " + str(coordinate)
            file.write(content + "\n")
            
        print("Store successful.")
        
        try:
            #print("Bugs! Bugs!")
            print("")
        finally:
            file.close()
            return None            
        

#short hands.
def gCOM():
    CenterOfMass.getCOM()
    return None

def add(mass, coord=(0,0,0)):
    CenterOfMass.addMassPoint(mass,coord)
    return None
    