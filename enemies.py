from Player import *
from random import randint
from inventory import *
import inventory

#enemy class that stores all the enemies in the game
class Enemy:
    def __init__(self,player,enemy_type=None):
        self.enemy_type = enemy_type
        self.choices = ["attack","trade","run away"]
        self.trade_amount = randint(10,10000)
        self.strength = randint(1,100)
        self.player = player
    def trade(self):
        self.pMoney = Player.getGold(self)
        if self.enemy_type == "Bandits":
            if self.trade_amount > self.player.gold:
                self.player.inventory.banditsSteal(inventory,self,prefer_highest=True)
                self.closing_text = "The bandits are displeased with your offer and steal from you."
            else:
                self.newGold = self.player.addGold(-self.trade_amount)
                self.player.setGold(self.newGold)
                self.closing_text = "The bandits accept your offer and let you go." 
        elif self.enemy_type == "Barbarians":
            if  self.pMoney < self.trade_amount:
                self.closing_text = "The Barbarians are displeased with your offer and have killed you."
            else:
                self.closing_text = "The Barbarians accept your offer and let you go."
    def attack(self,enemy_type):
        self.pHealth = Player.getHealth(self)
        if self.enemy_type == "Bandits":
            if self.strength > 75:
                self.inventory.banditsSteal(inventory,self,prefer_highest=True)
                self.closing_text = "The bandits have overpowered you and stolen from you."
            else:
                if self.pHealth < 75 and self.strength < 75:
                    self.closing_text = "You have defeated the bandits!"
                elif self.pHealth < self.strength:
                    self.inventory.banditsSteal(inventory,self,prefer_highest=True)
                    self.closing_text =  "The bandits have defeated you and stolen from you."
                elif self.pHealth > self.strength:
                    self.closing_text = "The bandits have been defeated! Proceed on your quest young adventurer."
                else:
                    self.closing_text = "After a long battle, no damage sustained or items stolen."
        elif self.enemy_type == "Barbarians":
            if self.strength > 75:
                self.closing_text = "The Barbarians have overpowered you and killed you."
            else:
                if self.pHealth < 75:
                    self.closing_text = "You have defeated the Barbarians!"
                elif self.pHealth < self.strength:
                    self.closing_text = "The Barbarians have defeated you and killed you."
                elif self.pHealth > self.strength:
                    self.closing_text = "The Barbarians have been defeated! Proceed on your quest young adventurer."
                else:
                    self.closing_text = "After a long battle, no damage sustained."
        elif self.enemy_type == "Wolves":
            chance = self.winChance()
            roll = randint(1,100)
            if chance > roll:
                self.closing_text = "You have defeated the Wolves!"
            else:
                self.closing_text = "The Wolves have defeated you and killed you."
        elif self.enemy_type == "Dragon":
            chance = self.winChance()
            roll = randint(1,100) 
            if chance > roll:
                self.closing_text = "You have defeated the Dragon!"
            else:
                self.closing_text = "The Dragon has defeated you and killed you."
    def runAway(self,enemy_type):
        if self.enemy_type == "Bandits":
            chance = randint(1,100)
            if chance > 50:
                self.closing_text = "You have successfully run away from the Bandits!"
            else:
                self.inventory.banditsSteal(inventory,self,prefer_highest=True)
                self.closing_text = "The Bandits have caught you and stolen from you."
        elif self.enemy_type == "Barbarians":
            chance = randint(1,100)
            if chance > 50:
                self.closing_text = "You have successfully run away from the Barbarians!"
            else:
                self.closing_text = "The Barbarians have caught you and killed you."
        elif self.enemy_type == "Wolves":
            chance = randint(1,100)
            if self.number <= 5:
                chance = randint(50,100)
            else:
                chance = randint(1,50)
            if chance > 50:
                self.closing_text = "You have successfully run away from the Wolves!"
            else:
                self.closing_text = "The Wolves have caught you and killed you."
        elif self.enemy_type == "Dragon":
            chance = randint(1,100)
            if chance > 75:
                self.closing_text = "You have successfully run away from the Dragon!"
            else:
                self.closing_text = "The Dragon has caught you and killed you."



class Wolves(Enemy):
    def __init__(self, player):
        super().__init__(player, "Wolves")
        self.number = randint(1,10)
        self.opening_text = f"{self.number} wolves surround you!"
        self.image = "🐺"
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
    def __init__(self, player):
        super().__init__(player, "Dragon")
        self.opening_text = "A dragon is attacking you!"
        self.image = "🐉"
        self.Dhealth = 100
        self.choices = ["attack","run away"]
        if self.choices == "attack":
            result = self.attack("Dragon")
            return result
        elif self.choices == "run away":
            result = self.runAway("Dragon")
            return result
    def winChance(self):
        self.pHealth = self.player.getHealth()
        if self.pHealth < self.Dhealth:
            return randint(1,25)
        elif self.pHealth == self.Dhealth:
            return randint(25,50)
        else:
            return randint(50,75)
        
        

class Barbarians (Enemy):
    def __init__(self, player):
        super().__init__(player, "Barbarians")
        self.opening_text = "Barbarians are looking at you menacingly."
        self.image = "👊"
        self.strength = randint(50,100)
        self.trade_amount = randint(10,75)
        self.choices = ["attack","trade","run away"]
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
    def __init__(self, player):
        super().__init__(player, "Bandits")
        self.opening_text = "Bandits surround you!"
        self.image = "🗡️"
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
        
    def banditsSteal(self, inventory, prefer_highest=True):
        removed = []

        if not self.items:
            return removed

        # find highest rarity index present
        present_indices = {self.rarity.index(meta["rarity"]) for meta in self.items.values()}
        max_idx = max(present_indices)
        min_idx = min(present_indices)

        # try take one highest if requested and available
        if prefer_highest and max_idx is not None:
            candidates = self._items_of_rarity_index(max_idx)
            if candidates:
                # pick one candidate (choose the first)
                name, meta = candidates[0]
                removed_item = self.removeItem(name)
                if removed_item:
                    removed.append(removed_item)
                    return removed

    
        to_remove = 2
        idx = min_idx
        while to_remove > 0 and idx <= max_idx:
            candidates = self._items_of_rarity_index(idx)
            for name, meta in list(candidates):
                if to_remove <= 0:
                    break
                # remove one instance
                item_removed = self.removeItem(name)
                if item_removed:
                    removed.append(item_removed)
                    to_remove -= 1
            idx += 1

        return removed
    
