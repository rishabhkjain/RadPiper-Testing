import os
import csv
from subprocess import call

def testFile(topFolder, testIDLst, outputFieldsLst, fileNameLst, pathToCSV):
	solutionLst = [] #where to store output files
	call(cd " topFolder", shell=True) #cd to main directory
	for testID in testIDLst: #loop through the testIDs
		tmpSolution = []
		call(cp -a " /" + topFolder + "/" + testID + "/." + " /" + topFolder + "/mainBag/", shell=True)# copy all the files from the testID directory to mainBag
		call(python "run_postprocess_batch.py " + pathToCSV + " " + "/" + topFolder + "/mainBag/ "+  "True", shell=True) #run the test file
		for file in fileNameLst:#copy over and delete specific files
			call (cp " /" + topFolder + "/mainBag/" + file + " /topFolder/" + testID + "/" + file, shell = True)
			call (rm -rf +  " /" + topFolder + "/mainBag/" + file, shell = True)
		for outputField in outputFieldLst:
			tmpSolution.append((outputField, PostProcessOutputArray[0][outputField]))

	#save output list as csv
	with open(resultFile, "w") as output:
    	writer = csv.writer(output, lineterminator='\n')
    	writer.writerows(solutionLst)




