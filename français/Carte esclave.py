from microbit import * #importer la librairie microbit pour pouvoir utiliser les méthodes "show" et "sleep"
import random, radio # importer les librairies random et radio, random pour génerer un nombre aléatoire et radio pour communiquer entre les deux cartes microbit

radio.config(group = 22) #configuration de la radio sur le canal 22
radio.on() #allumer la radio

class chi_fu_mi:
    def __init__(self): #initialisation de la classe chi_fu_mi avec la variable score égale à 0
        self.score = 0
    def ciseau(self): #méthodes ciseau, feuille et pierre de la classe chi-fu-mi
        self.coup = "C" #définir le coup tiré au hasard
        display.show(self.coup) #affichage du coup sur la carte microbit
        sleep(3000) #afficher le coup prendant 3 secondes
        radio.send(self.coup) #envoie du coup à l'autre carte microbit
        player1.resultat() #appel de la méthode resultat qui permet d'avoir le résultat de la manche
    def feuille(self):
        self.coup = "F"
        display.show(self.coup)
        sleep(3000)
        radio.send(self.coup)
        player1.resultat()
    def pierre(self):
        self.coup = "P"
        display.show(self.coup)
        sleep(3000)
        radio.send(self.coup)
        player1.resultat()
    def reset(self): #méthode clear permettant de rénitialiser la partie
        display.clear() #efface l'affiche sur la carte microbit
        self.score = 0 #rénitialise le score à 0
    def resultat(self): #méthode resultat permettant d'obtenir le résultat de la manche
        bool= True #condition d'arrêt
        while bool == True:
            resultat = radio.receive() #permet de recevoir tous les messages de l'autre carte
            if resultat != None: #si on reçoie le résultat de la manche
                if resultat == "W":
                    display.show("W")
                    sleep(3000) #affiche le résultat pendant 3 secondes
                    self.score += 1 #si on gagne ajoute un point à notre score
                    display.show(self.score) #affiche le score sur la carte microbit
                elif resultat == "D":
                    display.show("D")
                    sleep(3000)
                    display.show(self.score)
                else:
                    display.show("L")
                    sleep(3000)
                    display.show(self.score)
                bool = False #on sort de la boucle while

player1 = chi_fu_mi() #créer l'instance joueur de la classe chi_fu_mi

while True:
    display.clear()
    if button_a.is_pressed() and button_b.is_pressed(): #appelle la méthode reset si les boutons A et B sont appuyés
        player1.reset()
    if accelerometer.was_gesture("shake"): #détecte si la crate micorbit est secouée
        coup = random.randint(0,2) #génere un nombre alétoire
        if coup == 0:
            player1.ciseau() #appelle une méthode en fonction du nombre obtenu
        elif coup == 1:
            player1.feuille()
        else:
            player1.pierre( )
        sleep(3000)
