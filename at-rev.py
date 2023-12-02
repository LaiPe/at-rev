import os
import sys
import fonctions as fnc

syntaxe = "python at-rev.py [nom-du-fichier-input] <etape-finale-processus> [nom-du-fichier-output] (options)"
etapes_process = ["-e","-r","-t","-c"]

def erreur_syntaxe():
    print("Syntaxe :",syntaxe)
    print("Pour plus d'aide concernant la syntaxe, essayez 'python at-rev.py -h'")
def aide():
    print("Syntaxe :",syntaxe,"\n")
    print("<etape-finale-processus> :")
    print("-e : extraction")
    print("-r : recontruction")
    print("-t : traduction")
    print('-c : "complet" , extraction + reconstruction + traduction + modifications\n')
    print("(options) :")
    print("--no-timecodes : empêche l'ecriture dans le fichier de sortie des timecodes délimitant chaque minute")
    print()

if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("Aide :\n")
        aide()
        exit(0)
    
    if len(sys.argv) < 4:
        print("Pas assez d'arguments")
        erreur_syntaxe()
        exit(1)
    if not(sys.argv[2] in etapes_process):
        print("Paramètre de processus invalide")
        erreur_syntaxe()
        exit(2)
    
    timeCode = True
    for i in range(4,len(sys.argv)):
        if sys.argv[i] == "--no-timecodes":
            timeCode = False
        else:
            print("Option invalide :",sys.argv[i])
            erreur_syntaxe()
            exit(3)
            
    chemin_absolu_script = os.path.dirname(os.path.abspath(__file__))
    glossaire = fnc.init_glossaire(chemin_absolu_script)
    
    input = open(sys.argv[1],"r", encoding='utf-8')
    output = open(sys.argv[3],"w+", encoding='utf-8')
   

    texte = input.read()
    input.close()
    print("\n- Traitement du fichier",sys.argv[1])

    liste_lignes_vo = fnc.extraction(texte)
    print("- Extraction")
    if sys.argv[2] == "-e":
        fnc.ecriture(output,liste_lignes_vo,timeCode)
        output.close()
        print("- Ecriture")
        exit(0)

    liste_phrases_vo = fnc.reconstruction(liste_lignes_vo)
    print("- Reconstruction")
    if sys.argv[2] == "-r":
        fnc.ecriture(output,liste_phrases_vo,timeCode)
        output.close()
        print("- Ecriture")
        exit(0)

    print("\n=> ",fnc.compta_caracteres(liste_phrases_vo)," caractères envoyées à l'API Google Translate\n",sep="")
    liste_phrases_traduites = fnc.traduction(liste_phrases_vo)
    print("- Traduction")
    if sys.argv[2] == "-t":
        fnc.ecriture(output,liste_phrases_traduites,timeCode)
        output.close()
        print("- Ecriture")
        exit(0)
    
    liste_phrases_traduites = fnc.modifications(liste_phrases_traduites,glossaire)
    print("- Modification")
    if sys.argv[2] == "-c":
        fnc.ecriture(output,liste_phrases_traduites,timeCode)
        output.close()
        print("- Ecriture")



