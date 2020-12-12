import csv
import statistics as st
import math
def loadCsv(filename):
    lines = csv.reader(open(filename, "r"));
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

def calprob(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev*stdev)) * exponent

dataset=loadCsv('diabetes.csv')
size=0.5 
train=[] 
test=[] 

for i in range(int(len(dataset)*size)):
	test.append(dataset[i])
for i in range(int(len(dataset)*size+1),len(dataset)):
	train.append(dataset[i])
print('The lenth of the training set',len(train))
print('The length of the testing set',len(test))

classes=[]
for i in dataset:
	if(i[-1] not in classes):
		classes.append(i[-1]) 
classdict={} 
classdict1={} 
classprob={}

for i in classes:
	classdict[i]=[]
	classdict1[i]=[]
	classprob[i]=1


for i in classes:
	for row in train:
		if row[-1]==i:
			classdict[i].append(row[:-1])


for classval,datt in classdict.items():
	for col in zip(*datt):
		classdict1[classval].append((st.mean(col),st.stdev(col)))


count=0 
for row in test:
	for i in classes:
		classprob[i]=1
	for classval,datt in classdict1.items():
		for i in range(len(row[:-1])):
			mean,std=datt[i]
			x=row[i]
			classprob[classval]*=calprob(x,mean,std) 
	print(classprob," for row ",row)

	mini=0
	cl=0
	for c,d in classprob.items():
		if d>mini:
			mini=d
			cl=c
	
	if row[-1]==cl:
		count+=1

acc=count/len(test)
print("Accuracy of classifier ",acc)










