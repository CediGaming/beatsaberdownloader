import shutil

def exportFolderToBS(src: str, dst:str, provider: str, id: int):
	print("Copying files to Beat Saber...")
	try:
		shutil.copytree(src, dst + f"\\{provider}-{id}")
		print("Copied files to Beat Saber!")
	except FileExistsError as e:
		print("Error: A download from this provider with this id already exists.")
