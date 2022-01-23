my_list = [10, 20, 30, 40]

print(type(my_list))

print(my_list[1])  # List has index

my_list.append(20)  # can have duplicate value
print(my_list)

my_list.remove(20)
print(my_list)

# set does not allow index to access element. only use for loop to access the elements of sets.

my_set = {"Jan", "Feb", "Mar"}

print(my_set)

my_set.add("april")  # set is not ordered, so no fix order.
print(my_set)

my_set.remove("Mar")

print(my_set, "\n")


