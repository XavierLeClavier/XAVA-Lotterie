from random import randint

#1) Intro
message_bienvenue = "Bienvenue au système de lotterie de la companie Xava Enterprise Inc. Corp. Ent. ©"
print(message_bienvenue)

#2) Calculs listes
#Liste de l'utilisateur
def Lutilisateur():
  Ldonne = []
  nint = 1
  while nint <= 5:
    n = float(input(f"Saisissez votre nombre numéro {nint} (entre 1 et 60 inclus): "))
    if n % 1 != 0:
      n = int(input("Veuillez saisir uniquement un nombre décimal : "))
    n = int(n)
    if n > 60 or n < 1:
      while n > 60 or n < 1:
        n = int(input("Veuillez saisir un nombre entre 1 et 60 inclus seulement : "))
    for e in Ldonne:
      if n == e:
        while n == e:
          n = int(input("Veuillez saisir un nombre n'ayant pas déja  été utilisé : "))
    nint += 1
    Ldonne.append(n)
  return Ldonne
##[45,]

# Liste terces
def numutilis():
  """
  La fonction créé un nombre de participants aléatoir entre 150 000 et 1 000 000
  Aucune entrées
  Valeur sortie: a --> nombres de participants autre
  """
  a = randint(150000, 1000000)
  return a

def otherdictionnaire(nu):
  """
  La fonction crée pour chaque utilisateur terces (selon le nombre obtenu avec numutilis()) une liste aléatoire de nombres entre 1 et 60
  Valeur entrée: nu --> nombre d'utilisateurs
  Valeur sortie: Dother --> Dictionnaire ou les clefs sont les 'noms d'utilisateur' et le valeurs sont la liste de 5 nombres qu'ils ont 'choisis'
  """
  Dother = {}
  for i in range(0, int(nu)):
    L = []
    for ie in range(5):
      L.append(randint(1, 60))
    goodkey = str(i)
    Dother[goodkey] = L
  return Dother

# Liste gagnante
def winning_numbers():
  """
  La fonction défini la liste de nombres gagnant (liste de 5 nombres entre 1 et 60)
  Aucune entrées
  Valeur sortie: winnum --> Liste gagante
  """
  winnum = []
  LocalStep = 0
  while LocalStep < 5:
    ValueForWinningList = randint(1, 60)
    if ValueForWinningList not in winnum:
      winnum.append(ValueForWinningList)
      LocalStep += 1
  return winnum

#3) Calculs additionnels
# Calcul de la loterie:
def calcpoints(Lw, Do):
  """
  La fonction donne le nombre de points gagné par chaque 'participants' (des robots)
  Un point correspond à un nombre pareil à la liste gagnante
  valeurs entrées: Lw --> liste des 5 nombres gagnants
  Do --> dictionnaire contenant tout les 'participants' et leurs 5 chiffre respectifs
  valeur sortie: Do --> dictionnaire avec le 'nom' des participants en clef et leur nombre de points en valeur attitrée
  """
  for e in Do.keys():
    points = 0
    for el in Do[e]:
      for ele in Lw:
        if el == ele:
          points += 1
    Do[e] = points
  return Do

#Appel de fonctions (chiffres gagnants à la fin pour éviter fraude)
Lutilis = Lutilisateur()
NombreUtilisateurs = numutilis()
otherdico = otherdictionnaire(NombreUtilisateurs)
winnum = winning_numbers()
otherdico['user'] = Lutilis
Dicocalcpoints = calcpoints(winnum, otherdico)

#Calcul nombre de points par joueurs
Lofall = [['0'], ['1'], ['2'], ['3'], ['4'], ['5']]
for e in Dicocalcpoints.values():
  Lofall[e].append(e)
Lofall = [['0', len(Lofall[0])-1], ['1', len(Lofall[1])-1], ['2', len(Lofall[2])-1], ['3', len(Lofall[3])-1], ['4', len(Lofall[4])-1], ['5', len(Lofall[5])-1]]
## [['0', 57480]['1', 3458] ...]

#4)Calcul argent remporté
"""
Règles:
joueurs a 5 chiffres gagnants: se partagent 47%
joueurs a 4 chiffres gagnants: se partagent 18%
joueurs a 3 chiffres gagnants: se partagent 10%
joueurs a 2 chiffres gagnants: se partagent 7%
joueurs a 1 chiffres gagnants: se partagent 4%
joueurs a 0 chiffres gagnants: rien
13%  sert a payer les taxes etc...
le 1% restant et l'arrondi vont dans la cagnotte
"""
#Calcul argent rapporté par achat tickets
def moulah(num):
  """
  Ce programme calcule combien d'argent a été rapporté par les tickets achetés sachant qu'un ticket coûte 5€
  Valeur entrée: num --> nombre de participants
  Valeur sortie: bignum --> argent total remporté
  """
  bignum = 5 + (num * 5)
  return bignum

#Calcul argents pour joueurs
def moulahforplayers(bignum):
  """
  Le programme détermine la quantité d'argent que remportent chaques 'groupes' de vainqueurs
  valeur entrée: bignum --> argent a diviser
  valeur sortie: Lml --> liste contenant l'argent attitulé pour les personne ayant eu de 0 à 5 chiffres vainquers et l'argent nécéssaire pour payer les taxes et la cagnotte (argent qui ira pour financer le gros lot futur)
  """
  five = int((bignum * 47) / 100)
  four = int((bignum * 18) / 100)
  three = int((bignum * 10) / 100)
  two = int((bignum * 7) / 100)
  one = int(bignum * 4/ 100)
  zero = 0
  if Lofall[5][1] == 0:
    five = 0
  taxes = int((bignum * 13) / 100)
  cagnotte = bignum - (five + four + three + two + one + taxes)
  Lml = [zero, one, two, three, four, five, taxes, cagnotte]
  return Lml

#Appel fonction
ListeArgentDivise = moulahforplayers(moulah(NombreUtilisateurs))

if Dicocalcpoints['user'] != 0:
  joueursmemepts = 0
  for e in Dicocalcpoints.values():
   if e == Dicocalcpoints['user']:
    joueursmemepts += 1
  Argentadistrib = ListeArgentDivise[Dicocalcpoints['user']] 
  argentremporte = float(Argentadistrib) / float(joueursmemepts)
  print(f"Vous avez remporté {str(argentremporte)[:4]} euros, le gain était de {Argentadistrib} euros et il était divisé par {joueursmemepts} personnes. \nEn total il y avait {moulah(NombreUtilisateurs)} euros en jeu et {NombreUtilisateurs} joueurs.\nLes chiffres vainqueurs étaient {winnum}. \n{str(ListeArgentDivise[7])[:3]} euros sont allés dans la cagnotte ")
else:
  print(f"Dommage, vous n'avez rien remporté! \nEn total il y avait {moulah(NombreUtilisateurs)} euros en jeu et {NombreUtilisateurs} joueurs. \nLes chiffres vainqueurs étaient {winnum} \n{str(ListeArgentDivise[7])[:3]} euros sont allés dans la cagnotte")