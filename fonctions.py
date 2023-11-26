def extraction(texte):
    from bs4 import BeautifulSoup
    
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
        alast_car = ligne[len(ligne)-2] #Avant-dernier caractère de la ligne
        aalast_car = ligne[len(ligne)-3] #Avant-avant-dernier caractère de la ligne

        caract_final = last_car == "." or last_car == "?" or last_car == "!" or last_car == ")"
        guillemets_final = last_car == '"' and (alast_car == "." or alast_car == "?" or alast_car == "!")
        points_suspens = last_car == "." and alast_car == "." and aalast_car == "."
        
        if caract_final or guillemets_final or points_suspens: #Si cette ligne constitue une fin de phrase
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
    for chain in li:
        chain_modif = chain
        for key in dict_modifs:
            if key in chain:
                chain_modif = chain_modif.replace(key, dict_modifs[key])
        li_modif += [chain_modif]
        
    return li_modif

def ecriture(w,li):
    for e in li:
        w.write(e)
        w.write("\n\n")

def init_glossaire():
    import csv
    dict = {}
    f = open("glossaire.csv","r",encoding="UTF-8")
    l = csv.reader(f,quotechar='+')
    for ligne in l:
        dict[ligne[0]] = ligne[1]
    return dict