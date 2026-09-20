# 09/17
# We learned to use UMPIRE Method

"""
PLAN
- validate input
- initialize the result as empty string
- loop x times - add 'na' to the result in each iteration
- if result is empty, we return batman
- else we append that result to batman
- return the result
"""

# IMPLEMEMT
def nanana_batman(x):
    if not isinstance(x, int) or x < 0:
        return 'error: invalid input'
    
    result = ""
    for i in range(x):
        result += "na"

    if result:
        return result + " batman"
    
    return "batman"

# review
# print(nanana_batman(3))

# problem set version 1

# input: string with alph chars and spaces separating the words
# output: the reversed string

# edge cases: empty string, 1 word string, special chars


def reverse_sentence(sentence):
    res = ""
    words = sentence.split()
    reversed_list = []

    if len(sentence) <= 0:
        return None

    if len(words) == 1:
        return sentence

    for i in range(len(words)-1, -1, -1):
        reversed_list.append(words[i])

    res = " ".join(reversed_list)

    return res


# print(reverse_sentence("tubby little cubby all stuffed with fluff"))
# print(reverse_sentence("Pooh"))

# 2. 

def goldilocks_approved(nums): 
    if len(nums) < 3:
        return -1

    # nums.sort()

    # return nums[1]

    
    min_elt = min(nums)
    max_elt = max(nums)

    for i in nums:
        if i != min_elt and i != max_elt:
            return i

# 3. 

# input : list 
# output : list
# EC: empty list, list w/ 1 element, string 

def delete_minimum_elements(hunny_jar_sizes):
    res = []

    if len(hunny_jar_sizes) == 1:
        return hunny_jar_sizes

    while len(hunny_jar_sizes) > 0:
        min_val = min(hunny_jar_sizes)
        res.append(min_val)
        hunny_jar_sizes.remove(min_val)

    return res

# print(delete_minimum_elements([5, 3, 2, 4, 1])) 

# Problem 4: Sum of Digits

# UNDERSTAND:
#  given: int
#  output: sum --> int
# EC:
# - float?, string?, return None

# PLAN
# initialize a sum variable
# split the int into a list of ints
# convert the num to int to split it and then
# convert the individual numbers back to integers. 
# loop and sum each int in the list to a total 

def sum_of_digits(num):

    if not isinstance(num, int):
        return None
    total = 0
    list_of_nums = [int(d) for d in str(num)]

    for num in list_of_nums:
        total += num
    return total

# print(sum_of_digits(434))

# OR

def sum_of_digits2(num):
    total = 0

    while num > 0:
        # get the last digit from %
        total += (num % 10)

        # then remove the last digit using //
        num //= 10

    return total

# print(sum_of_digits(434))

# 5. Bouncy

"""
given: list of operations
output: sum --> integer
EC: empty list, no list

PLAN
- initialize a sum variable to 1
- loop through the list and assess which operation we have 
- if the list contains something else continue ie. skip it. 

"""
def final_value_after_operations(operations):
    tiger_sum = 1

    if len(operations) < 0:
        return tiger_sum

    for op in operations:
        if op == "bouncy" or op == "flouncy":
            tiger_sum += 1
        if op == "trouncy" or op == "pouncy":
            tiger_sum -= 1
        else:
            continue

    return tiger_sum

operations = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))

# 6. Acronym

"""
UNDERSTAND:
- given: list of strings, string s
- return: True or False
EC:
- Empty list
- not all elt in list are strings
- is it case sensitive?

PLAN
- check for empty string then return False
- make the acronym s case insensititve
- initialize a result string
- loop through the list, take the char at 0-id and add it to the string result 
- compare result and s if they match return True else False 
"""

def is_acronym(words, s):
    if not isinstance(words, list):
        return False
    s.lower()

    result = ""

    for w in words:
        result += w[0].lower()

    if result == s:
        return True
    
    return False

words = ["christopher", "robin", "milner"]
s = "crm"
# print(is_acronym(words, s))

# 7. good things

def make_divisible_by_3(nums):
    count = 0

    for i in nums:
        if i % 3 == 1:
            i -= 1
            count += 1
        if i % 3 == 2:
            i += 1
            count += 1

    return count

print(make_divisible_by_3([3, 6, 9]))


        



   