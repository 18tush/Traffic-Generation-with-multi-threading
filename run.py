import pabot
from subprocess import call
from collections import UserString
from random import shuffle
import pandas as pd
import os
import time

websites=[]
f=open('url_all.txt.medium','r')
for i in f:
    websites.append(i)


# call(["python", "your_file.py"])
logFile = open('mylog.txt', 'w') 
# pabotlib.run("trafficgen",stdout=logFile)
start = time.time()



f=open('reference.robot','r')
content=[i for i in f]

all_files=[]

batch_size=10
num_of_batches=10


for k in range(num_of_batches):
    all_files=[]
    for i in range(batch_size+1):
        file_name='dynamic/'+'traffic0'+str(i)+'.robot'
        all_files.append(file_name)
        f1=open((file_name),'w+')
        ind=-1
        # for j in range(len(content)):
        #     if('@{users}' in content[j]):
        #         ind=j
        #         break
        # print(i)
        to="@{users}["+str(k*batch_size+i)+':'+str(k*batch_size+1+i)+']'
        content1=[i.replace("@{users}",to) for i in content]
        x=(k*batch_size+1)*(len(websites)//(batch_size*num_of_batches))
        web_to="${websites}["+str(x)+':'+str(x+len(websites)//(batch_size*num_of_batches))+']'
        content1=[i.replace("${websites}",web_to) for i in content1]
        for line in content1:
            f1.write(line)
    # time.sleep(1)
    call(["pabot", "dynamic"])
            
    for i in all_files:
        os.remove(i)

end= time.time()

print('Time taken:', end-start)