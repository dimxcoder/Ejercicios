H=int(input("Input Hora"))
M=int(input("Input Minutos"))
S=int(input("Input seconds"))

if H <= 23 :
    print("is correct H format")
else :
    print("is not a correct H format")

if M <= 60 :
    print("is correct M format")
else:
    print("is not a correct M format")

if S <= 60 :
    print("is correct S format")
else:
    print("is not a correct S Format")
