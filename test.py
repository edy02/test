
#test slovniku listu

list_of_lists=[[221,225],[121,122],[546,646],[646,648]]

print list_of_lists
list_of_lists.pop()

print list_of_lists

list_of_lists.append([354,643])
print list_of_lists

list_of_lists.insert(0,[1,3])
list_of_lists.pop()
print list_of_lists

new_list=[list_of_lists[0][0]+10, list_of_lists[0][1]]
print new_list

print "mazani"
list_of_lists.insert(0, new_list)
list_of_lists.remove(list_of_lists[2])
list_of_lists.pop()
print list_of_lists

print "tisk"
for coord in list_of_lists:
    print coord[0]
