#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import datetime
import io 
from os import listdir
from os.path import isfile, join


def save_data(data):
    f = open("moderation_results.csv", "a+")
    f.write(str(data))

def analyze_file(imageFile):
    client=boto3.client('rekognition')

    with open(imageFile, 'rb') as image:
        response = client.detect_moderation_labels(Image={'Bytes': image.read()})

    print('Detected labels for ' + imageFile)    
    print(response['ModerationLabels'])

    #save_data("ImageFile,Name,Confidence,ParentName,timestamp")
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
        timestamp = str(datetime.datetime.utcnow())
        save_data(imageFile + "," + label['Name'] + "," + str(label['Confidence']) + "," + label['ParentName'] + "," + timestamp + "\n")

if __name__ == "__main__":    
    #imageFile='images/IMG-20161218-WA0007.jpg'
    mypath = 'images/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
    for imageFile in onlyfiles:
        analyze_file(mypath + '\\' + imageFile)