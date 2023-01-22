from microbit import * #importer la librairie microbit pour pouvoir utiliser les méthodes "show" et "sleep"
import random, radio #importer les librairies random et radio, random pour génerer un nombre aléatoire et radio pour communiquer entre les deux cartes microbit
 
radio.config(group = 22) #configuration de la radio sur le canal 22
radio.on() #allumer la radio

class chi_fu_mi: #création de la class chifumi
    def __init__(self): 
        self.score = 0 #initialisation du score 
    def ciseaux(self): #méthode ciseaux
        self.coup = "C" ##ttribution du str "C" à la variable coup 
        display.show(self.coup) #affichage de la lettre "C" sur la carte microbit
        sleep(3000) #pause de 3 secondes 
        player1.resultat() #appel de la méthode score
    def feuille(self):
        self.coup = "F" #attribution du str "C" à la variable coup 
        display.show(self.coup) #affichage de la lettre "F" sur la carte microbit
        sleep(3000) #pause de 3 secondes 
        player1.resultat() #appel de la méthode score
    def pierre(self):
        self.coup = "P" #attribution du str "C" à la variable coup 
        display.show(self.coup) #affichage de la lettre "P" sur la carte microbit
        sleep(3000) #pause de 3 secondes
        player1.resultat() #appel de la méthode score
    def reset(self): #méthode reset
        display.clear() #éteint les led
        self.score = 0 #remet le score à 0 
    def resultat(self): #méthode score
        bool = True #création d'une variable booléenne
        while bool == True: # check de variable 
            coup_adversaire = radio.receive() #attribution du coup recu par le capteur de la carte à une variable
            if coup_adversaire != None: ##ondition qui vérifie si l'adversaire a joué 
                if coup_adversaire == self.coup: #vérifie sir les 2 coups sont similaire (égalité)
                    display.show("D") #affiche "D" pour Draw = égalité 
                    radio.send("D")  #envoi l'information de l'égalité à l'autre carte 
                    sleep(3000) #pause de 3 secondes
                elif coup_adversaire == "C" and self.coup == "P": #cas ou l'adversaire joue ciseaux et nous pierre
                    display.show("W")   ##affiche "W" pour win
                    radio.send("L") #envoi "L" pour loose à l'autre carte 
                    sleep(3000) 
                    self.score +=1 #ajout d'un point à la variable score 
                elif coup_adversaire == "C" and self.coup == "F":
                    display.show("L")
                    radio.send("W")
                    sleep(3000)
                elif coup_adversaire == "F" and self.coup == "C":
                    display.show("W")
                    radio.send("L")
                    sleep(3000)
                    self.score += 1
                elif coup_adversaire == "F" and self.coup == "P":
                    display.show("L")
                    radio.send("W")
                    sleep(3000)
                elif coup_adversaire == "P" and self.coup == "F":
                    display.show("W")
                    radio.send("L")
                    sleep(3000)
                    self.score += 1
                elif coup_adversaire == "P" and self.coup == "C":
                    display.show("L")
                    radio.send("W")
                    sleep(3000)
                display.show(self.score) #affichage du score de la carte à la fin de la manche 
                bool = False #arret de la boucle 
                                
player1 = chi_fu_mi() ##attribution 

while True:  #boucle à la base du programme de la carte, elle s'execute en continue  
    display.clear() #on eteint tous les pixels de l'écran pour mettre ou remettre l'affichage à 0
    if button_a.is_pressed() and button_b.is_pressed(): #condition qui vérifie quand les touches A et B sont préssées simultanément
        player1.reset() #lance l'attribut reset de la class chifumi avec l'agument 
    if accelerometer.was_gesture("shake"):
        coup = random.randint(0,2)
        if coup == 0:
            player1.ciseaux()
        elif coup == 1:
            player1.feuille()
        else:
            player1.pierre()  
        sleep(3000) #pause de 3 secondes 
