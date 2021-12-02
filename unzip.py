import zipfile
import os
path ="H:\ProgrammiersprachenCode\Python\hackcember\gift"


while(True):
	dirs=os.listdir(path)

	print(dirs)

	with zipfile.ZipFile(path+f"\{dirs[0]}") as zip_ref:
		zip_ref.extractall(path)

	os.remove(path+f"\{dirs[0]}")