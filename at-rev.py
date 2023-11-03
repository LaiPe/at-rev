import sys
from bs4 import BeautifulSoup

def extraction(texte):
    soupe = BeautifulSoup(texte, "html.parser")
    td_list = soupe.find_all('td') #Ensemble des tags <td> de la page
    content_list = [] #Ensemble du contenu des tags <td> impairs de la page
    for i in range(1,len(td_list),2):
        content_list += [td_list[i].string]
    return content_list 

def reconstruction(li):
    li_reconstruct = [] 
    temp = ""
    for ligne in li:
        last_car = ligne[len(ligne)-1] #Dernier caractère de la ligne
        caract_final = last_car == "." or last_car == "?" or last_car == "!" 
        didascalies = ligne[0] == "(" and last_car == ")"
        if caract_final or didascalies: #Si cette ligne constitue une fin de phrase
            temp += ligne
            li_reconstruct += [temp]
            temp = ""
        else:
            temp += ligne + " "
    return li_reconstruct

def compta_caracteres(li):
    result = 0
    for e in li:
        result += len(e)
    return result

def traduction(li):
    li_trad = []
    for e in li:
        li_trad += [appel_api(e)]
    return li_trad

def modifications(li,dict):
    li_modif = []
    temp = ""
    cpt = 0
    for chain in li:
        for letter in chain:
            if letter in dict:
                cpt += 1
                temp += dict[letter]
            else:
                temp += letter
        li_modif += [temp]
        temp = ""
    print("\n=> ",cpt," modifs effectués\n",sep="")
    return li_modif


def ecriture(w,li):
    for e in li:
        w.write(e)
        w.write("\n\n")


if __name__ == "__main__":
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')

    if len(sys.argv) < 3 or sys.argv[2] != "-w":
        print("\nSyntaxe : at-rev.py <nom-du-fichier-input> -w <nom-du-fichier-output>\n")
        exit(1)
    
    w = open(sys.argv[3],"w+")
    
    
    f = open(sys.argv[1],"r")
    texte = f.read()
    f.close()
    print("\n- Traitement du fichier",sys.argv[1])

    liste_lignes_vo = extraction(texte)
    print("- Extraction")

    liste_phrases_vo = reconstruction(liste_lignes_vo)
    print("- Reconstruction")

    print("\n=> ",compta_caracteres(liste_phrases_vo)," caractères envoyées à l'API Google Translate\n",sep="")

    list_phrases_trad_modif = modifications(liste_phrases_vo,{"’":"'"})
    print("- Modification")

    ecriture(w,list_phrases_trad_modif)
    print("- Ecriture")



