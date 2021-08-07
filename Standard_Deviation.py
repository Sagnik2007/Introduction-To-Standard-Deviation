import csv
import math

with open('C:/Users/milindo/Desktop/All Desktop Files Dad/WhiteHat Jr/Project 105/data.csv', newline='') as f:
    readedData = csv.reader(f)
    File_Data = list(readedData)

Total_Entries = len(File_Data[0])

New_Data = []

for i in File_Data[0]:
    New_Data.append(int(i))

SumOfEntries = sum(New_Data)

Mean = SumOfEntries / Total_Entries
print("Mean (Average) is -> "+str(Mean))

List = []

for i in New_Data:
    Step1 = Mean-float(i)
    List.append(Step1*Step1)

Sum = sum(List)
Divide = Sum/Total_Entries
Standard_Deviation = math.sqrt(Divide)

print("Standard Deviation is -> ", Standard_Deviation)