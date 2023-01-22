from microbit import *
import random, radio

radio.config(group = 22)
radio.on()

class rock_paper_scissors:
    def init(self):
        self.score = 0
    def scissors(self):
        self.move = "C"
        display.show(self.move)
        sleep(3000)
        radio.send(self.move)
        player1.result()
    def paper(self):
        self.move = "F"
        display.show(self.move)
        sleep(3000)
        radio.send(self.move)
        player1.result()
    def rock(self):
        self.move = "P"
        display.show(self.move)
        sleep(3000)
        radio.send(self.move)
        player1.result()
    def reset(self):
        display.clear()
        self.score = 0
    def result(self):
        bool= True
        while bool == True:
            result = radio.receive()
            if result != None:
                if result == "W":
                    display.show("W")
                    sleep(3000)
                    self.score += 1
                    display.show(self.score)
                elif result == "D":
                    display.show("D")
                    sleep(3000)
                    display.show(self.score)
                else:
                    display.show("L")
                    sleep(3000)
                    display.show(self.score)
                    bool = False

player1 = rock_paper_scissors()

while True:
    display.clear()
    if button_a.is_pressed() and button_b.is_pressed():
            player1.reset()
    if accelerometer.was_gesture("shake"):
        move = random.randint(0,2)
        if move == 0:
            player1.scissors()
        elif move == 1:
            player1.paper()
        else:
            player1.rock()
            sleep(3000)
