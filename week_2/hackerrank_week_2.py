def roman_to_integer(s):
    # the s string must be ordered in descending order unless special cases. 
    # where we subtract
    # Write your code here
    roman_to_int_map = {
        "I": 1, 
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    int_result = 0

    for i in range (len(s)):
        if i+1 < len(s) and roman_to_int_map[s[i]] < roman_to_int_map[s[i+1]]:
            int_result -= roman_to_int_map[s[i]]
        else:
            int_result += roman_to_int_map[s[i]]
        
    return int_result

t = "MCMXCIV"
s = "III"
print(roman_to_integer(t))
print(roman_to_integer(s))




