
# # Q1:
# Create a function that takes voltage and current and returns the calculated power. 
# Power = Voltage x Current

def power(voltage, current):
    power = voltage*current
    return power

# # Q2:
# Create a function that replaces all the vowels in a string with a specified character.

string = "mind blowing"
def Replace_Vowel(string,special):
    vowels = "aeiou"
    for char in string:
        if char in vowels:
           new_string =  string.replace(char,special)
    return new_string
Replace_Vowel(string,'*')

# # Q3:
# Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.


lst1 = [3,6,7,8]
lst2 = [7,9,4,3]
lst3 = [2,3,4,5,6,7] 
def Sum(lst1,lst2,lst3):
    common_number_sum = 0
    for li in lst1:
        if li in lst2:
            if li in lst3:
                common_number_sum += li
    return common_number_sum

# %%
Sum(lst1,lst2,lst3)

# # Q4:
# Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

def Loves_me_game(total_Petals):
    result = []
    for i in range(total_Petals):
        phrase = "Loves me" if i % 2 == 0 else "Loves me not"
        result.append(phrase)
    result[-1] = result[-1].upper()
    return ", ".join(result)

# An example to test
Loves_me_game(7)




