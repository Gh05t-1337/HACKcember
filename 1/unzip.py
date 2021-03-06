#!/usr/bin/python3
#link zur challenge: https://www.floriandalwigk.de/santas-geschenk-hackcember-1
import zipfile
import os
path ="gift"	#in diesem ordner befindet sich außschlieslich "geschenk.zip"

while(True):	#läuft bis es eine Fehlermeldung gibt. dauert nen bissl weils 2021 mal verpackt ist.
	dirs=os.listdir(path)	#dirs[0] ist der name der zu entpackenden zip datei 
	#print(dirs) 
	with zipfile.ZipFile(path+f"\{dirs[0]}") as zip_ref: #bei Linux muss da f"/{ statt f"\{ stehen
		zip_ref.extractall(path)	#wird in den ordner path entpackt
	os.remove(path+f"\{dirs[0]}")		#und gelöscht, damit es nicht zur endlosschleife kommen kann. Bei Linux muss da f"/{ statt f"\{ stehen

#am ende ist im ordner path nur noch geschenk.txt enthalten, weswegen es dann zur fehlermeldung kommt, da das keine zip datei ist
