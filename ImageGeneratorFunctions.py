## issues for image , weights right?, 
from PIL import Image 
from IPython.display import display 
import random
import json
import os
import requests
import typing as tp

from os import listdir
from os.path import isfile, join
from pathlib import Path
from os.path import join, dirname

#### Straing new project
def projectStart(_projectName, _projectTraits):
    '''
    Inputs project parameters and builds required files structure based on where this file is located.
    '''
    baseFiles = ['Images', 'Images(png)', 'Details', 'Metadata']
    files = baseFiles + _projectTraits
    
    parentDir = os.getcwd()
    path = os.path.join(parentDir, _projectName)
    os.mkdir(path)

    for directory in files:
        path = os.path.join(parentDir, _projectName, directory)
        os.mkdir(path)
    

def getProjectPath(_projectName): 
    '''
    Project name retuns the path of used directory
    '''
    parentDir = os.getcwd()
    path = os.path.join(parentDir, _projectName)
    
    return path


def weightTemplate(_projectName, _fileName, _projectTraits):
    '''
    Builds a text file in the details directory to choose and modify weights.
    A filename is used for different types of weightings. 
    '''
    data = []
    for trait in _projectTraits:
        path = os.path.join(getProjectPath(_projectName), trait)
        traits = [(f.split('.'))[0] for f in listdir(path)] 
        something = [{a:0} for a in traits]
        data.append({trait:something})
        
    saveWeights(_projectName, _fileName, data)
      
        
#### Creating Image Data
def createImageData(_projectTraits, _data):
    '''
    Creates the data for a single image to be constructed 
    '''
    newImage = {} #
    for trait in _projectTraits:
        newImage[trait] = random.choices((traitList(trait, _data)), (weightList(trait, _data)))[0]
  
    return(newImage)


def createImagesData(_projectName, _fileName, _projectTraits, _noOf):
    '''
    Creates a list of image data to construct mulipult images.
    Checks if all images are unique in the list, so there are no duplicates.
    '''
    images = []
    weightData = loadWeights(_projectName, _fileName)
    for image in range(1,_noOf + 1):
        unique = False
        while unique == False:
            imageData = createImageData(_projectTraits, weightData)
            if imageData in images:
                unique = False
            else:
                images.append(imageData)
                unique = True
        
    imageData = addTokenId(images)  
    saveImageData(_projectName, _fileName, imageData)
        
    return imageData


def traitList(_trait, _data):
    '''
    Builds a list of traits from the supplied data.
    '''
    traits = [d for a in _data for b in a if b == _trait for c in a[b] for d in c]
    
    return traits 
    
    
def weightList(_trait, _data):
    '''
    Builds a list of weights from the supplied data.
    '''
    weights = [c[d] for a in _data for b in a if b == _trait for c in a[b] for d in c]
        
    return weights
    

def checkWeights(_projectTraits, _data):
    '''
    Checks if all the weights equal 100
    '''
    for trait in _projectTraits:
        weights = weightList(trait, _data)
        total = sum(weights)
        if total != 100:
            print(trait, total)

            
def addTokenId(_allImages):
    '''
    Adds a token ID number to each image data in a list of multiplue image data  
    '''
    tokenId = 1
    for item in _allImages:
        item["tokenId"] = tokenId 
        tokenId = tokenId + 1
        
    return _allImages
        
        
#### Creating png Images, saves to images to Images(png)
def createImages(_projectName, _fileName, _projectTraits):
    '''
    Creates multipue images from date within images data and saves to Images(png)
    '''
    imagesData = loadImageData(_projectName, _fileName)
    for imageData in imagesData:
        createImage(_projectName, _projectTraits, imageData)

        
def createImage(_projectName, _projectTraits, _imageData):
    '''
    Creates a single image from the supplied data and saves it to Images(png)
    '''
    count = 0
    for i in _projectTraits:
        if count == 0:
            tempImage = Image.open(os.path.join(getProjectPath(_projectName), i, _imageData[i] + ".png")).convert('RGBA') 
        elif count != 0:
            tempLayer = Image.open(os.path.join(getProjectPath(_projectName), i, _imageData[i] + ".png")).convert('RGBA')
            tempImage = Image.alpha_composite(tempImage, tempLayer)         
        count = count + 1
                                   
    image = tempImage.convert('RGB')
    fileName = str(_imageData["tokenId"])
    fileName = str(_imageData["tokenId"]) + ".png"
    image.save(os.path.join(getProjectPath(_projectName), 'Images', fileName)) 
    image.save(os.path.join(getProjectPath(_projectName), 'Images(png)', fileName)) 
    
    
def createCustomImages(_projectName, _fileName, _projectTraits):
    '''
    Creates multipue images from date within images data and saves to Images(png)
    '''
    imagesData = loadImageData(_projectName, _fileName)
    for imageData in imagesData:
        createCustomImage(_projectName, _fileName, _projectTraits)
    
    
