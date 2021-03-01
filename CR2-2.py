#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:12:19 2021

@author: elliotede
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_columns(fig_type,x,y,plot_type):
    #This conditional ensures the colums of y are less than or equal to 10 
    if y.shape[1] > 10:
        print('Too many colums. Require columns to be less than or equal to 10')
    #This forces the user to input matrices of the same shape
    if x.shape != y.shape:
        print("x and y have different shapes")
        return
    else:
        #If the user choses each plot to be a subplot
        if  fig_type == "subplots":
            k = round(x.shape[1]//2)
            fig , ax = plt.subplots(2,k)
            #We loop i through 0 to the number of columns in x
            for i in range(x.shape[1]):
                #Starting a list for x and y co-ordinates
                x_d = []
                y_d = []
                #We loop j through 0 to number of rows in x
                for j in range(x.shape[0]):
                    #We add the entry in the jth row and ith column of x to x_d
                    x_d.append(x[j][i])
                    #We add the entry in the jth row and ith column of y to y_d
                    y_d.append(y[j][i])
                #If user chooses line plot
                if plot_type == "line":
                    ax[i//k, i - (i//k)*k].plot(x_d, y_d, label = "row " +str(i) )
                #If user chooses scatter plot
                elif plot_type == "scatter":
                    ax[i//k, i - (i//k)*k].scatter(x_d, y_d, label = "row " +str(i))
                #Ensures user can only input line or scatter
                else:
                    print("incorrect plot_type")
            plt.show() 
        #If the user choses to draw all plots on the same axes    
        elif fig_type == "single" :
            #We start off our plot
            fig = plt.figure()
            #We loop i through from 1 to the number of columms in x
            for i in range(x.shape[1]):
                #Starting off a list for the x and y co-ordinates
                x_d = []
                y_d = []
                #We loop j through 0 to number of rows in x
                for j in range(x.shape[0]):
                    #We add the entry in the jth row and ith column of x to x_d
                    x_d.append(x[j][i])
                    #We add the entry in the jth row and ith column of y to y_d
                    y_d.append(y[j][i])
                #If user chooses line plot
                if plot_type == "line":
                    plt.plot(x_d, y_d, label = "row " +str(i) )
                #If user chooses scatter plot
                elif plot_type == "scatter":
                    plt.scatter(x_d, y_d, label = "row " +str(i))
                #Ensures that user only puts line or scatter
                else:
                    print("incorrect plot_type")
            #We add a legend and we plot it
            plt.legend()
            plt.show()
        #We ensure the user inputs the correct figure type
        else:
            print("incorrect fig_type")      
        
x1 = np.array([[1,2,3,2],[2,6,7,3],[3,6,7,4]])
y1 = np.array([[2,5,3,5],[5,8,6,1],[-1,5,3,7]])

plot_columns("single", x1, y1,"line")
plot_columns("subplots",x1 , y1,"scatter")

#Uncomment tests below to run them instead of ones above
#x2 = np.array([[1,4,3,3],[2,4,5,3],[3,4,7,4]])
#y2 = np.array([[1,5,np.pi,2],[2,6,7,3],[3,6,7,4]])

#plot_columns("single", x2, y2,"line")
#plot_columns("subplots", x2, y2,"scatter")

#x3 = np.array([[1,-3,3,5],[1,6,7,10]])
#y3 = np.array([[2,5,3,6],[5,8,6,8]])

#plot_columns("single", x3, y3,"line")
#plot_columns("subplots",x3 , y3,"scatter")

#x4 = np.array([[1,2,3,2],[2,6,7,3]])
#y4 = np.array([[2,5,3/4,5],[5,8,6,1]])

#plot_columns("single", x4, y4,"line")
#plot_columns("subplots",x4 , y4,"scatter")

