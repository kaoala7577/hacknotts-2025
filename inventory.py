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

    def banditsSteal(self, prefer_highest=True):
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
    
