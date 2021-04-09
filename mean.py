import csv
with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    allValues = list(reader)

allValues.pop(0)
#print(allValues)

# sorting data  to get the height of people.
weight_arr=[]
for i in range(len(allValues)):
	height = allValues[i][1]
	weight_arr.append(float(weight))

#print(heightArray)
#getting the mean
n = len(weight_arr)
sumAllValues = 0
for weight in weight_arr:
    sumAllValues += weight

mean = sumAllValues / n
print("Mean / Average is: " + str(mean))
