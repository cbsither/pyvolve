import re
import os
import sys
import numpy as np
pamlorder = list("ARNDCQEGHILKMFPSTWYV")
pyvolveorder = list("ACDEFGHIKLMNPQRSTVWY")
import pprint as pp
ZERO=1e-8
TOL=8

input_file = sys.argv[1]

with open(input_file, "r") as f:
    paml = f.readlines()

########## frequencies ##########
fraw = paml[-1].strip().strip(";").split(" ")
freq = []
for AA in pyvolveorder:
    freq.append( float( fraw [ pamlorder.index(AA) ] ) )

### RENORMALIZE TO MY TOLERANCE OF 1e-8
if ( abs(1. - np.sum(freq)) > ZERO ):
    freq = np.array(freq)
    freq /= np.sum(freq) 
    freq = list(freq)   

########## matrix #############
rates = np.zeros([20,20])
matrixraw = paml[:-2]

x = 0
for row in matrixraw:
    row_list = row.strip().split(" ")
    assert(len(row_list) == x+1), "\n BAD ROW"
    source = pamlorder[x+1]
    for i in range(len(row_list)):
        target = pamlorder[i]
        
        i_index = pyvolveorder.index(source)
        j_index = pyvolveorder.index(target)
        
        
        rate = float(row_list[i].strip())
        rates[i_index][j_index] = rate
        rates[j_index][i_index] = rate
        #print(source, target, i_index, j_index, rate)
        
    x+=1
    
final_rates = []
for row in rates:
    final_rates.append(list(row))

name = pamlfile.split(".paml")[0].lower()
print(name + "_freqs = " + str(freq))
print(name + "_matrix = " + str(final_rates))


print("\n")

    
    