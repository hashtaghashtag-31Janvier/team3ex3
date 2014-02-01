# -*- coding: utf-8 -*-
# Problème : http://www.codingame.com/ide/?target=clogin&s=1&id=23988926040d0b7546ededc003798cd9b73fc0#!test:260471:true:%2523!list
# Solution C++ (convertie en python par mes soins) tiré de : http://blabla404.free.fr/blog/2013/07/27/codingame-juillet-2013/

N = 10000 #nb max de node
# on stocke le graphe sous la forme de liste d'adjacence (qu'on initialise avec une taille de 10000 (nb de sommets max))
graphe = [[] for i in xrange(0, N)]
# on garde en mémoire le plus long chemin à partir d'un sommet afin de ne pas refaire des calculs déjà faits
memoire = {}


def longueur(x):
  """ Retourne la longueur du chemin à partir du sommet x """
  global graphe, memoire # on déclare le graphe et la memoire en global afin de pouvoir modifier les copies présentes dans le "main" du programme
  
  if x in memoire:    # le chemin à déjà été calculé on le retourne
    return memoire[x]

  res = 1
  for i in graphe[x]:
    res = max(res, 1 + longueur(i))   # parcour du graphe en profondeur à la recherche du chemin le plus long
  
  memoire[x] = res # maj de la memoire

  return res


# on lit le fichier d'input
f = open('in3.txt', 'r')
n = int(f.readline().strip()) # lit la première ligne contenant un entier représentant le nombre e relation dans le graphe, la nettoie, et la transforme en int

# lit les n relations : xrange(0, n) est un générateur retourne à chaque appel un nombre, (0 puis 1 puis 2, jusqu'a n)
for i in xrange(0, n):        
  a, b = [int(i) for i in f.readline().split()] # récupère une relation/ligne sous la forme "a b", la transforme en ['a', 'b'], puis [a, b] et stocke les deux entier dans 2 variables
        # équivalent à :
        # ligne = f.readline() # lecture de la ligne sous forme d'une string
        # values = ligne.split() # on découpe la chaine pour récupérer les 2 valeurs (toujours sous forme de string)
        # a, b = int(values[0]), int(values[1])
  graphe[a].append(b)  # ajoute une relation de a vers b

# recherche du chemin le plus long
maxi = -1
for i in xrange(0, N):
  maxi = max(maxi, longueur(i))

print maxi
