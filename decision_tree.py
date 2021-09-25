#-------------------------------------------------------------------------
# AUTHOR: Vincent Verdugo
# FILENAME: decision_tree.py
# SPECIFICATION: This program creates, trains, and tests the performance
# of 3 different datasets on the same training set. The lowest accuracy of
# each dataset is printed
# FOR: CS 4210 - Assignment #2
# TIME SPENT: 1.5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for index, ds in enumerate(dataSets):
    lowestAccuracy = 0
    print("Dataset", index + 1)

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append(row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # for each instance in the current dataset
    for instance in dbTraining:
        # create a list, then run through each instance
        replacement = []
        for index, value in enumerate(instance):
            # replace each value with an arbitary number
            if index == 0:
                replacement.append(1 if value == 'Young' else 2 if value == 'Prepresbyopic' else 3)
            elif index == 1:
                replacement.append(1 if value == 'Myope' else 2)
            elif index == 2:
                replacement.append(1 if value == 'No' else 2)
            elif index == 3:
                replacement.append(1 if value == 'Reduced' else 2)
        # append the instance replaced by integer values
        X.append(replacement)
    # now X will be the same as the current dataset (ds), but each value for each instance is replaced by an arbitrary integer

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    for instance in dbTraining:
        Y.append(1 if instance[4] == 'Yes' else 2)

    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       dbTest = []
       XTest = []

       with open('contact_lens_test.csv', 'r') as csvfile:
           reader = csv.reader(csvfile)
           for index, row in enumerate(reader):
               if index > 0:
                   dbTest.append(row)

       for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
           #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           replacement = []
           for index, value in enumerate(data):
               if index == 0:
                   replacement.append(1 if value == 'Young' else 2 if value == 'Prepresbyopic' else 3)
               elif index == 1:
                   replacement.append(1 if value == 'Myope' else 2) 
               elif index == 2:
                   replacement.append(1 if value == 'No' else 2) 
               elif index == 3:
                   replacement.append(1 if value == 'Reduced' else 2) 
           XTest.append(replacement)
       prediction = clf.predict(XTest)
       correctPredictions = 0
       for index, data in enumerate(dbTest):
           if (prediction[index] == 1 and data[4] == 'Yes') or (prediction[index] == 2 and data[4] == 'No'):
               correctPredictions += 1
       if i == 0:
           lowestAccuracy = correctPredictions / len(dbTest)
       if correctPredictions / len(dbTest) < lowestAccuracy:
           lowestAccuracy = correctPredictions / len(dbTest)
    print("Final accuracy:", lowestAccuracy)