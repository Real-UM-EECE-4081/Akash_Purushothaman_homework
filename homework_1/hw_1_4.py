#4
list_ = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Enter a number between 1-10: "))
new_list = [item for item in list_ if item > num]
print("New List:", new_list)
