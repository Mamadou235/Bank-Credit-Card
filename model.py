# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('Dataset.csv')

# dataset['experience'].fillna(0, inplace=True)

# dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

# X = dataset.iloc[:, :3]

#Converting words to integer values
# def convert_to_int(word):
#     word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
#                 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
#     return word_dict[word]

# X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

# y = dataset.iloc[:, -1]

X = df[['Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1','Total_Trans_Amt', 'Total_Trans_Ct','Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']]
y = df['Attrition_Flag'].map({'Existing Customer':0,'Attrited Customer':1})



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import RandomForestClassifier
rand = RandomForestClassifier()

#Fitting model with trainig data
rand.fit(X, y)

# Saving model to disk
pickle.dump(rand, open('data_model','wb'))

# Loading model to compare the results
data_model = pickle.load(open('data_model','rb'))
print(data_model.predict([[1, 2, 3, 4, 5, 6, 7]]))