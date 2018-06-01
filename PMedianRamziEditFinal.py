#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pulp import *
import pandas as pd
import numpy as np
import time


'''
# You can uncomment this code block if you would like to import 
# a dictionary of dictionaries and convert into a pandas dataframe

def load_obj(name ):
    with open('/home/vagrant/Downloads/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
D = load_obj('dictionary_D')

pandas_D = pd.DataFrame.from_dict(D)

# make sure your demands are the rows in order to run without modifying code
print('print pandas_D')
print(pandas_D)
'''


# 
pandas_from_csv = pd.read_csv('/Users/Ramzi/Desktop/JustDistanceNoWeightsWTesla.csv',header=0,index_col='ID')
#print('print pandas_from_csv')
#print(pandas_from_csv)

#get column keys
# test_pd.keys()

# get row keys
# test_pd.index

# Assumes that the column headers are the potential origins/facilities points
# and the rows are the demand points
facilities = pandas_from_csv.keys()
# facilities = pandas_D.keys()

# convert all strings in keys to a list of integers
facilities = list(map(int, facilities))  

print('print D keys (origins)')
print(facilities)

demand = pandas_from_csv.index
# demand = pandas_D.index

demand = list(map(int, demand))

print('print demand points')
print(demand)

# start counting time
t1=time.time()

p = 16 #  number of locations to optimize to

# decision variables
# This is same as X = LpVariable.dicts('X_%s_%s', (location), cat = 'Binary', lowBound = 0, upBound = 1)
# but shorter and a format speficier is not needed.

# declare facility variables
X = LpVariable.dicts('X',(facilities),0,1,LpInteger)

# declare demand variables
Y = LpVariable.dicts('Y', (demand,facilities),0,1,LpInteger) 

# create the LP object, set up as a MINIMIZATION problem
prob = LpProblem('P Median', LpMinimize)

# prob += sum(sum(D[i][j] * Y[i][j] for j in location) for i in demand)
# pandas iloc looks up values by row(i) and column(j)
prob += sum(sum(pandas_from_csv.iloc[i,j] * Y[i][j] for j in facilities) for i in demand)

# set up constraints
# This is same as prob += sum([X[j] for j in location]) == p
prob += lpSum([X[j] for j in facilities]) == p

# For Q-coverage problems, modify the constraint below and instead of '== 1' 
# make it equal to the number of facilities that need to service each demand
for i in demand: prob += sum(Y[i][j] for j in facilities) == 1

for i in demand:
    for j in facilities: 
        prob +=  Y[i][j] <= X[j]
     
# constraint below is is in example if you want to make location 105 an existing facility        
prob += X[0] == 1
prob += X[1] == 1
prob += X[2] == 1
prob += X[3] == 1
prob += X[4] == 1
prob += X[5] == 1
prob += X[6] == 1
prob += X[7] == 1
prob += X[8] == 1
prob += X[9] == 1
prob += X[10] == 1


#remeber index!!!

prob.solve()

#  format output
print(' ')
print("Status:",LpStatus[prob.status])
print(' ')
print("Objective: ",value(prob.objective))
print(' ')

for v in prob.variables():
    subV = v.name.split('_')
    
    if subV[0] == "X" and v.varValue == 1: print('p-Median Node: ', subV[1])

result = []   
'''print(' ')
for v in prob.variables():
    subV = v.name.split('_')
    if subV[0] == "Y" and v.varValue == 1: print(subV[1], ' is connected to', subV[2])'''

print(' ')
for v in prob.variables():
    subV = v.name.split('_')
    if subV[0] == "Y" and v.varValue == 1: 
    	result.append((subV[1], ' is connected to', subV[2]))
print(result)

df = pd.DataFrame(np.array(result))
print (df)
df.to_csv('/Users/Ramzi/Dropbox/EdgeListP-medianCode/EdgelistwithNoWeightsTesla.csv', sep=',')



# print out elapsed time    
print("Processing time took:",time.time()-t1)






