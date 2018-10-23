# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:23:45 2018

@author: Lihao
"""
import math

class vector(object):
    def __init__(self ,i ,j , k):
        self.x = i
        self.y = j
        self.z = k
        
    def magnitude(self):
        num = self.x**2 + self.y**2 + self.z**2
        return round(math.sqrt(num), 2)
    
    def __add__(self,other):
        v3x = self.x + other.x
        v3y = self.y + other.y
        v3z = self.z + other.z
        
        return vector(v3x, v3y, v3z)
    
    def __sub__(self, other):
        v3x = self.x - other.x
        v3y = self.y - other.y
        v3z = self.z - other.z
        
        return vector(v3x, v3y, v3z)
    
    def __str__(self):
        x_coord = round(self.x, 4)
        y_coord = round(self.y, 4)
        z_coord = round(self.z, 4)
        
        
        i = '(' + str(x_coord) + 'i^' + ')'
        j = '(' + str(y_coord) + 'j^' + ')'
        k = '(' + str(z_coord) + 'k^' + ')'
        
        if self.x == 0:
            return j + ' + ' + k
        
        elif self.y == 0:
            return i + ' + ' + k
        
        elif self.z == 0:
            return i + " + " + j
    
        else:
            return i + " + " +  j + " + " + k
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    
    def dot(self,other):
        num1 = self.x * other.x
        num2 = self.y * other.y
        num3 = self.z * other.z
        
        return num1 + num2 + num3
    
    def cross(self,other):
        v3x = other.y * self.z - other.z * self.y
        v3y = other.z * self.x - other.x * self.z
        v3z = other.x * self.y - other.y * self.x
        
        return vector(v3x, v3y, v3z)
    
    def angle(self, other):
        v3 = vector.cross(self,other)
        v1mag = self.magnitude()
        v2mag = other.magnitude()
        v3mag = v3.magnitude()
        
        angle = math.asin(v3mag/(v1mag*v2mag))
        return round(math.degrees(angle), 3)
    
    def anglefromaxis(self, axis):
        if axis == 'x':
            angle = math.atan(abs(self.y)/abs(self.x))
            angle = round(math.degrees(angle), 2)
            
            if self.y >= 0 and self.x >= 0:
                return angle
            
            elif self.y >= 0 and self.x <= 0:
                return 180 - angle
            
            elif self.y <= 0 and self.x <= 0:
                return 180 + angle
            
            else:
                return 360 - angle
            
        
        elif axis == 'z':
            magnitude = self.magnitude()
            base = math.sqrt(self.x ** 2 + self.y **2)
            
            angle = math.asin(base/magnitude)
            angle = math.degrees(angle)
            
            return round(angle, 2)
        
        else:
            print("The parameter can only be 'x' or 'z'. ")
            
    def getVec(angle, magnitude):
        #Return a instance of vector, by it is angle and magitude.
        #Only support 2D.
        if angle < 0:
            angle = 360 + angle
            
        elif angle > 360:
            angle = angle - 360
        
        if angle > 0 and angle <= 90:
            relAngle = math.radians(angle)
            x_coord = magnitude * math.cos(relAngle)
            y_coord = magnitude * math.sin(relAngle)
            
            return vector(x_coord, y_coord, 0)
        
        elif angle > 90 and angle <= 180:
            relAngle = math.radians(angle - 90)
            
            x_coord = magnitude * math.cos(relAngle) * (- 1)
            y_coord = magnitude * math.sin(relAngle)
            
            return vector(x_coord, y_coord, 0)
        
        elif angle > 180 and angle <= 270:
            relAngle = math.radians(angle - 180)
            
            x_coord = magnitude * math.cos(relAngle) * (- 1)
            y_coord = magnitude * math.sin(relAngle) * (- 1)
            
            return vector(x_coord, y_coord, 0)
            
        else:
            relAngle = math.radians(angle - 270)
            
            x_coord = magnitude * math.cos(relAngle)
            y_coord = magnitude * math.sin(relAngle) * (- 1)
            
            return vector(x_coord, y_coord, 0)
            
            
        
            
            
        
        
            
    
        
        
        
        
        
        
    
        
    
            
            
        