#-------------------------------------------------------------------------
# AUTHOR: Vincent Verdugo
# FILENAME: naive_bayes.py
# SPECIFICATION: Outputs the  classification of each test instance if the confidence is >= 0.75
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hour, 10 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data
db = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for index, row in enumerate(reader):
        if index > 0:
            db.append(row)

X = []
Y = []

#transform the original training features to numbers and add to the 2D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
for instance in db:
    replacement = []
    for index, value in enumerate(instance):
        if index == 1:
            replacement.append(1 if value == 'Sunny' else 2 if value == 'Overcast' else 3)
        elif index == 2:
            replacement.append(1 if value == 'Hot' else 2 if value == 'Mild' else 3)
        elif index == 3:
            replacement.append(1 if value == 'High' else 2)
        elif index == 4:
            replacement.append(1 if value == 'Weak' else 2)
    X.append(replacement)


#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
for instance in db:
    Y.append(1 if instance[5] == 'Yes' else 2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
test = []
XTest = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for index, row in enumerate(reader):
        if index > 0:
            test.append(row)
for instance in test:
    replacement = []
    for index, value in enumerate(instance):
        if index == 1:
            replacement.append(1 if value == 'Sunny' else 2 if value == 'Overcast' else 3)
        elif index == 2:
            replacement.append(1 if value == 'Hot' else 2 if value == 'Mild' else 3)
        elif index == 3:
            replacement.append(1 if value == 'High' else 2)
        elif index == 4:
            replacement.append(1 if value == 'Weak' else 2)
    XTest.append(replacement)

#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
prediction = clf.predict_proba(XTest)
probabilities = prediction.tolist()
print(probabilities)

for index, instance in enumerate(test):
    if prediction[index][0] >= 0.75:
        print (instance[0].ljust(15) + instance[1].ljust(15) + instance[2].ljust(15) + instance[3].ljust(15) + instance[4].ljust(15) + "Yes".ljust(15) + str(probabilities[index][0]).ljust(15))
    elif prediction[index][1] >= 0.75:
        print (instance[0].ljust(15) + instance[1].ljust(15) + instance[2].ljust(15) + instance[3].ljust(15) + instance[4].ljust(15) + "No".ljust(15) + str(probabilities[index][1]).ljust(15))
    else:
        pass