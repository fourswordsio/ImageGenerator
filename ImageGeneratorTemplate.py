from PIL import Image 
from IPython.display import display 
import random
import json
import os
import requests
import typing as tp
import ImageGeneratorFunctions as ig

from os import listdir
from os.path import isfile, join
from pathlib import Path
from os.path import join, dirname


##### parameters #####
'''
Fill out all details to before starting
'''
## Project name ##
projectName = 'PROJECT_NAME'

## Discription of project ##
projectDiscription = 'PROJECT_DISCRIPTION'

## Traits intended for project ## ordered in layer position
projectTraits = ['TRAIT_1', 'TRAIT_2', 'TRAIT_3', 'TRAIT_4']

## Image data file saving ## 
fileName = 'TESTING_NAME'

## Number of Images ##
noOf = 10

'''
Fill out these details once known 
'''

## Base storage image URI ##
imageBaseURI = "https://something.mypinata.cloud/ipfs/"

## IPFS CID for uploaded images ## available after IPSF upload 
CID = 'THE_CID_FROM_UPLOADING_IMAGES_TO_IPFS'


### Use this function to build the requiered file structure in parent directory
#ig.projectStart(projectName, projectTraits)

### Build a text file template for weights, open the file in `Details` and modify weights to equal 100 for each trait
#ig.weightTemplate(projectName, fileName, projectTraits)

### Creates the data for a series of images to be built and saves the  
#ig.createImagesData(projectName, fileName, projectTraits, noOf)

### Check number of traits
#ig.traitCount(projectTraits, fileName)

### Creates images from saved 
#ig.createImages(projectName, fileName, projectTraits)
#ig.createCustomImages(projectName, fileName, projectTraits)

### Builds Metadata
#ig.buildMetadataFiles(projectName, fileName, imageBaseURI, CID, projectDiscription)




