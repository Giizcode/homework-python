import pandas as pd
df = pd.read_csv('C:\\Users\\kamal\\OneDrive\\Desktop\\stackoverflow_qa.csv')
df.head(2)
df['creationdate'] = pd.to_datetime(df['creationdate'])
before_2014 = df[df['creationdate'] < '2014-01-01']
score_gt_50 = df[df['score']>50]
score_between_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]
answer_Scott_Boston = df[df ['ans_name']== 'Scott Boston']
users = ['Scott Boston', 'unutbu', 'Warren Weckesser', 'DSM', 'jezrael']
answered_by_users = df[df['ans_name'].isin(users)]
filtered = df [
   (df['creationdate']>= '2014-03-01') &
   (df['creationdate']<= '2014-10-31') &           
   (df['ans_name']== 'unutbu') &
   (df ['score']< 5)
];
score_or_views = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) |
    (df['viewcount'] > 10000)
];
not_scott = df[df['ans_name'] != 'Scott Boston']
####################################################

import pandas as pd 
df = pd.read_csv("C:\\Users\\kamal\\Downloads\\titanic.csv")
df.head(3)
filtered = df[
    (df['Pclass'] == 1) &
    (df['Age'] >= 20) & (df['Age'] <= 30) &
    (df['Sex'] == 'female')
];
paid_more_than_100 = df[df['Fare'] > 100]
survived_alone = df[(df['Survived'] == 1) & (df['SibSp'] == 0) & (df['Parch'] == 0)]
paid_more_than_50 = df[(df['Fare'] > 100) & (df['Embarked'] == 'C')]
relation = df[(df['SibSp'] > 0) & (df['Parch'] > 0)]
young_no_survive = df[(df['Age'] <= 15) & (df['Survived'] == 0)]
cabins_and_high_fare = df[(df['Cabin'].notna()) & (df['Fare'] > 200)]
odd_passenger_ids = df[df['PassengerId'] % 2 != 0]
unique_ticket_passengers = df.drop_duplicates(subset='Ticket', keep=False)
miss_class_1 = df[(df['Name'].str.contains('Miss')) & (df['Pclass'] == 1)]
