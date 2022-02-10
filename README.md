# ImageGenerator
Python Image Generator 
'''
PROCESS:
1. projectStart()
2. fill trait files with layer images 
3. weightTemplate() 
4. open the weightTemple text file and modify the weights so that each traits weights equal 100 (save text file)
5. createImageData()
6. traitCount() 
7. Check the traits to see if it fits with what is desired
8. createsImages()
9. Review the images in Images(png)
10. Make any nessary changes
11. Upload the files to your IPFS
12. Add the CID from the IPSF
13. buildMetadataFile()
14. Open metadata files to check if the images are the same.
15. Upload the Metadata files to IPFS
'''

### Use this function to build the requiered file structure in parent directory
#projectStart(projectName, projectTraits)

### Build a text file template for weights, open the file in `Details` and modify weights to equal 100 for each trait
#weightTemplate(projectName, fileName, projectTraits)

### Creates the data for a series of images to be built and saves the  
#createImagesData(projectName, fileName, projectTraits, noOf)

### Check number of traits
#traitCount(projectTraits, fileName)

### Creates images from saved 
#createImages(projectName, fileName, projectTraits)
#createCustomImages(projectName, fileName, projectTraits)

### Builds Metadata
#buildMetadataFiles(projectName, fileName, imageBaseURI, CID, projectDiscription)

#traitCount(projectName, projectTraits, fileName)

'''
ALL FUNCTIONS:
projectStart(_projectName, _projectTraits)
getProjectPath(_projectName)
weightTemplate(_projectName, _fileName, _projectTraits)
traitList(_trait, _data)
weightList(_trait, _data)
createImageData(_projectTraits, _data)
createImagesData(_projectName, _fileName, _projectTraits, _noOf)
checkWeights(_projectTraits, _data)
addTokenId(_allImages)
saveWeights(_projectName, _fileName, _data)
loadWeights(_projectName, _fileName)
saveImageData(_projectName, _fileName, _data)
loadImageData(_projectName, _fileName)
removeExtention(_dir) --Issues--
traitCount(_projectTraits, _fileName)
createImages(_projectName, _fileName, _projectTraits)
createImage(_projectName, _projectTraits, _imageData)
createCustomImages(_projectName, _fileName, _projectTraits)
createCustomImage(_projectName, _projectTraits, _imageData)
getAttribute(_key, _value)
buildMetadataFiles(_projectName, _fileName, _imageBaseURI, _CID, _projectDiscription)
'''
