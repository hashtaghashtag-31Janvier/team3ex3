#!/usr/bin/env python
# -*- coding: utf-8 -*-

#parse le fichier d'entrée et le transforme en liste ["1", "1 3", "2 4"]
#Fonctionne!
def parse(filepath):
    entry = []
    with open(filepath, "r") as f:
        for line in f:
            entry.append(line[0:-1])
    print (entry)
    return entry

#j'ai supposé qu'il n'y avait pas plus de 10 noeuds (0 à 9)
#Ne fonctionne pas pour l'instant
def visit(source,influences,visited,deepness):
    #si le noeud est visité, on retourne sa profondeur
    if source in visited:
        return deepness

    #on parcourt chaque influence. Si le premier est le noeud source, on visite le noeud qu'il influence. 
    most_deep = 0
    visited.append(source)
    for i in influences:
        if i[0] == source and i[2] not in visited:
            current_deep = visit(i[2], influences, visited, deepness + 1)
            if current_deep > most_deep:
                most_deep = current_deep
    return most_deep

#main pour tester
if __name__ == "__main__":
    entry = parse("entry.txt")
    answer = visit(entry[0], entry[1:], [], 0)
    print(str(answer))
            
        
