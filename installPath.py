import os

installPathFile = './installPath.txt'
defaultInstallPath = "C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels"

def readInstallPath():
	if os.path.exists(installPathFile):
		file = open(installPathFile, 'r')
		text = file.read()
		file.close()
		return text
	elif os.path.exists(defaultInstallPath):
		saveInstallPath(defaultInstallPath)
		return readInstallPath()
	else:
		saveInstallPath(promptForInstallPath())
		return readInstallPath()

def promptForInstallPath():
	print("No installation path has been found. Please enter your Beat Saber installation path:")
	path = input()
	if path.endswith('\\'):
		path = path[:-1]
	array = path.split('\\')

	if array[-1] == "Beat Saber": 
		path += "\\Beat Saber_Data\\CustomLevels"
	elif array[-1] == "Beat Saber_Data":
		path += "\\CustomLevels"
	elif array[-1] == "CustomLevels":
		pass

	return path

def saveInstallPath(path: str):
	file = open(installPathFile, 'w')
	file.write(path)
	file.close()