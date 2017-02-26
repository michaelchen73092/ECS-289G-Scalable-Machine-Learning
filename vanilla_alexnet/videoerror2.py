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
probframe = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #for count frame rate
framecorr = 0 #count correct frame number
totalframe = 0 #count total frame number
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
           probframe[j] = float(probValue) #store frame probability
       indexframe=np.argmax(probframe)
       totalframe = totalframe + 1
       if int(videoClass) == int(indexframe):
          framecorr =framecorr + 1
       probframe = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #for count frame rate
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
             probframe[j] = float(probValue) #store frame probability
         indexframe=np.argmax(probframe)
         totalframe = totalframe + 1
         if int(videoClass) == int(indexframe):
            framecorr =framecorr + 1
         probframe = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #for count frame rate

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
print '#######Video Accuracy Rate #######'
print 'Correct rate:' + str(float(float(correct)*100/float(total))) + '%'
print 'total video number:' + str(total)
print 'total correct video number:' + str(correct)
print '##################################'
#print ouf for frame rate
print '#######Frame Accuracy Rate #######'
print 'Number of correct frames:' + str(framecorr)
print 'Number of total frames:' +str(totalframe)
print 'Frame Accuracy Rate:' + str(float(float(framecorr)*100/float(totalframe))) + '%'
print '##################################'
print '     ' + 'correct\t' + 'total\t' + 'precision\t'
for j in range(0, 10):
    if totalList[j] == 0:
       precision = 'NA'
    else:
         precision = correctList[j]*100/totalList[j]
    print 'Class'+str(j)+':'+str(correctList[j])+'\t'+str(totalList[j])+'\t'+  \
    str(precision)+'%\t'
print '##################################'

#Author: Wei-Chih Chen 
#Time: Nov 28 2015
