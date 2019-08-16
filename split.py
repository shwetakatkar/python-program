my_str=input("enter the string")
str=my_str.casefold()
words=str.split()
words.sort()
for word in words:
    print(word)
