import random as rd
import copy

def recherche_matrice_x3(m,x):
    for i in range(3):
        for j in range(3):
            if m[i][j]==x:
                return i,j
    return -1,-1

class jeu:
    def __init__(self):
        self.n= 3 #longeur et largeur
        self.taquin=[] #jeu
        self.etat_visite=[] #enregistrer les etat deja visités

    def ajout(self):
        self.etat_visite.append(copy.deepcopy(self.taquin))

    def etat_initial(self):
        l=[1,2,3,4,5,6,7,8,0]
        rd.shuffle(l)
        for i in range(3):
            self.taquin.append([l[3*i],l[3*i+1],l[3*i+2]])
        self.ajout()
    
    def etat_final(self):
        d=[[1,2,3],[8,0,4],[7,6,5]]
        if(self.taquin==d):
            return True
        else :
            return False

    def afficher_etat(self):
        for i in range(3):
            print(self.taquin[i])
        print("\n")

    def afficher_etat_visite(self):
        print("-------------")
        for j in self.etat_visite:
            for i in range(3):
                print(j[i])
            print("-------------")

    def existe(self):
        if self.taquin in self.etat_visite:
            return True
        else :
            return False

    def up(self):
        x,y=recherche_matrice_x3(self.taquin,0)
        if(x==0):
            return 0
        self.taquin[x][y],self.taquin[x-1][y]=self.taquin[x-1][y],self.taquin[x][y]
        if self.existe():
            self.taquin=copy.deepcopy(self.etat_visite[-1])
            return 0
        else :
            self.ajout()
            return 1

    def down(self):
        x,y=recherche_matrice_x3(self.taquin,0)
        if(x==2):
            return 0
        self.taquin[x][y],self.taquin[x+1][y]=self.taquin[x+1][y],self.taquin[x][y]
        if self.existe():
            self.taquin=copy.deepcopy(self.etat_visite[-1])
            return 0
        else :
            self.ajout()
            return 1

    def left(self):
        x,y=recherche_matrice_x3(self.taquin,0)
        if(y==0):
            return 0
        else :
            self.taquin[x][y],self.taquin[x][y-1]=self.taquin[x][y-1],self.taquin[x][y]
            if self.existe():
                self.taquin=copy.deepcopy(self.etat_visite[-1])
                return 0
            else :
                self.ajout()
                return 1
                       
    def right(self):
        x,y=recherche_matrice_x3(self.taquin,0)
        if(y==2):
            return 0
        else :
            self.taquin[x][y],self.taquin[x][y+1]=self.taquin[x][y+1],self.taquin[x][y]
            if self.existe():
                self.taquin=copy.deepcopy(self.etat_visite[-1])
                return 0
            else :
                self.ajout()
                return 1

    def pas(self):
        return len(self.etat_visite)-1

a=jeu()
a.etat_initial()
print(a.up())
print(a.up())
print(a.right())
print(a.left())
print(a.right())
print(a.down())
print(a.right())
print(a.down())
print(a.etat_final())
print(a.pas())
a.afficher_etat_visite()
a.afficher_etat()
