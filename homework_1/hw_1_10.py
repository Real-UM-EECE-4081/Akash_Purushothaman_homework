#10

filepage = input("Enter python file text:")
file = open(filepage, 'r')
dictionary = dict()

for line in file:
    words = line.split(" ")
    for word in words:
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1

for key in list(dictionary.keys()):
    print("The frequency of", key,"is:", dictionary[key])
