#First factorial
import math
digits = math.factorial(1)
print(digits)

#Consonant count
vowels = "aeiouAEIOU"
# sentence = "All cows eat grass"
sentence = "Today is a really hot day but will cool down later"
string = sentence.replace(" ", "")

vowelCount = 0
consonantCount = 0

for i in string:
    if(i in vowels):
        vowelCount += 1
    else:
        consonantCount += 1

print(consonantCount)

#Hamming distance
words = ["11001101", "10110110"]
first_word = words[0]
second_word = words[1]
i=0
difference_count = 0

while i < len(first_word):
    if second_word[i] != first_word[i]:
        difference_count = difference_count + 1
    i = i + 1
print(difference_count, 'positions.')