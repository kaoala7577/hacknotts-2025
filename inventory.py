from random import randint

class Inventory:
    def __init__(self):
        self.rarity = ["common","uncommon","rare","epic","legendary"]
        self.items = {}

    def addItem(self, item, itemRarity=None):
        if itemRarity is None:
            itemRarity = self.rarity[randint(0, len(self.rarity)-1)]
        if item in self.items:
            self.items[item]["count"] += 1
        else:
            self.items[item] = {"rarity": itemRarity, "count": 1}
        return f"{item} ({itemRarity}) has been added to your inventory."

    def removeItem(self, item):
        meta = self.items.get(item)
        if not meta:
            return None
        meta["count"] -= 1
        removed = {"name": item, "rarity": meta["rarity"]}
        if meta["count"] <= 0:
            del self.items[item]
        return removed

    def viewInventory(self):
        if not self.items:
            return "Inventory is empty."
        parts = []
        for name, meta in self.items.items():
            parts.append(f"{name} x{meta['count']} ({meta['rarity']})")
        return "Inventory contains: " + ", ".join(parts)
    def _items_of_rarity_index(self, idx):
        return [(name, meta) for name, meta in self.items.items() if self.rarity.index(meta["rarity"]) == idx]

    