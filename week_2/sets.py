nums = {1, 2, 3}
# print(nums)
# or
numss = set()

# add
# set.remove(idx)
nums.remove(1)
# or discard to avoid error when the idx is not available
nums.discard(4)

# add 
nums.add(7)
# print(nums)

students_A = {"Alice", "Bob", "Carol"}

students_B = {"Bob", "Carol", "David"}

union = students_A | students_B
# print("union: ", union)

intersect = students_A & students_B
# print("intersect: ", intersect)

diffA = students_A - students_B
# print("diffA: ", diffA)

symDiff = students_A ^ students_B
# print("symDiff: ", symDiff)

students_C = ["Alice", "Bob", "Carol"]
if "Alice" in students_C:
    # print("yes")
    pass

# Understand
# Input: List of Dictionaries [keys: name, habitat and population]
# Output: name of species with the lowest population (or index when tied)

# Plan
# go over each animal dicitonary in list
# have a variable keep track of the curr min population
# 

def most_endangered(species_list):
    # loop over the list 
        # .get()
    if len(species_list) <= 0:
        return "Error: Empty list"
    
    curr_min = float('inf')
    min_index = -1
    for i in range(len(species_list)):
        if species_list[i].get("population") < curr_min:
            # update
            curr_min = species_list[i].get("population")
            min_index = i
    
    return species_list[min_index].get("name")

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

# print(most_endangered(species_list))

# 2.

from collections import Counter
# Understand:
# input: 2 strings endagered and observed species
# how many instances of observed species are also endagered (Union)

# Step 1: frequency observed species 
# dictionary Key: "species", value: count 
# go over each c in endangered, lookup freq[c], add value to count variable

def count_endangered_species(endangered_species, observed_species):
    freq_dict = Counter(observed_species)
    count = 0
    endangered_set = set(endangered_species)
    observed_set = set(observed_species)
    union = endangered_set & observed_set
    # union = set(endangered_species) & set(observed_species) (one liner)
    
    for species in union:
        count += freq_dict.get(species)
    
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"
 
# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  

def navigate_research_station(station_layout, observations):
    # convert station layout to dictionary key[char], value[index]
    idx_dict = {}
    total = 0

    for index, character in enumerate(station_layout):
        idx_dict[character] = index
    
    current_idx = 0
    for c in observations:
        total += abs(current_idx - idx_dict.get(c))
        current_idx = idx_dict.get(c)
    
    return total

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

# print(navigate_research_station(station_layout1, observations1))  
# print(navigate_research_station(station_layout2, observations2))



def count_endangered_species(endangered_species, observed_species):
    observed_dict = Counter(observed_species)
    print(observed_dict)
    count = 0

    for k, v in observed_dict.items():
        if k in endangered_species:
            count += v
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"
 
# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  


def navigate_research_station(station_layout, observations):
    station_map = {}
    total_dist = 0
    curr_observ = 0

    for i in range(len(station_layout)):
        station_map[station_layout[i]] = i

    for ob in observations:
        total_dist += abs(curr_observ - station_map.get(ob))
        curr_observ = station_map.get(ob)

    return total_dist
        

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

# print(navigate_research_station(station_layout1, observations1))  
# print(navigate_research_station(station_layout2, observations2))


# 4. prioritizing endangered species

def prioritize_observations(observed_species, priority_species):
    observed_set = set(observed_species)
    priority_set = set(priority_species)
    result = []
    species_count = 0

    # make a list of animals in observed that are not priority
    non_extinct = sorted(observed_set - priority_set)

    for animal in priority_species:
        if animal in observed_species:
            species_count = observed_species.count(animal)
            result.extend([animal] * species_count)

    result.extend(non_extinct)

    return result

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

# print(prioritize_observations(observed_species1, priority_species1))
# print(prioritize_observations(observed_species2, priority_species2)) 

# 5. calculating conservation statistics

def distinct_averages(species_populations):
    n = len(species_populations)
    count = set()

    while n > 1:
        min_pop = min(species_populations)
        species_populations.remove(min_pop)
        max_pop = max(species_populations)
        species_populations.remove(max_pop)
        average = (min_pop + max_pop) / 2
        count.add(average)
        n -= 2
    return len(count)


species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

# print(distinct_averages(species_populations1))
# print(distinct_averages(species_populations2))




    