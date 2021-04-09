import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    allData = list(reader)
# removing the list of titles using pop
allData.pop(0)

weight_arr=[]
for i in range(len(allData)):
    n_num = allData[i][1]
    weight_arr.append(n_num)

num = len(weight_arr)
weight_arr.sort()

if num % 2 == 0:
    median1 = float(heightArr[n//2])

	median2 = float(heightArr[n//2 - 1])

	median = (median1 + median2)/2
else:
	median = heightArr[n//2]

print("median is:"+ str(median))