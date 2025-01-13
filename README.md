# Initiation-Programmation-Python
Initiation à la programmation Python

TP. Programmation Orientée Objet en Python
(Corrigé)

# Exercice :

On veut gérer les notes des élèves d'un établissement scolaire. Pour ce fait, on va utiliser une classe élève.

Chaque élève est caractérisé par ces informations:
    NCE: l'identifiant de l'élève
    nom: nom de l'élève
    nbrNotes: le nombre de notes de l'élève
    Notes: une séquence contenant les différentes notes de l'élève

Et les méthodes suivantes :

    Un constructeur d'initialisation
    Une méthode saisie () permettant la saisie des notes d'un élève
    Une méthode affichage (): permettant l'affichage des informations d'un élève
    Une méthode moyenne () : retourne comme résultat la moyenne des notes de l'élève.
    Une methode max() qui permet d'afficher la note maximale de l'élève
    Une méthode admis () qui retourne comme résultat la valeur true, si un élève est admis (moyenne >=10) et la valeur false, sinon.

Ecrire un programme python qui permet de déclarer la classe élève et ces méthodes.

Exemple d'exécution
  **saisie**
Donner le NCE de l'élève : 123 
Donner le nom de l'élève : ali 
Donner le nombre des notes: 2 
Donner une note :15
Donner une note :13 

  **affichage** 
Le NCE est : 123
Le nom est : ali
Le nombre de note est : 2
les notes de l'élève sont:
15
13
Les notes triées de l'élève: [13, 1514
La note maximale est : 15
La moyenne est : 14.0
L'élève est admis !



![TP_Programmation_Orientée_Objet_en_Python](https://github.com/user-attachments/assets/740b9130-c84f-4e83-897a-c9e0f4df51bf)


# Corrigé :

# coding: utf-8
class Eleve:
    def __init__(self,NCE=0,nom='',nbrNotes=0,Notes=[]):
        self.NCE=NCE
        self.nom=nom
        self.nbrNotes=nbrNotes
        self.Notes=Notes
        
    def saisie(self):
        print('**saisie**')
        self.NCE=int(input('Donner le NCE de l\'élève : '))
        self.nom=input('Donner le nom de l\'élève : ')
        self.nbrNotes=int(input('Donner le nombre des notes : '))
        self.Notes=[]
        for i in range(self.nbrNotes):
            Note=float(input('Donner une note : '))
            self.Notes.append(Note)
            
    def affichage(self):
        print('**affichage**')
        print('Le NCE est : ', self.NCE)
        print('Le nom est : ', self.nom)
        print('Le nombre de not est : ', self.nbrNotes)
        print('Les notes de l\'élève sont : ')
        for i in range(self.nbrNotes):
            print(self.Notes[i])
        self.Notes.sort()
        print('Les notes triées de l\'élève : ',self.Notes)
        
    def max(self):
        maxi=0
        for i in range(self.nbrNotes):
            if self.Notes[i]>maxi:
                maxi=self.Notes[i]
        print('La note maximale est : ',maxi)
        
    def moyenne(self):
        somme=0
        for i in range(self.nbrNotes):
            somme+=self.Notes[i]
        moyen=somme/self.nbrNotes
        return moyen
        
    def admis(self):
        if eleve.moyenne()>=10:
            return True
        else:
            return False
        
eleve=Eleve()
eleve.saisie()
eleve.affichage()
eleve.max()
eleve.moyenne()
eleve.admis()
print('La moyenne est : ',eleve.moyenne())
if eleve.admis():
    print('L\'élève est admis !')
else:
    print('L\'élève est redouble !')
