import numpy as np
import xlrd
import os 
from toolbox_02450.similarity import similarity
import matplotlib.pylab as plt


print(os.getcwd())
path= "C:/Users/nico/Desktop/vita_di_nico/unitn/Erasmus_DTU_2023/Courses/02450-Introduction_Machine_Learning_DataMining/assigements/assignment_1/assignment_1/dataset.xls"
if os.path.exists(path):
# Load xls sheet with data
    doc = xlrd.open_workbook(path).sheet_by_index(0)
else : print("path non valida")

#Converts Present and Absent into numbers.
def toNumber(x)-> int:
    if x == "Present":
        return 1
    else:
        return 0

# Extract attribute names (1st row, column 4 to 12)
attributeNames = doc.row_values(0, 1, 11)

X = np.zeros((462,10))



for i in range(1,11):
     if(i == 5):
        famHist = np.array( doc.col_values(i, 1,463) )
        for i in range(len(famHist)):
            famHist[i] = toNumber(famHist[i])
     else: 
         X[:,i-1] =  np.array(doc.col_values(i,1,463)).T
         
X[:, 4] = famHist


# Delete the last column, CHD 
X_no_CHD = np.delete(X, 9, 1)

# Basic statistics 

# min, max, mean, std, 
basic_stats = np.ones((10,4))

for i in range(len(basic_stats)):
    for j in range(len(basic_stats[0])):
        if j == 0:    
            basic_stats[i][j] = np.min(X[:,i])
        if j == 1:
            basic_stats[i][j] = np.max(X[:,i])
        if j == 2:    
             basic_stats[i][j] = np.mean(X[:,i])
        if j == 3:
             basic_stats[i][j] = np.std(X[:,i])
            
stat = np.array(["min", "max","mean","std"])
for i in range(len(basic_stats)):
    print("<<<",attributeNames[i],">>>")
    for j in range(len(basic_stats[0])):
        if j == 0:    
           print("    min: ",  basic_stats[i][j])
        if j == 1:    
           print("    max: ",  basic_stats[i][j])
        if j == 2:    
              print("    mean: ",  basic_stats[i][j])
        if j == 3:    
              print("    std: ",  basic_stats[i][j])


famH_ = np.sum(X[:,4])
print("Nunmber of patients with famili history positive to CHD :",famH_ , " --- ",round(famH_ /len(X)*100,2),"%")

chd_ = np.sum(X[:,9])
print("Nunmber of patients positive to CHD :",chd_," --- ",round(chd_ /len(X)*100,2),"%")
c_famhist_chd = X[:,4] + X[:,9]

c_famhist_chd[c_famhist_chd == 1] = 0
c_famhist_chd= np.sum(c_famhist_chd)/2
print("Number of patients with both CHD and famhist: ", c_famhist_chd, " --- ", round(c_famhist_chd/len(X)*100,2),"%")






