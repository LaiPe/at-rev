import sys
import fonctions as fnc

if __name__ == "__main__":

    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')

    if len(sys.argv) < 3 or sys.argv[2] != "-w":
        print("\nSyntaxe : at-rev.py <nom-du-fichier-input> -w <nom-du-fichier-output>\n")
        exit(1)
    
    glossaire = fnc.init_glossaire()
    w = open(sys.argv[3],"w+", encoding='utf-8')
    f = open(sys.argv[1],"r", encoding='utf-8')
    
    texte = f.read()
    f.close()
    print("\n- Traitement du fichier",sys.argv[1])

    liste_lignes_vo = fnc.extraction(texte)
    print("- Extraction")

    liste_phrases_vo = fnc.reconstruction(liste_lignes_vo)
    print("- Reconstruction")

    print("\n=> ",fnc.compta_caracteres(liste_phrases_vo)," caractères envoyées à l'API Google Translate\n",sep="")
    liste_phrases_traduites = fnc.traduction(liste_phrases_vo)
    print("- Traduction")

    liste_phrases_traduites = fnc.modifications(liste_phrases_traduites,glossaire)
    print("- Modification")

    fnc.ecriture(w,liste_phrases_traduites)
    w.close()
    print("- Ecriture")