def createCustomImage(_projectName, _fileName, _projectTraits):
    '''
    Creates a single image from the supplied data and saves it to Images(png)
    Users can set a custom method to build images
    '''
    imagesData = loadImageData(_projectName, _fileName)
        
    ## Lists for conflicting issues
    HatIssues = ['Big Hat','Straw Hat']
    GlassesIssues =['Aviators','Raybans']
    LaserEyes = ['Laser']
    SideIssue = ['Straw Hat', 'Bucket Hat']
    
    for imageData in imagesData:
        ## Eyes ontop of certain hat
        if imageData['Mouths'] in HatIssues and imageData['Eye'] in GlassesIssues: 
            im1 = Image.open(os.path.join(getProjectPath(_projectName), 'Backgrounds' + imageData["Backgrounds"] + ".png")).convert('RGBA')
            im2 = Image.open(os.path.join(getProjectPath(_projectName), 'Furs' , imageData["Furs"] + '.png')).convert('RGBA')
            im3 = Image.open(os.path.join(getProjectPath(_projectName), 'Mouths' , imageData["Mouths"] + '.png')).convert('RGBA')
            im4 = Image.open(os.path.join(getProjectPath(_projectName), 'Eyes' , imageData["Eyes"] + '.png')).convert('RGBA')

        ## Eyes ontop of everything
        elif imageData['Eyes'] in LaserEyes: 
            im1 = Image.open(os.path.join(getProjectPath(_projectName), 'Backgrounds' + imageData["Backgrounds"] + ".png")).convert('RGBA')
            im2 = Image.open(os.path.join(getProjectPath(_projectName), 'Furs' + imageData["Furs"] + '.png')).convert('RGBA')
            im3 = Image.open(os.path.join(getProjectPath(_projectName), 'Mouths' + imageData["Mouths"] + '.png')).convert('RGBA')
            im4 = Image.open(os.path.join(getProjectPath(_projectName), 'Eyes' + imageData["Eyes"] + '.png')).convert('RGBA')

        ## Standard way
        else: 
            im1 = Image.open(os.path.join(getProjectPath(_projectName), 'Backgrounds', imageData["Backgrounds"] + ".png")).convert('RGBA')
            im2 = Image.open(os.path.join(getProjectPath(_projectName), 'Furs', imageData["Furs"] + '.png')).convert('RGBA')
            im3 = Image.open(os.path.join(getProjectPath(_projectName), 'Mouths', imageData["Mouths"] + '.png')).convert('RGBA')
            im4 = Image.open(os.path.join(getProjectPath(_projectName), 'Eyes', imageData["Eyes"] + '.png')).convert('RGBA')

        #Create each composite
        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(com1, im3)
        com3 = Image.alpha_composite(com2, im4)

        image = com3.convert('RGB')
        fileName = str(imageData["tokenId"])
        fileNamePng = str(imageData["tokenId"]) + ".png"
        image.save(os.path.join(getProjectPath(_projectName), 'Images', fileName)) 
        image.save(os.path.join(getProjectPath(_projectName), 'Images(png)', fileName)) 
    
        
#### Creating  Metadata
def getAttribute(_key, _value):
    '''
    Converts dict key and value to metadata standard
    '''
    return {
        "trait_type": _key,
        "value": _value
    }
    
    
def buildMetadataFiles(_projectName, _fileName, _imageBaseURI, _CID, _projectDiscription):    
    '''
    Builds the metadata ready for uplaod 
    '''
    data = loadImageData(_projectName, _fileName)
    for image in data:

        token = {
            "description": _projectDiscription,
            "image": _imageBaseURI + _CID + '/' + str(image['tokenId']),
            "tokenId": image['tokenId'],
            "name": image['tokenId'],
            "attributes": []
        }
        for trait in image:
            if trait != 'NONE':
                token["attributes"].append(getAttribute(trait, image[trait]))
        
        with open(os.path.join(getProjectPath(_projectName), 'MetaData', str(image['tokenId'])), 'w') as outfile:
            json.dump(token, outfile, indent=4)

            
#### Saving and Loading.
def saveWeights(_projectName, _fileName, _data):
    '''
    Saves trait weights in details as Weights_`_fileName` 
    '''
    path = os.path.join(getProjectPath(_projectName), 'Details', ('Weights_' + _fileName))
    with open(path, 'w') as f:
        json.dump(_data, f, indent=4)
    f.close()
    
    return(_fileName)


def loadWeights(_projectName, _fileName):
    '''
    Loads trait weights from details as Weights_`_fileName` 
    '''
    path = os.path.join(getProjectPath(_projectName), 'Details', ('Weights_' + _fileName))
    with open(path, 'r') as f:
        data = json.load(f)
    f.close()
    
    return(data)


def saveImageData(_projectName, _fileName, _data):
    '''
    Saves image data in details as Images_`_fileName` 
    '''
    path = os.path.join(getProjectPath(_projectName), 'Details', ('Images_' + _fileName))
    with open(path, 'w') as f:
        json.dump(_data, f, indent=4)
    f.close()
    
    return(_fileName)


def loadImageData(_projectName, _fileName):
    '''
    Loads image data from details as Images_`_fileName` 
    '''
    path = os.path.join(getProjectPath(_projectName), 'Details', ('Images_' + _fileName))
    with open(path, 'r') as f:
        data = json.load(f)
    f.close()
    
    return(data)



       
        
