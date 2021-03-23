import os
import shutil

import installPath
import source
import downloader
import extractor
import exporter


tempZipFile = './temp.zip'
tempFolder = './temp'

def cleanup():
	if os.path.exists(tempFolder):
		shutil.rmtree(tempFolder)
	if os.path.exists(tempZipFile):
		os.remove(tempZipFile)


if __name__ == "__main__":
	cleanup()
	installPath = installPath.readInstallPath()
	while True:
		weburl = source.promptSourceURL()
		provider = source.parseProviderFromURL(weburl)
		id = source.parseIdFromURL(weburl)
		scrapeurl = source.generateScrapeURL(provider, id)

		downloader.scrapeZipFile(scrapeurl, tempZipFile)
		extractor.extractZip(tempZipFile, tempFolder)
		exporter.exportFolderToBS(tempFolder, installPath, provider, id)

		cleanup()
