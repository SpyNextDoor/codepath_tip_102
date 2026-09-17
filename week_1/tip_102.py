# 1.
def welcome():
    print("Welcome to The Hundred Acre Wood!")

# welcome()

# 2.
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# greeting("Juma")

# 3. 

#we all have access!!!

def get_item(items, x):
    length = len(items)
    
    return items[x] if x > length - 1 else None
    
items = ["piglet", "pooh", "roo", "rabbit"]
print(get_item(items, 5))

# 5. 

def sum_honey(hunny_jars):
    honey_sum = 0
    for i in hunny_jars:
        honey_sum += i        
    return honey_sum
    
hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

# 6. 

def doubled(hunny_jars):
    hunny_two = []
    for num in hunny_jars:
        val = num * 2 
        hunny_two.append(val)
        
    return hunny_two
    
hunny_jars = [1, 2, 3]
print (doubled(hunny_jars)) 
    
    
    
    
