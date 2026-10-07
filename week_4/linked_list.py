class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

x = Node(3)
y = Node(4)

x.next = y
print(x.value)

"""
Understand: 
Input: List of strings, integer for the limit
Output: A list of strings that do not go beyond this limit
Edge cases: An empty list, negative target value

Plan:
Iterate through list; for each string, add it to a "filtered" list if the length is less than the limit
"""


def filter_meme_lengths(memes, max_length):
    if max_length < 0:
        print("Error: negative max length")
        return memes
    
    filtered_list = []
    for meme in memes:
        if len(meme) <= max_length:
            filtered_list.append(meme)
    
    return filtered_list



memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

print(filter_meme_lengths(memes, 20))
print(filter_meme_lengths(memes_2, 15))
print(filter_meme_lengths(memes_3, 10))

from collections import Counter 

def find_trending_memes(memes):
    memes_freq = Counter(memes) 
    trending_memes = []

    for meme, freq in memes_freq.items():
        if freq > 1:
            trending_memes.append(meme)
    return trending_memes

# O(n): time & space 
memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(find_trending_memes(memes))
print(find_trending_memes(memes_2))
print(find_trending_memes(memes_3))


# 4.
"""
Understand: 
Input: a list of strings
Output: that list of strings, but reversed
Edge cases: empty list, list with only one element

Plan:
Make another stack
Pop items from memes into this stack
Return the stack
"""

def reverse_memes(memes):
    reversed_memes = []
    for i in range(len(memes) - 1, -1, -1):
        reversed_memes.append(memes[i])
    return reversed_memes

memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(reverse_memes(memes))
print(reverse_memes(memes_2))
print(reverse_memes(memes_3))

# O(n) time and space
"""
Output Example:
['One does not simply walk into Mordor', 'Distracted boyfriend', 'Dogecoin to the moon!']
['This is fine', 'Expanding brain', 'Surprised Pikachu']
['Bad Luck Brian', 'Philosoraptor', 'First world problems', 'Y U No?']
"""
