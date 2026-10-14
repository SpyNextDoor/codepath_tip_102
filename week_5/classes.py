"""
Unit 5 Session 1
Andre, Brian, Jean
"""


"""
Understand:
- Make an instance of the Villager class
- Name is Apollo, species is Eagle, catchphrase is pah
"""
"""""""""
# 1.

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    
    
    

# Instantiate your villager here

apollo = Villager("Apollo", "Eagle", "pah")

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 
"""
"""
""""""
# 2.

bones = Villager("Bones", "Dog", "yip yip")
print(bones.greet_player("Tram"))
"""
"""# 3.
print(bones.greet_player("Samia"))"""



 #4 

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.valid_furniture = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"}

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
        
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and new_catchphrase.replace(' ','').isalpha():
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")
    
    def add_item(self, item_name):
        if item_name in self.valid_furniture:
            self.furniture.append(item_name)

    def print_inventory(self):
        inventory_map = {}

        if not self.furniture:
            print("Inventory empty")  
        
        for item in self.furniture:
            if item in inventory_map:
                inventory_map[item] += 1
            else:
                inventory_map[item] = 1

        print(inventory_map)
         



    
"""
alice = Villager("Alice", "Koala", "guvnor")



alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)


"""

# 5.
"""
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)
"""

# 6.
"""
alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
"""

# 7.
    
def of_personality_type(townies, personality_type):
    result = [villager.name for villager in townies if villager.personality == personality_type]
    """
    result = []
    for villager in townies:
        if villager.personality == personality_type:
            result.append(villager.name)
    """
    return result

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))

