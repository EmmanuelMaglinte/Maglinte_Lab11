Words = []
Your_Words = []

print("Place Words!-")
for x in range (1, 11):
    word = str(input(f"Word {x}:"))
    Words.append(word)
    
MinWordLength = int(input("Number of words you want?: "))
for item in Words:
    if len(item) >= MinWordLength:
     Your_Words.append(item) 
   
print(f"Your Words: {Your_Words}")
