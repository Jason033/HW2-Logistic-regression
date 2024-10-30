# HW2-Logistic-regression
# prompt
請使用Logistic regression來解決Titanic資料集的問題，以下是資料的解釋
(1) train.csv 
train.csv contains the details of a subset of the passengers on board (891 passengers, to be exact -- where each passenger gets a different row in the table). To investigate this data, click on the name of the file on the left of the screen. Once you've done this, you can view all of the data in the window.The values in the second column ("Survived") can be used to determine whether each passenger survived or not:

if it's a "1", the passenger survived.
if it's a "0", the passenger died.
this format of train data
PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
1	0	3	Braund, Mr. Owen Harris	male	22	1	0	A/5 21171	7.25		S
2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Thayer)	female	38	1	0	PC 17599	71.2833	C85	C

(2) test.csv
Using the patterns you find in train.csv, you have to predict whether the other 418 passengers on board (in test.csv) survived.

Click on test.csv (on the left of the screen) to examine its contents. Note that test.csv does not have a "Survived" column - this information is hidden from you, and how well you do at predicting these hidden values will determine how highly you score in the competition!
this is format of test data
PassengerId	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
892	3	Kelly, Mr. James	male	34.5	0	0	330911	7.8292		Q
893	3	Wilkes, Mrs. James (Ellen Needs)	female	47	1	0	363272	7		S


The data location is in the same file as the code.
please follow CRISP-DM 框架 to solve problem，and deploy code on streamlit
  ，and use confusion matrix to evaluate the performance and show accuracy

# chagpt answer
![image](https://github.com/user-attachments/assets/fb8bb488-c9cf-4171-9876-9f590ae868c1)
![image](https://github.com/user-attachments/assets/1145f2fe-8d79-4e53-b6f9-2762515f5f4a)
![image](https://github.com/user-attachments/assets/927d44fb-ca1c-41d0-809c-480daf2e6614)
![image](https://github.com/user-attachments/assets/3cdb7480-6be3-47e8-a43c-a8557b947061)
![image](https://github.com/user-attachments/assets/65f882e3-0fff-40a0-9f85-168fbe9307c5)
![image](https://github.com/user-attachments/assets/ead89a31-3c8f-4d20-903c-2150c5730af3)

# result
![image](https://github.com/user-attachments/assets/d68eb7fd-5dce-4b61-b1aa-d3b3c3171d02)
![image](https://github.com/user-attachments/assets/eb86d704-f3e0-4a62-a6b0-28ef8fb93c59)

# kaggle
![image](https://github.com/user-attachments/assets/db1e48c1-5205-49e8-8c38-69013ad7f461)




