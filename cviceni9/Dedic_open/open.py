#import knihovny pro práci se soubory
import os

#vytvoří seznam, do kterého se budou přidávat cesty k souborům
files = []

#for cyklus, který prochází vnořenou strukturu a os.getcvwd bere cestu
for root,dirs,filenames in os.walk(os.getcwd()):
    #druhá smyčka prochází přímo snímky ve finální složce ze snímky, pokud jsou ve formátu png, tak přidá do proměné path cestu k souboru + název souboru.
    for filename in filenames:
        if (filename.endswith(".png")):
            path = (os.path.join(root, filename)) 
            #přidá do seznamu cestu k souboru
            files.append(path)
#kvůli omezení CMD na +-8000 znaků se načítá text do souboru .bat
input_file = "spustit_gimp.bat"
#otevře soubor
with open(input_file, "w") as file:
    #zapíše do souboru cestu k gimpu.exe a přidá k němu cestu ze seznamu, tudíž se gimp spustí s cestou ke snímku, který se má otevřít
    file.write(f"C:/GIMP/GIMP2/bin/gimp-2.10 {' '.join(files)}")
#spustí soubor a začne otevírat snímky v gimpu
os.system("spustit_gimp.bat")

"""
Skript, který otevírá snímky do GIMPU

Vytvořím si prázdný seznam, následně pomocí for cyklu iteruju přes adresářovou strukturu a příkazem os.walk ji procházím
a os.getcwd zapíše cestu k souboru. další for loop se už konkrétně kouká na snímky.
Pokud soubor končí .png, tak jej přidá do seznamu s kompletní cestou.

Kvůli omezenosti CMD 8000 znaků se musí vytvořit otevírací soubor. Dálší řádek otevře soubor spustit_gimp.bat pro zápis, do kterého
zapisuje cestu ke spuštění gimpu + k němu přidá .png ze seznamu a na závěr spustí .bat

"""

