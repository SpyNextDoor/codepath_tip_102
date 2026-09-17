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
print(nanana_batman(3))