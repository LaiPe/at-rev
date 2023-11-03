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
    from google.cloud import translate_v2 as translate
    translate_client = translate.Client()
    li_trad = []

    for e in li:
        if isinstance(e, bytes):
            e = e.decode("utf-8")
        
        result = translate_client.translate(e, target_language="fr")
        li_trad += [result["translatedText"]]
    return li_trad

def modifications(li,dict_modifs):
    li_modif = []
    cpt = 0
    for chain in li:
        chain_modif = chain
        for key in dict_modifs:
            if key in chain:
                cpt += 1
                chain_modif = chain_modif.replace(key, dict_modifs[key])
        li_modif += [chain_modif]
        
    print("\n=> ",cpt," phrases modifiées\n",sep="")
    return li_modif


def ecriture(w,li):
    for e in li:
        w.write(e)
        w.write("\n\n")


if __name__ == "__main__":

    glossaire = {"&#39;":"'","\u2019":"'"}

    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')

    if len(sys.argv) < 3 or sys.argv[2] != "-w":
        print("\nSyntaxe : at-rev.py <nom-du-fichier-input> -w <nom-du-fichier-output>\n")
        exit(1)
    
    w = open(sys.argv[3],"w+", encoding='utf-8')
    
    f = open(sys.argv[1],"r")
    texte = f.read()
    f.close()
    print("\n- Traitement du fichier",sys.argv[1])

    liste_lignes_vo = extraction(texte)
    print("- Extraction")

    liste_phrases_vo = reconstruction(liste_lignes_vo)
    print("- Reconstruction")

    print("\n=> ",compta_caracteres(liste_phrases_vo)," caractères envoyées à l'API Google Translate\n",sep="")
    liste_phrases_traduites = traduction(liste_phrases_vo)
    print("- Traduction")

    liste_phrases_traduites = modifications(liste_phrases_traduites,glossaire)
    print("- Modification")

    ecriture(w,liste_phrases_traduites)
    w.close()
    print("- Ecriture")



