

''' import libraries '''
import csv
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.tree import DecisionTreeClassifier

''' Read csv '''
train_X = pd.read_csv("inputs/titanic/train.csv")
test_X = pd.read_csv("inputs/titanic/test.csv")

train_Y = train_X['Survived']

''' data info '''
print(train_X.shape)

print(train_X.info())

with pd.option_context('display.max_columns', None):
    print(train_X.head(5))

print(test_X.info())


''' To check missing values '''
missing_values = train_X.isna().sum()/train_X.shape[0]
print(missing_values)

''' Because the Cabin is missing a lot, I discarded it '''
train_X.drop('Cabin', axis = 1, inplace=True)
test_X.drop('Cabin', axis = 1, inplace=True)

''' Age and Fare has 19.87% missing values '''
train_X['Age'] = train_X['Age'].interpolate(method='linear')
test_X['Age'] = test_X['Age'].interpolate(method='linear')
test_X['Fare'] = test_X['Fare'].interpolate(method='linear')
# train_X=train_X.fillna(train_X.mean())
# test_X=test_X.fillna(test_X.mean())

''' set the index by PassengerId '''
train_X = train_X.set_index('PassengerId')
test_X = test_X.set_index('PassengerId')

''' replace gender to number '''
def replaceGender(gender):
    if gender == 'male':
        return 1
    else:
        return 0

train_X['Sex'] = train_X['Sex'].apply(replaceGender)
test_X['Sex'] = test_X['Sex'].apply(replaceGender)

''' remove 'Survived' from train_X '''
train_X.drop('Survived', axis = 1, inplace=True)

''' remove some unimportant columns '''
train_X.drop('Name', axis = 1, inplace=True)
test_X.drop('Name', axis = 1, inplace=True)

train_X.drop('Embarked', axis = 1, inplace=True)
test_X.drop('Embarked', axis = 1, inplace=True)

train_X.drop('Ticket', axis = 1, inplace=True)
test_X.drop('Ticket', axis = 1, inplace=True)


''' replace SibSp and Parch '''
train_X.drop('SibSp', axis = 1, inplace=True)
test_X.drop('SibSp', axis = 1, inplace=True)

train_X.drop('Parch', axis = 1, inplace=True)
test_X.drop('Parch', axis = 1, inplace=True)

''' replace Pclass and Age '''
train_X.drop('Pclass', axis = 1, inplace=True)
test_X.drop('Pclass', axis = 1, inplace=True)

with pd.option_context('display.max_columns', None):
    print(train_X.head(5))

with pd.option_context('display.max_columns', None):
    print(test_X.head(5))

''' train the model '''
tree = DecisionTreeClassifier(max_depth=3)
tree.fit(train_X, train_Y)


''' predict '''
test_Y = tree.predict(test_X)

''' save it to result '''
passenger_id = []
for pid in test_X.index:
    passenger_id.append(pid)

df = pd.DataFrame({'PassengerId': passenger_id, 'Survived': test_Y})

# 将DataFrame保存为CSV文件
df.to_csv('outputs/result.csv', index=False)


