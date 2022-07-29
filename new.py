# from xml.etree.ElementInclude import include
# import robot
# logFile = open('mylog.txt', 'w')
# robot.run("traffic01.robot",stdout=logFile)
import os


f=open('reference.robot','r')
content=[i for i in f]

all_files=[]

for i in range(10):
    file_name='dynamic/'+'traffic0'+str(i)+'.robot'
    all_files.append(file_name)
    f1=open((file_name),'w+')
    ind=-1
    for j in range(len(content)):
        if('@{users}' in content[j]):
            ind=j
            break
    to="@{users}["+str(i)+':'+str((i+1))+']'
    content1=[i.replace("@{users}",to) for i in content]
    for line in content1:
        f1.write(line)


            
for i in all_files:
    os.remove(i)


    


