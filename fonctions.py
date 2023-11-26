def extraction(texte):
    from bs4 import BeautifulSoup
    from datetime import time
    
    soupe = BeautifulSoup(texte, "html.parser")
    td_list = soupe.find_all('td') # Ensemble des tags <td> de la page
    content_list = [] # Ensemble du contenu
    current_minute = time(hour=0, minute=0) # Minute en cours
    temp = [] # Ensemble des entrées contenue dans la minute en cours

    for i in range(len(td_list)): # i = indice de lecture du fichier, parcourant les td (timecode et content)
        if i%2 == 1: # Si i est impair (content)
            temp += [td_list[i].string] # Nouvelle entrée ajouté 
        else: #Si i est pair (timecode)
            lecture_minute = time(hour=int(td_list[i].string[0:2]), minute=int(td_list[i].string[3:5])) # Formatage de la minute lue pour comparaison
            if lecture_minute > current_minute: # Si la minute lu est supérieure à la minute en cours 
                current_minute = lecture_minute # Passage à la nouvelle minute
                content_list += [temp]
                temp = []
    content_list += [temp]
    return content_list

def reconstruction(li_content):
    li_reconstruct = []
    temp = ""
    for minute in li_content:
        temp_minute = []
        for ligne in minute:
            last_car = ligne[len(ligne)-1] #Dernier caractère de la ligne
            alast_car = ligne[len(ligne)-2] #Avant-dernier caractère de la ligne
            aalast_car = ligne[len(ligne)-3] #Avant-avant-dernier caractère de la ligne

            caract_final = last_car == "." or last_car == "?" or last_car == "!" or last_car == ")"
            guillemets_final = last_car == '"' and (alast_car == "." or alast_car == "?" or alast_car == "!")
            points_suspens = last_car == "." and alast_car == "." and aalast_car == "."

            if caract_final or guillemets_final or points_suspens: #Si cette ligne constitue une fin de phrase
                temp += ligne
                temp_minute += [temp]
                temp = ""
            else:
                temp += ligne + " "
        li_reconstruct += [temp_minute]
        temp_minute = []

    return li_reconstruct

def compta_caracteres(li):
    result = 0
    for minute in li:
        for e in minute:
            result += len(e)
    return result

def traduction(li):
    from google.cloud import translate_v2 as translate
    translate_client = translate.Client()
    li_trad = []

    for minute in li:
        temp_minute = []
        for e in minute:
            if isinstance(e, bytes):
                e = e.decode("utf-8")  
            result = translate_client.translate(e, target_language="fr")
            temp_minute += [result["translatedText"]]
        li_trad += [temp_minute]
        temp_minute = []
    return li_trad

def modifications(li,dict_modifs):
    li_modif = []
    for minute in li:
        temp = []
        for chain in minute:
            chain_modif = chain
            for key in dict_modifs:
                if key in chain:
                    chain_modif = chain_modif.replace(key, dict_modifs[key])
            temp += [chain_modif]
        li_modif += [temp]
        temp = []
        
    return li_modif

def ecriture(w,li_content):
    from datetime import datetime, timedelta
    m = datetime(year=1, month=1, day=1, hour=0, minute=0) # Minute courante
    for minute in li_content:
        for e in minute:
            w.write(e)
            w.write("\n\n")
        m = m + timedelta(minutes=1)
        w.write("============== "+m.strftime("%H:%M")+" ==============")
        w.write("\n\n")
        

def init_glossaire():
    import csv
    dict = {}
    f = open("glossaire.csv","r",encoding="UTF-8")
    l = csv.reader(f,quotechar='+')
    for ligne in l:
        dict[ligne[0]] = ligne[1]
    return dict