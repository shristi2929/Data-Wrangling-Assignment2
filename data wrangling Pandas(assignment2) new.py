#import the necessary libraries

import pandas as pd
#Import the dataset from this(https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
#Use sep= "|" while reading the data
#Assign it to a variable called users and use the 'user_id' as index
user = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",sep='|',index_col = 'user_id')
user

###See the first 10 and last 10 entries
print("--------First 10 entries -------")
print(user.head(10))
print("--------last 10 entries -------")
print(user.tail(10))

##What is the number of observations in the dataset?

print("Number of Observations : ",len(user))

##What is the number of columns in the dataset?

print("Number of Columns :", len(user.columns)) 

###Print the name of all the columns.

user.columns

###How is the dataset indexed?

user.index

##What is the data type of each column?

user.info()

##Print only the occupation column

user.occupation

user["occupation"]

###How many different occupations are in this dataset?

n = user.occupation
z = n.nunique()
z
user["occupation"].nunique()

#What is the most frequent occupation?
user['occupation'].mode()

#DataFrame Info.

user.info()

#Describe all the columns

user.describe()

#Summarize only the occupation column
user.groupby("occupation")["occupation"].count().sort_values()

#What is the mean age of users?
user["age"].mean()

#What is the age with least occurrence?
user["age"].value_counts().idxmin()