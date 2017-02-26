import sys
import numpy as np
import re

#testSrc = open('/home/SSD3/ycjlin-data/20150928caffe/examples/vanilla_alexnet/list/test000.lst', 'r')
#AftModel = open('/home/SSD3/ycjlin-data/20150928caffe/examples/vanilla_alexnet/mdb_reader2.txt', 'r')
testSrc = open('./list/test.lst', 'r')
AftModel = open('./mdb_reader2.txt', 'r')

#variables initiate
total = 0 #count total video number
correct = 0 #count correct prediction after alexNet model comparing with test000.lst
correctList = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) #correct # for each class
totalList = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) #total # for each class
prob = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #count total prob. in one video
f1=open('./videoerror.log','w+') #initiate log file
########################
videoName = 'null'
videoNameComp = 'null'
#readline from test000.lst
for lineTestSrc in testSrc.readlines():
    #get lines from test000.lst
    if videoName != 'null': #store previous class
       videoNameComp = videoName
       videoClassComp= videoClass 
    videoName = re.search('/(.+?/)', lineTestSrc) #get video name
    videoClass= lineTestSrc[len(lineTestSrc)-2] #get video class [Note] last position is \n
    #compare with AftModel
    if videoNameComp == 'null' or videoName.group(0) == videoNameComp.group(0):
       AftModel.readline()
       # calculate 10 probability in one frame
       for j in range(0, 10):
           probRead=AftModel.readline()
           probValue = probRead.partition('[')[-1].rpartition(']')[0] #get float in AftModel
           prob[j]= prob[j] + float(probValue) #do not divide # of frames in a video 
    else:
         index=np.argmax(prob) #return index of max value 
         totalList[int(videoClassComp)] =totalList[int(videoClassComp)] + 1 #calculate total # of videos
         if int(videoClassComp) == int(index):
            #calculate total # of correct videos
            correctList[int(videoClassComp)] = correctList[int(videoClassComp)]+1  
         else:
              f1.write('Class ' + str(videoClassComp) + ':' + str(index) + "\t" + str(videoNameComp.group(0)) + '\n')
         #reset prob and count
         prob = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) 
         # calculate 10 probability in one frame
         AftModel.readline()
         for j in range(0, 10):
             probRead=AftModel.readline()
             probValue = probRead.partition('[')[-1].rpartition(']')[0] #get float in AftModel
             prob[j]= prob[j] + float(probValue)

#Last frame without calculate in for loop
index=np.argmax(prob) #return index of max value 
totalList[int(videoClassComp)] =totalList[int(videoClassComp)] + 1 #calculate total # of videos
if int(videoClassComp) == int(index):
   correctList[int(videoClassComp)] = correctList[int(videoClassComp)]+1
else:
    f1.write('Class ' + str(videoClassComp) + ':' + str(index) + "\t" + str(videoNameComp.group(0)) + '\n')
f1.close()
total=np.sum(totalList)
correct=np.sum(correctList)
#print out information
print 'Correct rate:' + str(correct*100/total) + '%'
print 'total video number:' + str(total)
print 'total correct video number' + str(correct)
print '     ' + 'correct\t' + 'total\t' + 'precision\t'
for j in range(0, 10):
    if totalList[j] == 0:
       precision = 'NA'
    else:
         precision = correctList[j]*100/totalList[j]
    print 'Class'+str(j)+':'+str(correctList[j])+'\t'+str(totalList[j])+'\t'+  \
    str(precision)+'%\t'
 
