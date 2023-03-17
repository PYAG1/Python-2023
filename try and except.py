items = [1,2,3,4,5]
try:
    item = items[6]
except Exception as e:
    print(e,"you are wrong")

##question 2
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 20)
    print(ans)
except Exception as e:
    print(e,'you are wrong')


##question 3
with open('file_does_not_exist.txt', 'r') as file:
    try:
        print(file.read())
    except Exception as e:
        print(e,'error bro')
