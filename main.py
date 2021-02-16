#####################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Name: Diana Toh, Jamie Liew
#Group Name: yaypython
#Class: PN2004J
#Date: ddMMyyyy
#Version: 3.0
#####################################################################

#####################################################################
#Pandas - is a fast powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language
#Import pandas for data analysis
import pandas as pd
#####################################################################
#Import Pandas Library for Data Analysis
######################################################

######################################################
#Class Branch - Data Analysis
#Load excel data (CSV format) to dataframe
#######################################################
class DataAnalysis:
  def __init__ (self):

    #Load excel data (CSV format) to dataframe - 'df'
    df = pd.read_csv('SEAregion20002010.csv')
    #show specific country dataframe
    TopCountries(dataframe)
########################################################
#Class Branch: End of code
########################################################

########################################################
#Function Branch - sortCountry
#Parses data and displays sorted result(s)
########################################################
def TopCountries(df):

  #Print dataframe (rows and columns)
  print("The following dataframe for SEA from 2000 to 2010 are read as follows: \n"
  print(df)
  
  #Sum of visitors per country
  Sumofcountries = sum(df.rows))

  #Sort the countries in descending order
  SortCountries = []
  SortCountries = df.sort(Sumofcountries, descending=[0])
  Topthree = SortCountries[:2]
  print(Topthree)
  
  return
#################################################
#Function Branch: End of code
###################################################

#################################################
#Main Branch
##################################################
if __name__ == '__main__':
    
  #Project Title
  print('#################################')
  print('# Data Analysis App - PYTHON PROJECT #')
  print('#################################')

  #perform data analysis on specific excel (CSL) file
  DataAnalysis()

#####################################################
#Main Branch: End of Code
####################################################