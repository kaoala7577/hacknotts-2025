from Player import *
from random import randint, choice
from inventory import *

class Allies:
    def __init__(self, player, allyType = None):
        self.allyType = allyType
        self.Inventory = inventory()


class Healer(Allies):
    def __init__(self, player):
        super().__init__(player, "Healer")
        self.opening_text = "A healer approaches you with open arms."
        self.image = "❤️‍🩹"
        self.heal_amount = randint(10,50)
        self.heal_chance = randint(1,100)
        self.damage_chance = randint(1,100)
        self.damage_amount = randint(5,25)
        self.choices = ["accept healing","decline healing"]
        self.pHealth = self.player.getHealth()
        if self.choices == "accept healing":
            if self.heal_chance >= self.damage_chance:
                self.pHealth += self.heal_amount
                self.player.setHealth(self.pHealth)
                self.closing_text = f"You have been healed by {self.heal_amount} points. Your health is now {self.pHealth}."
            elif self.damage_chance > self.heal_chance:
                self.pHealth -= self.damage_amount
                self.player.setHealth(self.pHealth)
                self.closing_text = f"The Healer's tricked you! You have taken {self.damage_amount} damage. Your health is now {self.pHealth}."

        elif self.choices == "decline healing":
            self.closing_text = "You have declined the Healer's offer."

class OldLady(Allies):
    def __init__(self, player):
        super().__init__(player, "Old Lady")
        self.opening_text = "An old lady calls you to the side and asks if you could help her out."
        self.image = "👵"
        self.reward_chance = randint(1,100)
        self.curse_chance = randint(1,100)
        self.choices = ["give gold","decline","steal gold"]
        self.good_v_evil = randint(1,100)
        self.witch = randint(1,100)
        self.choices = ["assist","decline"]
        self.itemToBeRetrieved = ["Basket","Wild Flowers","Ancient Amulet","Mystic Scroll","Enchanted Ring"]
        self.pHealth = self.player.getHealth()
        if self.choices == "assist":
            self.rewardItem = self.itemToBeRetrieved[randint(0,len(self.itemToBeRetrieved)-1)]
            self.closing_text = f"The Old Lady is grateful for your help and rewards you with a {self.rewardItem}!"
            self.player.inventory.addItem(self.rewardItem)
            
        elif self.choices == "decline":
            if self.witch > 50:
                self.pHealth -= 20
                self.player.setHealth(self.pHealth)
                self.closing_text = f"The Old Lady is actually a witch! She has cast a curse on you for declining her request. Your health is now {self.pHealth}."
            else:
                self.closing_text = "You have declined the Old Lady's request. She looks very sad."



class Knight(Allies):
    def __init__(self, player):
        super().__init__(player, "Knight")
        self.opening_text = "A knight approaches you on the roadside."
        self.image = "🛡️"
        #knight gives player weapons and armour to help on quest
        self.weapons = ["Sword","Axe","Bow","Dagger","Mace"]
        self.armour = ["Shield","Helmet","Chestplate","Leggings","Boots"]
        self.givenWeapon = self.weapons[randint(0,len(self.weapons)-1)]
        self.givenArmour = self.armour[randint(0,len(self.armour)-1)]
        self.closing_text = f"The Knight has given you a {self.givenWeapon} and {self.givenArmour} to aid you on your quest."
        self.player.inventory.addItem(self.givenWeapon)
        self.player.inventory.addItem(self.givenArmour)

class Tavern(Allies):
    def __init__(self, player):
        super().__init__(player, "Tavern")
        locations = ["Village","Town","City","Fortress","Castle"]
        self.TavernLocation = choice(locations)
        self.pHealth = self.player.getHealth()
        if self.TavernLocation == "Village":
            self.opening_text = "You have arrived at a small village tavern. You rest amongst the friendly villagers, but realise you need to keep moving on your quest regardless of the warm welcome. After a brief respite, you continue your journey, feeling slightly more refreshed. Your health increases by 10 points."
            self.image = "🛖"
            self.pHealth += 10
            self.player.setHealth(self.pHealth)
            self.closing_text = f"Your health is now {self.pHealth}."
        
        elif self.TavernLocation == "Town":
            self.opening_text = "You have stumbled upon a bustling town tavern filled with cheerful town folk and excited adventurers. You decide to settle here briefly, enjoying the lively atmosphere. After a hearty meal and some rest, you feel rejuvenated, and your health increases by 15 points."
            self.image = "🏠"
            self.pHealth += 15
            self.player.setHealth(self.pHealth)
            self.closing_text = f"Your health is now {self.pHealth}."
        
        elif self.TavernLocation == "City":
            self.opening_text = "You enter a grand city tavern, where the air is filled with the sounds of music and laughter. You take a moment to relax and mingle with the vivacious city dwellers. After a night filled with merriment (and potential hangover), you gather your strength and your health increases by 20 points."
            self.image = "🏘️"
            self.pHealth += 20
            self.player.setHealth(self.pHealth)
            self.closing_text = f"Your health is now {self.pHealth}."
        
        elif self.TavernLocation == "Fortress":
            self.opening_text = "You find yourself in a fortified tavern within a mighty fortress. The atmosphere is filled with tales of valor and bravery. You take a moment to rest among the seasoned warriors, gaining inspiration from their stories. After some time, you feel invigorated, and your health increases by 25 points."
            self.image = "🏛️"
            self.pHealth += 25
            self.player.setHealth(self.pHealth)
            self.closing_text =  f"Your health is now {self.pHealth}."
        
        elif self.TavernLocation == "Castle":
            self.opening_text = "You are granted the rare privilege of entering a lavish castle tavern only frequented by royalty, nobles and distinguished guests. The opulence and grandeur of the surroundings initially overwhelm you, but you soon find yourself relaxing and getting used to the taste of luxury. Alas after a night of indulgence and extravagance, you must continue your quest though you will miss the comforts of the castle. Your health increases by 30 points."
            self.image = "🏰"
            self.pHealth += 30
            self.player.setHealth(self.pHealth)
            self.closing_text = f"Your health is now {self.pHealth}."
