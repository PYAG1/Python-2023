menu = ["apple","pear","banana","her", " there"]

def findcoffe(pear):
    if pear[0] == 'c':
        return pear

map_coffee = map(findcoffe,menu)
print(map_coffee)
for x in map_coffee:
    print(x)