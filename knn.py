#-------------------------------------------------------------------------
# AUTHOR: Vincent Verdugo
# FILENAME: knn.py
# SPECIFICATION: This program outputs the LOO-CV error rate for 1NN (nearest neighbors)
# FOR: CS 4210 - Assignment #2
# TIME SPENT: 35 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)

errors = 0
#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):
    X = []
    Y = []
    testSample = []
    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    for index, row in enumerate(db):
        if index == i:
            pass
        else:
            X.append([float(row[0]), float(row[1])])

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    for index, row in enumerate(db):
        if index == i:
            pass
        else:
            Y.append(float(1) if row[2] == '+' else float(2))
    #store the test sample of this iteration in the vector testSample
    testSample = [float(db[i][0]),float(db[i][1])]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    prediction = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    if (prediction == 1.0 and db[i][2] == '+') or (prediction == 2.0 and db[i][2] == '-'):
        pass
    else:
        errors += 1

#print the error rate
print("Error rate for 1NN:", errors / len(db))
