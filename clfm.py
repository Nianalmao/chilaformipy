from random import*
p= input("even or odd?")
b= int(input("chosse any number between 0 and 10"))
m= randint(0,10)
print(m)
s= int(b+m)
if (s%2==0 and p=="even") or (s%2!=0 and p=="odd"):
    print("congrats you won!")
else:
    print("try again!")