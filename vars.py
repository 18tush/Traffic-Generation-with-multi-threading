# nodes=['SMCA','SME','Admin UI','SMSM','Sandbox']
from collections import UserString
from random import shuffle
import pandas as pd


# Don't change below parameters in nodes
nodes=['CA','ZEN','Admin UI','Nanolog','Sandbox']   

# Configure nodes2 values for customized names
nodes2=['SMCA','SME','Admin UI','SMSM','Sandbox']
dns='8.8.8.8'
counter=0

# Configure management ip's below
mips=['3.1.1.9','3.1.1.10','3.1.1.11','3.1.1.12','3.1.1.13']

# Configure service ip's below
zensip= '3.1.1.21'
nanologsip= '3.1.1.22'





f= open('url_all.txt.medium','r')
websites=[]
for i in f:
    websites.append(i)
shuffle(websites)
# websites=websites[:5]
a=''

websites=[i.rstrip('\n') for i in websites]
shuffle(websites)
# print(websites)
# websites=['http://www.aibai.cn/','http://www.beautyphoto.info/','http://www.loveadvice.info/','http://www.adultfilmclassics.com/']

num_links=len(websites)

users=[]
f= open('users.txt')
for i in f:
    x,y= i.split()
    users.append([x,y])
# users=users[1:4]
# df = pd.read_csv('users.csv')
# import csv
# with open(r"users.csv", 'rb') as f:
#     reader = csv.reader(f)
#     linenumber = 1
#     try:
#         for row in reader:
#             linenumber += 1
#     except Exception as e:
#         print (("Error line %d: %s %s" % (linenumber, str(type(e)), e.message)))
# print(df)

num_users=len(users)
per_user= num_links//num_users

if(per_user>10000):
    websites=websites[:num_users*10000]

# users=users[1:2]
# shuffle(users)

num_users=len(users)
num_links=len(websites)
per_user= num_links//num_users

print(num_links)
print(users)
print(per_user)

# a=[i[0] for i in users]
# print(len(a))
# print(len(set(a)))
# b=list(set(a))
# d=dict()
# for i in a:
#     if(i in d):
#         d[i]+=1
#     else:
#         d[i]=1
# c=[i for i in d if d[i]>1]
# print(c)
# print(len(set(users)))

print(websites)
index=0


batch_users=[]

