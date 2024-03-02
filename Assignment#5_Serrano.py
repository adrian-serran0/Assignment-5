# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:33:42 2024

@author: adrian
"""
import math

class Basic_Math_Operations:
    
    def __inti__(self):
        self.firstn = firstn
        self.lastn = lastn
    
#1 ========================================   

    def greet(self,firstn,lastn):
        print(f"Hello, {firstn} {lastn}.")
        
#2 ========================================    
    
    @staticmethod
    def sums():
        num1 = int(input("What is the value of number one? "))
        num2 = int(input("What is the value of number two? "))
        s = num1 + num2 
        return s

#3 ========================================    

    def perform_opp(self,num1,num2,oper):
        if oper == 'add':
            answer = num1+num2
        elif oper == 'subtract':
            answer = num1-num2
        elif oper == 'multiply':
            answer = num1*num2
        elif oper == 'divide':
            answer = num1/num2
        return answer

#4 ========================================    
    
    def square(self,num):
        s = num*num
        return s
    
#5 ========================================    
    
    def factorial(self,num):
        if num < 0:
            print("Factorial Error.")
        elif num == 1 or num == 0:
            print("1")
        else:
            fact = 1 
            while(num > 1):
                fact = fact*num
                num = num-1
            print(fact)
            return fact 
        
#6 ========================================    
        
    def count(self,start,end):
        print(start)
        for num in range(start,end):
            start = start+1
            print(start)
            
#7 ========================================    
            
    def hypotenuse(self):
        base = int(input("What is the base length? "))
        perpen = int(input("What is the perpendicular edge length? "))
        a = self.square(base)
        b = self.square(perpen)
        c = round(math.sqrt(a+b),3)
        return c  
    
#8 ========================================    

    def rec_area(self,width,height):
        area = width*height
        return area
    
#9 ========================================    
    
    def power(self,base,exponent):
        answer = base**exponent
        return answer
    
#10========================================    
    
    def return_type(self,value):
        x = type(value)
        return x
    
    
#Program ________________________________________________________________________

x = Basic_Math_Operations()

Yes = True

while Yes == True:
    
    print('---------------------------------------------')
    choice = input("What would you like to do? The choices are: \n '1' Greet user, \n '2' Sum two numbers, \n '3' Perform any Opperation, \n '4' Square a number, \n '5' Factorial a number, \n '6' Count from one number to another, \n '7' Find a Hypotenuse, \n '8' Find the area of a Rectangle, \n '9' Calculate an expotented numvber, \n '10' Return the Data type, \n or 'Exit'? ")
    print('---------------------------------------------')
    
    if choice == 'Exit':
        Yes = False
        
#1 ========================================   
  
    elif choice == '1':

        firstn = input("Enter the first name. ")
        lastn = input("Enter the last name. ")
        y = x.greet(firstn, lastn)
        
#2 ========================================
        
    elif choice == '2':
        print('The answer is', x.sums())
        
#3 ========================================
        
    elif choice == '3':
        num1 = int(input("What is number one? "))
        num2 = int(input("What is number two? "))
        oper = input("What is the opperation? Choose: 'add','subtract','multiply', or 'divide'. ")
        y = x.perform_opp(num1, num2, oper)
        print('The answer is', y)
#4 ========================================
        
    elif choice == '4':
        numy = int(input("What number would you like to square? "))
        y = x.square(numy)
        print('The square is', y)
        
#5 ========================================
        
    elif choice == '5':
        num = int(input("What number factorial would you like to take? "))
        y = x.factorial(num)
        
#6 ========================================
        
    elif choice == '6':
        start = int(input("What is the starting value? "))
        end = int(input("What is the ending value? "))
        y = x.count(start, end)
        
#7 ========================================
    
    elif choice == '7':
        y = x.hypotenuse()
        print('The hypotenuse is', y)
        
#8 ========================================
        
    elif choice == '8':
        width = int(input("What is the width of the rectangle? "))
        height = int(input("What is the height of the rectangle? "))
        y = x.rec_area(width, height)
        print('The area is', y)
        
#9 ========================================
        
    elif choice == '9':
        base = int(input("What is the base of the exponential? "))
        exponent = int(input("What is the exponent? "))
        y = x.power(base, exponent)
        print('The answer is', y)
        
#10 ========================================
        
    elif choice == '10':
        value = input("What is the object you want the data type for? ")
        y = x.return_type(value)
        print(y)
        
        
   