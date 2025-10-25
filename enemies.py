from Player import *
from random import randint
from inventory import *

#enemy class that stores all the enemies in the game
class Enemy:
    def __init__(self,enemy_type=None):
        self.enemy_type = enemy_type
        self.choices = ["attack","trade","run away"]
        self.trade_amount = randint(10,10000)
        self.strength = randint(1,100)
    def trade(self,enemy_type):
        self.pMoney = Player.getGold(self)
        if self.enemy_type == "Bandits":
            if self.trade_amount > self.pMoney:
                self.Inventory.banditsSteal(Inventory,self,prefer_highest=True)
                return "The bandits are displeased with your offer and steal from you."
            else:
                self.newGold = self.addGold(-self.trade_amount)
                self.setGold(self.newGold)
                return "The bandits accept your offer and let you go." 
        elif self.enemy_type == "Barbarians":
            if  self.pMoney < self.trade_amount:
                return "The Barbarians are displeased with your offer and have killed you."
            else:
                return "The Barbarians accept your offer and let you go."
    def attack(self,enemy_type):
        self.pHealth = Player.getHealth(self)
        if self.enemy_type == "Bandits":
            if self.strength > 75:
                return "The bandits have overpowered you and killed you."
            else:
                if self.pHealth < 75 and self.strength < 75:
                    return "You have defeated the bandits!"
                elif self.pHealth < self.strength:
                    return "The bandits have defeated you and stolen from you."
                elif self.pHealth > self.strength:
                    return "The bandits have been defeated! Proceed on your quest young adventurer."
                else:
                    return "After a long battle, no damage sustained or items stolen."
        elif self.enemy_type == "Barbarians":
            if self.strength > 75:
                return "The Barbarians have overpowered you and killed you."
            else:
                if self.pHealth < 75:
                    return "You have defeated the Barbarians!"
                elif self.pHealth < self.strength:
                    return "The Barbarians have defeated you and killed you."
                elif self.pHealth > self.strength:
                    return "The Barbarians have been defeated! Proceed on your quest young adventurer."
                else:
                    return "After a long battle, no damage sustained."
        elif self.enemy_type == "Wolves":
            chance = self.winChance()
            roll = randint(1,100)
            if chance > roll:
                return "You have defeated the Wolves!"
            else:
                return "The Wolves have defeated you and killed you."
        elif self.enemy_type == "Dragon":
            chance = self.winChance()
            roll = randint(1,100) 
            if chance > roll:
                return "You have defeated the Dragon!"
            else:
                return "The Dragon has defeated you and killed you."
    def runAway(self,enemy_type):
        if self.enemy_type == "Bandits":
            chance = randint(1,100)
            if chance > 50:
                return "You have successfully run away from the Bandits!"
            else:
                return "The Bandits have caught you and stolen from you."
        elif self.enemy_type == "Barbarians":
            chance = randint(1,100)
            if chance > 50:
                return "You have successfully run away from the Barbarians!"
            else:
                return "The Barbarians have caught you and killed you."
        elif self.enemy_type == "Wolves":
            chance = randint(1,100)
            if self.number <= 5:
                chance = randint(50,100)
            else:
                chance = randint(1,50)
            if chance > 50:
                return "You have successfully run away from the Wolves!"
            else:
                return "The Wolves have caught you and killed you."
        elif self.enemy_type == "Dragon":
            chance = randint(1,100)
            if chance > 75:
                return "You have successfully run away from the Dragon!"
            else:
                return "The Dragon has caught you and killed you."



class Wolves(Enemy):
    super().__init__("Wolves")
    def __init__(self):
        self.number = randint(1,10)
        self.choices = ["attack","run away"]
        if self.choices == "attack":
            result = self.attack("Wolves")
            return result
        elif self.choices == "run away":
            result = self.runAway("Wolves")
            return result
    def winChance(self):
        if self.number == 5:
            return 50
        elif self.number < 5:
            return 75
        else:
            return 25

   
class Dragon (Enemy):
    super().__init__("Dragon")
    def __init__(self):
        self.Dhealth = 100
        self.choices = ["attack","run away"]
        if self.choices == "attack":
            result = self.attack("Dragon")
            return result
        elif self.choices == "run away":
            result = self.runAway("Dragon")
            return result
    def winChance(self):
        self.pHealth = self.getHealth()
        if self.pHealth < self.Dhealth:
            return randint(1,25)
        elif self.pHealth == self.Dhealth:
            return randint(25,50)
        else:
            return randint(50,75)
        
        

class Barbarians (Enemy):
    super().__init__("Barbarians")
    def __init__(self):
        self.strength = randint(50,100)
        self.trade_amount = randint(10,75)
        self.choices = ["attack","trade"]
        if self.choices == "trade":
            result = self.trade("Barbarians")
            return result
        elif self.choices == "attack":
            result = self.attack("Barbarians")
            return result
        elif self.choices == "run away":
            result = self.runAway("Barbarians")
            return result

       
    
class Bandits(Enemy):
    super().__init__("Bandits")
    def __init__(self):
        self.steal_amount = randint(5,25)
        self.trade_amount = randint(1,50)
        self.choices = ["attack","trade","run away"]
        if self.choices == "trade":
            result = self.trade("Bandits")
            return result
        elif self.choices == "attack":
            result = self.attack("Bandits")
            return result
        elif self.choices == "run away":
            result = self.runAway("Bandits")
            return result