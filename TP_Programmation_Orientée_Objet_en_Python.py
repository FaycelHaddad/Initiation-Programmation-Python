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