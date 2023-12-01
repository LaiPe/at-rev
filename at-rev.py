import os
import sys
import fonctions as fnc

if __name__ == "__main__":

    corect_options = ["-e","-r","-t","-c"]

    if len(sys.argv) < 3 or not(sys.argv[2] in corect_options):
        print("\nSyntaxe : python at-rev.py <nom-du-fichier-input> <etape-finale-processus> <nom-du-fichier-output>\n")
        print("<etape-finale-processus> :")
        print("-e : extraction")
        print("-r : recontruction")
        print("-t : traduction")
        print('-c : "complet" , extraction + reconstruction + traduction + modifications\n')
        exit(1)
    
    chemin_absolu_script = os.path.dirname(os.path.abspath(__file__))
    glossaire = fnc.init_glossaire(chemin_absolu_script)
    f = open(sys.argv[1],"r", encoding='utf-8')
    w = open(sys.argv[3],"w+", encoding='utf-8')
   
    texte = f.read()
    f.close()
    print("\n- Traitement du fichier",sys.argv[1])

    liste_lignes_vo = fnc.extraction(texte)
    print("- Extraction")
    if sys.argv[2] == "-e":
        fnc.ecriture(w,liste_lignes_vo)
        w.close()
        print("- Ecriture")
        exit(0)

    liste_phrases_vo = fnc.reconstruction(liste_lignes_vo)
    print("- Reconstruction")
    if sys.argv[2] == "-r":
        fnc.ecriture(w,liste_phrases_vo)
        w.close()
        print("- Ecriture")
        exit(0)

    print("\n=> ",fnc.compta_caracteres(liste_phrases_vo)," caractères envoyées à l'API Google Translate\n",sep="")
    liste_phrases_traduites = fnc.traduction(liste_phrases_vo)
    print("- Traduction")
    if sys.argv[2] == "-t":
        fnc.ecriture(w,liste_phrases_traduites)
        w.close()
        print("- Ecriture")
        exit(0)
    
    liste_phrases_traduites = fnc.modifications(liste_phrases_traduites,glossaire)
    print("- Modification")
    if sys.argv[2] == "-c":
        fnc.ecriture(w,liste_phrases_traduites)
        w.close()
        print("- Ecriture")



