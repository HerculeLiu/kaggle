''' import libraries '''
import csv
import matplotlib.pyplot as plt
import pandas as pd
import openai
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.tree import DecisionTreeClassifier
from pyresparser import ResumeParser
from OpenAITextGenerator import get_response

''' Read csv '''
Resume_raw = pd.read_csv("inputs/archive/Resume/Resume.csv")

print(Resume_raw.info())
# print("?????\n?????")

with pd.option_context('display.max_columns', None):
    print(Resume_raw.head(5))

print("[Category] has value : ")
print(Resume_raw['Category'].unique())

dict = {}

for Profession_name in Resume_raw['Category'].unique():
    dict[Profession_name] = Resume_raw[Resume_raw['Category'] == Profession_name]

print("dict size : ", dict.__len__())

for k in dict.keys():
    print("Profession [", k , "] has : ", dict[k].shape[0])
    print(dict[k].head(5))


# 示例输入问题和文本
question = "this is a HR resume, give me some key word of this people"
text = dict['HR'].iloc[5]['Resume_str']

# 获取回答
answer = get_response(question, text)

# 输出摘要结果
print("摘要：\n", answer)



'''  '''
parser = ResumeParser()
data = parser.parse('inputs/archive/data/data/HR/11592605.pdf').get_extracted_data()

print(
    "name = ",data['name']
    ,"email = ",data['email']
    ,"phone = ",data['mobile_number']
    ,"education = ",data['education']
    ,"experience = ",data['experience']
    ,"skills = ",data['skills']
)



