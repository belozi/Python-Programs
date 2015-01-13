s= "everybody"
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for x in s.lower():
    for y in vowels:
        if x == y:
            count += 1
  
print("Number of vowels: " + str(count))
