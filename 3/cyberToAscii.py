#!/usr/bin/python3
#link zur Challenge: https://www.floriandalwigk.de/das-cyber-rotkaeppchen/
with open("cyber.txt") as f:
    cyber=f.read().lower()  #Cybermärchen lesen

cyberliste=""

for wort in cyber.split():
    if "cyber" in wort:     #für alle Cyber Wörter:
        if wort.split("cyber")[1][0]=="-":  #falls mit Bindestrich getrennt: 1, sonst: 0
            cyberliste+="1"
        else:
            cyberliste+="0"


print(cyberliste+"\n") #binary

hexdec='%x' % int(cyberliste, 2) #spaßeshalber hexadecimal
print(hexdec+"\n")

#zu ascii konvertieren
text=''.join(chr(int(cyberliste[i:i+8], 2)) for i in range(0, len(cyberliste), 8))
print(f"Passwort: {text}"+"\n")
