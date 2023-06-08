num=int(input("Enter a number: "))
x=0
y=1
for i in range(1, 11):
    while y<=10:
        x=num*y
        y+=1
        
print(x)