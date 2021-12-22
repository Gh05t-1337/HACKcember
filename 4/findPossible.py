#!/usr/bin/python3
#link zur Challenge: https://www.floriandalwigk.de/das-letzte-geschenk-hackcember-2021/
#findet die möglichen passwörter. (müssen dann einfach nacheinander an der zip getestet werden)
#es ist ein passwort in der rockyou.txt, das 24*4=96 zeichen hat.

#rockyou.txt wird benötigt. einfach danach googlen und downloaden

text=""
with open("rockyou.txt","r",encoding='latin-1') as f:
	text=f.read()
	
for word in text.split("\n"):
	if len(word)==96:
		print(word)
