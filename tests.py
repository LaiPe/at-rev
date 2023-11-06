import fonctions as fnc


glossaire = fnc.init_glossaire()
print("glossaire :",glossaire)

li = ["bonjour, phrase témoin","l’espoir fait vivre","R&amp;D","l&#39;aspect","il m'a dit : « Bonjour ! »","et je lui ai dit : &quot;Bonjour&quot;","espace insécable","'''''","m'm'm'm'am'a"]

li = fnc.modifications(li,glossaire)
for e in li:
    print(e)