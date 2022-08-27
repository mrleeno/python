#List Comprehension

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

nums = [i*2 for i in range(10)]
print(nums)

word = input()
vowels = ["a","e","i","o","u"]

listc = [i for i in word if i not in vowels]
print(listc)