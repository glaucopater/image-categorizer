import requests
import io 
from os import listdir
from os.path import isfile, join

api_key = 'acc_3d59c7c967cc508'
api_secret = '24e68357cec839604ea30a2ee5537271'
#image_path = 'D:\XiaomiRedmi10032019\WhatsApp\Media\WhatsApp Images\IMG-20181206-WA0010.jpg'
image_path = 'D:\XiaomiRedmi10032019\WhatsApp\Media\WhatsApp Images\IMG-20190125-WA0009.jpg'
#D:\XiaomiRedmi10032019\WhatsApp\Media\WhatsApp Images

def analyze(image_path):
    response = requests.post('https://api.imagga.com/v2/categories/nsfw_beta',
    auth=(api_key, api_secret),
    files={'image': open(image_path, 'rb')})
    data = {}
    data["filename"] = image_path
    data["result"] = response.json()
    return data

def save_data(json):
    f = open("nsfw_results.txt", "a+")
    f.write(str(json))


mypath = 'D:\XiaomiRedmi10032019\WhatsApp\Media\WhatsApp Images'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print (onlyfiles)


for im in onlyfiles:
    data = analyze(mypath + '\\' + im)   
    save_data(data)
    #print (analyze(image_path))