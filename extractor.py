import zipfile

def extractZip(srcPath: str, dstPath: str):
	print("Extracting zip...")
	with zipfile.ZipFile(srcPath, 'r') as zip_ref:
		zip_ref.extractall(dstPath)
	print("Extracting zip finished!")