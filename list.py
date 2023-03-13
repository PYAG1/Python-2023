#lists are like arrays
#you can nest lists

list = [1,[1,2,3,4],5,6]


#you can add the keyword 'sep='''to separate the list items


#we can add by using insert but insert takes two parameters the first is like the index and the second is the value you want to add
#you can use .append 
#.extend([9,6,7,5]) adds an array of values
list.insert(len(list),50)

list.pop(1) #pop you mention the index

print(list)

for i in list:
    print('hi',i)
#we use brackets
##########################################################################



my_tuple = (1,3,True)
print(my_tuple.count('int'))
#.count shows the number of occurence of a value

