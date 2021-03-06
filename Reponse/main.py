#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Représente un node dans l'arbre
class Dude:
    influences = []

    def add_influence(self, name):
        self.influences.append(name)

    # Calcule récursivement la profondeur des liens du dude
    def deepness(self):
        most_deep = 1
        for i in self.influences:
            most_deep = max(most_deep, entry[i].deepness())
        return most_deep


#Parse le fichier d'entrée et génère la liste des objets de dudes
#Fonctionne!
def parse(filepath):
    listeDudes = {}
    with open(filepath, "r") as f:
        for line in f:
            # On crée le dude si celui-ci n'existe pas encore
            try:
                i, j = [int(n) for n in line.split()]

                try:
                    listeDudes[i]
                except KeyError:
                    listeDudes[i] = Dude()

                try:
                    listeDudes[j]
                except KeyError:
                    listeDudes[j] = Dude()

                listeDudes[i].add_influence(j)
            except :
                pass 
        
    return listeDudes

#j'ai supposé qu'il n'y avait pas plus de 10 noeuds (0 à 9)
#Ne fonctionne pas pour l'instant
#def visit(source,influences,visited,deepness):
    #si le noeud est visité, on retourne sa profondeur
    #if source in visited:
   #     return deepness

    #on parcourt chaque influence. Si le premier est le noeud source, on visite le noeud qu'il influence. 
    #most_deep = 0
    #visited.append(source)
    #for i in influences:
     #   if i[0] == source and i[2] not in visited:
      #      current_deep = visit(i[2], influences, visited, deepness + 1)
       #     if current_deep > most_deep:
        #        most_deep = current_deep
    #return most_deep

#main pour tester
# MARCHE PAS
if __name__ == "__main__":
    entry = parse("entry.txt")

    most_deep = 1
    for i in entry.viewkeys():
        most_deep = max(most_deep, entry[i].deepness())

    # print most_deep
    #answer = visit(entry[0], entry[1:], [], 0)
    #print(str(answer))
            
        
