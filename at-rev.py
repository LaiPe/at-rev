import sys
from bs4 import BeautifulSoup

def extraction(texte):
    soupe = BeautifulSoup(texte, "html.parser")
    td_list = soupe.find_all('td') #Ensemble des tags <td> de la page
    content_list = [] #Ensemble du contenu des tags <td> impairs de la page
    for i in range(len(td_list)):
        if i%2 == 1: 
            content_list += [td_list[i].string]
    return content_list 

def reconstruction(li):
    li_reconstruct = [] 
    temp = ""
    for i in range(len(li)):
        selector = li[i][len(li[i])-1] #Dernier caractère de la ligne
        caract_final = selector == "." or selector == "?" or selector == "!" 
        didascalies = li[i][0] == "(" and selector == ")"
        if caract_final or didascalies: #Si le dernier caractère de la ligne est une "fin de phrase"
            temp += li[i]
            li_reconstruct += [temp]
            temp = ""
        else:
            temp += li[i] + " "
    return li_reconstruct

def compta_caracteres(li):
    result = 0
    for e in li:
        result += len(e)
    return result

#def traduction(li):

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
    ecriture(w,liste_phrases_vo)




