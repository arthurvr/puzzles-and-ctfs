#These are the imports that we need for our Neural Network
#Numpy is a powerful array and matrix library used to format our data
import numpy as np
#Pandas is a machine learning library that also allows for reading and formatting data structures
import pandas as pd
#This will be used to split our data
from sklearn.model_selection import train_test_split
#This is used to normalize our data
from sklearn.preprocessing import StandardScaler
#This is used to encode our text data to integers
from sklearn.preprocessing import LabelEncoder
#This is our Multi-Layer Perceptron Neural Network
from sklearn.neural_network import MLPClassifier

#These are the colour labels that we will convert to int
colours = ["Red", "Blue", "Green", "Yellow", "Pink", "Purple", "Orange"]


#Read the training and testing data files
training_data = pd.read_csv("training_dataset.csv")
training_data.head()

testing_data = pd.read_csv("testing_dataset.csv")
testing_data.head()

#The Neural Network cannot take Strings as input, therefore we will encode the strings as integers
encoder = LabelEncoder()
encoder.fit(training_data["Colour Scheme"])
training_data["Colour Scheme"] = encoder.transform(training_data["Colour Scheme"])
testing_data["Colour Scheme"] = encoder.transform(testing_data["Colour Scheme"])



#Read our training data from the CSV file.
#First we read the data we will train on
X = np.asanyarray(training_data[['Height','Width','Length','Colour Scheme','Maker Elf ID','Checker Elf ID']])
#Now we read the labels of our training data
y = np.asanyarray(training_data['Defective'].astype('int'))

#Read our testing data
test_X = np.asanyarray(testing_data[['Height','Width','Length','Colour Scheme','Maker Elf ID','Checker Elf ID']])

train_X, validate_X, train_y, validate_y = train_test_split(X, y, test_size=0.2)

#Now we need to split our training dataset here

print ("Sample of our data:")
print("Features:\n{}\nDefective?:\n{}".format(train_X[:3], train_y[:3]))

scaler = StandardScaler()
scaler.fit(train_X)
 
train_X = scaler.transform(train_X)
validate_X = scaler.transform(validate_X)
test_X = scaler.transform(test_X)

#Now we normalize our dataset

print ("Sampe of our data after normalization:")
print("Features:\n{}\nDefective?:\n{}".format(train_X[:3], train_y[:3]))


clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(15, 2), max_iter=10000)

print ("Starting to training our Neural Network")



clf.fit(train_X, train_y)

y_predicted = clf.predict(validate_X)


#This function tests how well your Neural Network performs with the validation dataset
count_correct = 0
count_incorrect = 0
for x in range(len(y_predicted)):

    if (y_predicted[x] == validate_y[x]):
        count_correct += 1
    else:
        count_incorrect += 1

print ("Training has been completed, validating neural network now....")
print ("Total Correct:\t\t" + str(count_correct))
print ("Total Incorrect:\t" + str(count_incorrect))

accuracy =  ((count_correct * 1.0) / (1.0 * (count_correct + count_incorrect)))

print ("Network Accuracy:\t" + str(accuracy * 100) + "%")

print ("Now we will predict the testing dataset for which we don't have the answers for...")


y_test_predictions = clf.predict(test_X)




#This function will save your predictions to a textfile that can be uploaded for scoring
print ("Saving predictions to a file")

output = open("predictions.txt", 'w')

for value in y_test_predictions:
    output.write(str(value) + "\n")

print ("Predictions are saved, this file can now be uploaded to verify your Neural Network")
output.close()




