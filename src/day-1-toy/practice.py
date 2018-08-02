list_one = [1, 2, 3, "4", 4, "5", 6]
#copy the list 
list_two = list_one[:]
print(list_two)
# invent the list with a condition
list_two.append()
logic = [i for i in list_two if int(i) % 2 == 0]
print(logic)
