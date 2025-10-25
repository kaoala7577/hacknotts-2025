from Player import *
from random import randint
from inventory import *

class Allies:
    def __init__(self, allyType = None):
        self.allyType = allyType
        self.Inventory = Inventory()


class Healer(Allies):
    def __init__(self):
        super().__init__("Healer")
        self.heal_amount = randint(10,50)
        self.heal_chance = randint(1,100)
        self.damage_chance = randint(1,100)
        self.damage_amount = randint(5,25)
        self.choices = ["accept healing","decline healing"]
        self.pHealth = self.getHealth()
        if self.choices == "accept healing":
            if self.heal_chance >= self.damage_chance:
                self.pHealth += self.heal_amount
                self.setHealth(self.pHealth)
                print(f"You have been healed by {self.heal_amount} points. Your health is now {self.pHealth}.")
            elif self.damage_chance > self.heal_chance:
                self.pHealth -= self.damage_amount
                self.setHealth(self.pHealth)
                print(f"The Healer's tricked you! You have taken {self.damage_amount} damage. Your health is now {self.pHealth}.")

        elif self.choices == "decline healing":
            print("You have declined the Healer's offer. No changes to your health.")

class OldLady(Allies):
    def __init__(self):
        super().__init__("Old Lady")
        self.reward_chance = randint(1,100)
        self.curse_chance = randint(1,100)
        self.choices = ["give gold","decline","steal gold"]
        self.good_v_evil = randint(1,100)
        self.witch = randint(1,100)
        self.choices = ["assist","decline"]
        self.itemToBeRetrieved = ["Basket","Wild Flowers","Ancient Amulet","Mystic Scroll","Enchanted Ring"]
        self.pHealth = self.getHealth()
        if self.choices == "assist":
            if self.reward_chance > self.curse_chance:
                self.rewardItem = self.itemToBeRetrieved[randint(0,len(self.itemToBeRetrieved)-1)]
                print(f"The Old Lady is grateful for your help and rewards you with a {self.rewardItem}!")
                self.addItem(self.rewardItem)
            else:
                print("The Old Lady is actually a witch! She has cast a curse on you for helping her and now your health has declined.")
                self.pHealth -= 15
                self.setHealth(self.pHealth)
                print(f"Your health is now {self.pHealth}.")
            
        elif self.choices == "decline":
            if self.witch > 50:
                print("The Old Lady is actually a witch! She has cast a curse on you for declining her request and now your health has declined.")
                self.pHealth -= 20
                self.setHealth(self.pHealth)
                print(f"Your health is now {self.pHealth}.")
            else:
                print("You have declined the Old Lady's request. No changes to your health but now she's sad.")



class Knight(Allies):
    def __init__(self):
        super().__init__("Knight")
        #knight gives player weapons and armour to help on quest
        self.weapons = ["Sword","Axe","Bow","Dagger","Mace"]
        self.armour = ["Shield","Helmet","Chestplate","Leggings","Boots"]
        self.givenWeapon = self.weapons[randint(0,len(self.weapons)-1)]
        self.givenArmour = self.armour[randint(0,len(self.armour)-1)]
        print(f"The Knight has given you a {self.givenWeapon} and {self.givenArmour} to aid you on your quest.")
        self.addItem(self.givenWeapon)
        self.addItem(self.givenArmour)

        
'''class Seer(Allies):
    def __init__(self):
        super().__init__("Seer")
        self.prediction_chance = randint(1,100)
        self.choices = ["hear prediction","decline"]
        if self.choices == "hear prediction":
            if self.prediction_chance > 50:

                print("The Seer predicts that you will succeed on your quest and find great fortune!")
            else:
                print("The Seer foresees challenges ahead, but with courage, you may overcome them.")
        elif self.choices == "decline":
            print("You have declined to hear the Seer's prediction.")'''