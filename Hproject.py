class Patient:
    def __init__(self,nom,maladie,argent,poche,etat):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent
        self.poche = poche
        self.etat = etat
        self.lieu = "Salle d'attente"
        

    def rendre_endroit(self,lieu):
        self.lieu = lieu
        print(f"{self.nom} se rend à {self.lieu}")

    def prendre_medicament(self):
        print(f"{self.nom} prend ce médicament : {self.poche} de sa poche")
        self.etat = "Soigné"
        print(f"Son état est maintenant : {self.etat} ")
        

    def payer(self,prix):
        if self.argent >= prix:
            self.argent -= prix
            print(f"{self.nom} a payé {prix} euros")
            return True
        else:
            print(f"{self.nom} n'a pas assez d'argent pour payer")
            return False





class Docteur:
    def __init__(self,nom,argent):
        self.nom = nom
        self.argent = argent
        self.cabinet = []
        self.diagnostics = {"mal indenté":"ctrl+maj+",
                            "unsave":"saveOnFocusChange",
                            "404":"CheckLinkRelation",
                            "azmatique":"Ventoline",
                            "syntaxError":"f12+doc"}

    def nouveau_patient(self,patient):
        print(f"Le docteur reçoit {patient.nom} comme nouveau patient")
        self.cabinet.append(patient)
    
    def diagnostique(self,patient):
        print(f"Le docteur a trouvé la maladie de {patient.nom}, c'est : {patient.maladie}")

    def se_fait_payer(self,patient):
        has_money = patient.payer(50)
        if has_money:
            self.argent += 50
            print(f"Le docteur a été payé 50€ par {patient.nom}")
        else:
            print(f"{patient.nom} n'a pas assez d'argent pour payer la consultation")
        


        
        

    def prescription(self,patient):
        """
        chercher un remède dans le dictionnaire self.diagnostics basé sur la maladie d'un patient.
         Si la maladie est présente dans le dictionnaire, le remède associé est stocké dans la variable remede.
          Sinon, la variable remede prend la valeur None.
        """
        remede = self.diagnostics.get(patient.maladie,None)
        if remede is not None:
            print(f"Le docteur a trouvé un reméde, {patient.nom} doit prendre {remede}")
            print("l'état du patient a changé en Traitement")
            patient.etat = "Traitement"

        else:
            print(f"Le docteur n'a pas trouvé de reméde pour la maladie de {patient.nom}")

        return remede

    def afficher(self):
        print("| Nom | Maladie | Argent | Poche | État de Santé |")
        print("| -------- | -------------- | ------ | ----- | ------------- |")
        for patient in self.cabinet:
            
            print(f"| {patient.nom}| {patient.maladie} | {patient.argent} | {patient.poche} | {patient.etat} |")

class Pharmacie:
    def __init__(self,argent):
        self.argent = argent
        self.traitement = {"ctrl+maj+":60,
                            "saveOnFocusChange":100,
                            "CheckLinkRelation":35,
                            "Ventoline":40,
                            "f12+doc":20}
        
    def acheter_medicament(self,patient,remede):
        if remede in self.traitement:
            
            has_money = patient.payer(self.traitement[remede])
            if has_money:
                print(f"{patient.nom} a acheté {remede} pour {self.traitement[remede]} €")
                self.argent += self.traitement[remede]
                patient.poche = remede
                patient.prendre_medicament()
            else:
                print(f"{patient.nom} n'a pas assez d'argent pour {remede}, son état est donc mort")
                patient.etat = "mort"
                patient.rendre_endroit("cimetiere")




def main():
    
    
    marcus = Patient("Marcus","mal indenté",100,"vide","malade")
    optimus = Patient("Optimus","unsave",200,"vide","malade")
    sangoku = Patient("Sangoku","404",80,"vide","malade")
    darth= Patient("DarthVader","azmatique",110,"vide","malade")
    semicolon = Patient("Semicolon","syntaxError",60,"vide","malade")

    docteur = Docteur("Paul",0)
    pharmacie = Pharmacie(argent=0)

    docteur.nouveau_patient(marcus)
    docteur.nouveau_patient(optimus)
    docteur.nouveau_patient(sangoku)
    docteur.nouveau_patient(semicolon)
    docteur.nouveau_patient(darth)
    
    print("Les patients sont dans une salle d'attente")
    print()
    docteur.afficher()
    print()
    print("Le docteur commence à recevoir les patients")
    for patient in docteur.cabinet:
        print(f"Le docteur {docteur.nom} reçoit {patient.nom}")
        # Diagnostique le patient
        docteur.diagnostique(patient)
        # inscrit un traitement
        remede = docteur.prescription(patient)
        # se fait payer
        docteur.se_fait_payer(patient)
        # se rend à la pharmacie
        patient.rendre_endroit("Pharmacie")
        # acheter médicament
        pharmacie.acheter_medicament(patient,remede)



"""
__name__ est une variable spéciale en Python qui contient le nom du module actuel.
__main__ est une chaîne de caractères spéciale qui est assignée à __name__ lorsque le fichier Python est exécuté en tant que programme principal.
Ainsi, la condition if __name__ == "__main__": vérifie si le fichier Python est exécuté en tant que programme independent. 
Si c'est le cas, le bloc de code indenté qui suit (généralement une fonction appelée main()) sera exécuté.
"""

if __name__ == "__main__":
    main()
