nums = {1, 2, 3}
print(nums)
# or
numss = set()

# add
# set.remove(idx)
nums.remove(1)
# or discard to avoid error when the idx is not available
nums.discard(4)

# add 
nums.add(7)
print(nums)

students_A = {"Alice", "Bob", "Carol"}

students_B = {"Bob", "Carol", "David"}

union = students_A | students_B
print("union: ", union)

intersect = students_A & students_B
print("intersect: ", intersect)

diffA = students_A - students_B
print("diffA: ", diffA)

symDiff = students_A ^ students_B
print("symDiff: ", symDiff)

students_C = ["Alice", "Bob", "Carol"]
if "Alice" in students_C:
    print("yes")