import os

files = []
for root,dirs,filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if (filename.endswith(".png")):
            path = (os.path.join(root, filename)) 
            files.append(path)
input_file = "spustit_gimp.bat"
with open(input_file, "w") as file:
    file.write(f"C:/GIMP/GIMP2/bin/gimp-2.10 {' '.join(files)}")
os.system("spustit_gimp.bat")

"""
Skript, který otevírá snímky do GIMPU

Vytvořím si prázdný seznam, následně pomocí for cyklu iteruju přes adresářovou strukturu a příkazem os.walk ji procházím
a os.getcwd zapíše cestu k souboru. další for loop se už konkrétně kouká na snímky.
Pokud soubor končí .png, tak jej přidá do seznamu s kompletní cestou.

Kvůli omezenosti CMD 8000 znaků se musí vytvořit otevírací soubor. Dálší řádek otevře soubor spustit_gimp.bat pro zápis, do kterého
zapisuje cestu ke spuštění gimpu + k němu přidá .png ze seznamu a na závěr spustí .bat

"""