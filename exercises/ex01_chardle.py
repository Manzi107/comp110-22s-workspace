"""EX01 - Chardle - A cute step toward Wordle."""
_author_ = "730489734"

user_input: str = input("Enter a 5-character word:")
user_input2: str = input("Enter a single character:")

zero: str = user_input[0]
one: str = user_input [1]
two: str = user_input [2]
three: str = user_input [3]
four: str = user_input [4]

print ("Searching for " + user_input2 + " in " + user_input)
count_m: int = 0
if len(user_input) > 5: 
    print("Error: Word must contain 5 characters")
if len(user_input2) > 1:
    print("Error: Character must be a single character.")

if user_input2 == zero:
    print(user_input2 + " found at index 0")
    count_m = count_m + 1
if user_input2 == one: 
    print(user_input2 + " found at index 1")
    count_m = count_m + 1
if user_input2 == two:
    print(user_input2 + " found at index 2")
    count_m = count_m + 1
if user_input2 == three: 
    print(user_input2 + " found at index 3")
    count_m = count_m + 1
if user_input2 == four:
    print(user_input2 + " found at index 4")
    count_m = count_m + 1

print(str(count_m) + " instances of " + user_input2 + " found in " + user_input)

