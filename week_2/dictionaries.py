# create a dict

student = {"name": "Alice"}
empty = {}

values = {0: [], 1: []}

# insert
student["emal"] = "alice@gmail.com"
# or
student.update({"major": "CS", "year": "2"})

# read
print(student["name"]) # when sure the key is there
print(student.get("phone")) # alternative
print(student.get("phone", "N/A")) # return NA to avoid errors

# exist ??
print("age" in student) # False
print("major" in student) # True

# dictionaries are mutable

# iterating
for key in student:
    print(key)

for value in student.values():
    print (value)

for k, v in student.items():
    print(k, v)

# example question:

def word_count(lst):
    new_dict = {}

    if len(lst) == 0:
        return new_dict

    for word in lst:
        if word not in new_dict:
            new_dict[word] = 1
        else:
            new_dict[word] += 1

    return new_dict

print(word_count([]))

"""
UNDERSTAND:
input: list of artists and a list of set_times
output: Dictionary of the line up
Edge Cases: Empty List 

Plan: Initialise an empty dictionary
      Check for edge Cases
     
"""

def lineup(artists, set_times):
    line_up = {}
    for i in range(len(artists)):
        line_up[artists[i]] = set_times[i]

    return line_up

    
"""
UNDERSTAND:
- given artist --> str
- festival_schedule --> dict
output: artist_info --> dict

ec: 
- artist not found
- empty dict
- key, value (key -> art_name, value: dict)
    
PLAN:
- check if artist is in festival_sch --> return dict
- if dict is empty --> return None
- search for artist name in the dict and return the value
"""

def get_artist_info(artist, festival_schedule):
    if artist not in festival_schedule:
        return {"message": "Artist not found"}
    else:
        return festival_schedule[artist]

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}
    
print(get_artist_info("Blood Orange", festival_schedule)) 

""" 
Understand:
    -Input: A dictionary
    - Output: An integer that is sum
    - Edge Cases: Empty Dictionary

Plan: Tracker that would track the sum, loop throught the values of the "day" key 


"""

def total_sales(ticket_sales):
    total = 0
    for value in ticket_sales.values():
        total += value 
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

"""
in: 2 dict
out: dict
ec: either of the dict is empty
PLAN:
- initialize an empty dict
- loop of the keys (artists)
- for each key
    - if value in dict1 == dict2
    then we add it to the new dict
"""

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflict_table = {}
    if len(venue1_schedule) == 0 or len(venue2_schedule) == 0:
        return conflict_table
    
    for artist, time in venue1_schedule.items():
         if artist in venue2_schedule:
            if venue1_schedule[artist] == venue2_schedule[artist]:
                conflict_table[artist] = time
    return conflict_table

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))


""" 
Understand: 
    - Input: 1 dict
    - Output: A string
    - Edge Cases: Empty Dictionary
Plan: Initiate an empty dictionary that track the artists and their number of votes
    Each artists starts with one vote
    vote.values()
"""


def best_set(votes):
    vote_counts = {}
    highest_vote = 1
    for artist in votes.values():
        if artist in vote_counts:
            vote_counts[artist] +=1 
        else: 
            vote_counts[artist] = 1
    for artist, score in vote_counts.items():
        if score > highest_vote:
            highest_vote = score
            highest_scorer = artist
    return highest_scorer

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))