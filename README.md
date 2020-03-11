# CPU Heatmap Generator
 
This repository uses the seaborn module in python to create a heatmap of each CPUs Utilization over a specified period of time.

## Requirements
A. Python3 Libraries
	
1. Matplotlib
2. Seaborn
3. Numpy

B. System Activity Report (SAR) tool on Linux

## Usage

```
./Parser.sh <CSV CPU List> <Timespan> 
./Parser.sh 0,1,2,3,4,5,6,7 10
```

The heatmap obtained will look something like this.

![](https://github.com/Kadle11/CPU_Heatmap/blob/master/HeatmapFig/HeatMap_1.png)

Here the X-axis is a plot of the timespan specified (10s) and the Y-axis corrosponds to the Number of Cores.
This heatmap indicates individual CPU utilization during every second of the workload.

To change the number of cores, open ```CPU_Heatmap.py``` and change the value of ```numCPU```

**_Example of a 1 minute workload on a 32-Core (Logical) machine_**

![](https://github.com/Kadle11/CPU_Heatmap/blob/master/HeatmapFig/16384_HeatMap.png)
