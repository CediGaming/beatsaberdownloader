import re
import zipfile
import cloudscraper
import os

import shutil

tempZipFile = './temp.zip'
tempFolder = './temp'
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


def scrapeFile(url: str):
	print("Downloading...")
	scraper = cloudscraper.create_scraper()
	content = scraper.get(url).content
	scraper.close()
	print("Downloading finished!")
	return content

def saveAndExtractZip(content: bytes):
	print("Saving and extracting zip...")
	file = open(tempZipFile, 'wb')
	file.write(content)
	file.close()
	with zipfile.ZipFile(tempZipFile, 'r') as zip_ref:
		zip_ref.extractall(tempFolder)
	print("Saving and extracting finished!")


def exportFolderToBS(provider: str, id: int):
	print("Copying files to Beat Saber...")
	try:
		shutil.copytree(tempFolder, installPath + f"\\{provider}-{id}")
		print("Copied files to Beat Saber!")
	except FileExistsError as e:
		print("Error: A download from this provider with this id already exists.")

def cleanup():
	if os.path.exists(tempFolder):
		shutil.rmtree(tempFolder)
	if os.path.exists(tempZipFile):
		os.remove(tempZipFile)


def promptSourceURL():
	print("Please provide the source (Web-)URL of the map to download:")
	url = input()
	if url.endswith('\\'):
		url = url[:-1]
	return url

def parseProviderFromURL(url: str):
	array = url.split('/')
	for item in array:
		regex = re.search('\w*\.\w*', item)
		if regex != None:
			return item
	
	return "Unknown.Domain"

def parseIdFromURL(url: str):
	array = url.split('/')
	
	return int(array[-1])



if __name__ == "__main__":
	cleanup()
	installPath = readInstallPath()
	while True:
		weburl = promptSourceURL()
		provider = parseProviderFromURL(weburl)
		id = parseIdFromURL(weburl)
		scrapeurl = f"https://{provider}/api/download/key/{id}"

		saveAndExtractZip(scrapeFile(scrapeurl))
		exportFolderToBS(provider, id)

		cleanup()
		print("Done!")
