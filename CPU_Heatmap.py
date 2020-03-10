import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

numCPU = 8

def plotHeatmap(fileName):
    numInstances = 0
    matCPU = []
    for CPU in range(numCPU):
        matCPU.append([])
    
    with open(fileName, "r") as csvFile:
        reader = csv.reader(csvFile)
        currCPU = 0
        for row in reader:
            #print(row)
            if(row[0]=='Average:'):
                break
            if(row[2]=='CPU'):
                currCPU = 0
                numInstances+=1
                continue
            #print(currCPU)
            matCPU[currCPU].append(100.0-float(row[8]))
            currCPU+=1
                    
        npCPU = np.array(matCPU)
        npCPU.reshape(numCPU, numInstances)
        
        
        ax = sns.heatmap(npCPU, center=50)
        return ax

ax = plotHeatmap("SAR_CPU.csv")
plt.show()
