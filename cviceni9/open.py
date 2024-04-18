import os

files = []
for root,dirs,filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if (filename.endswith(".png")):
            path = (os.path.join(root, filename)) 
            files.append(path)
os.system("C:/GIMP/GIMP2/bin/gimp-2.10 " + " ".join(files))

"""
Skript, který otevírá snímky do GIMPU

Vytvořím si prázdný seznam, následně pomocí for cyklu iteruju přes adresářovou strukturu a příkazem os.walk ji procházím
a os.getcwd zapíše cestu k souboru. další for loop se už konkrétně kouká na snímky.
Pokud soubor končí .png, tak jej přidá do seznamu s kompletní cestou. Následně se spustí GIMP, který se načítá s cestami uloženými v seznamu.

"""



