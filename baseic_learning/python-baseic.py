# learning = "list"
my_list = ["one","two","three",]
print(my_list[2])
  
# learning = "append"  
my_list.append("four")
print(my_list)

#learning  = "set"

my_set = {"red","blue","yellow","brown","gray"}
print(my_set)
my_set.add("color")
print(list(my_set))
for element in my_set:
    print(element)


titi = [my_set]
print(titi)
titi.append("rad")
print(titi)
print(titi[0])
print(titi[1])
#print(titi[2])
for element in titi:
    print(element)

#using = "append,set and list"
my_list.append("one")
print(my_list)
print(set(my_list))

# learning = "remove"
my_list.remove("one")
print(my_list)
my_set.remove("gray")
print(my_set)
titi.remove(my_set)
print(titi)