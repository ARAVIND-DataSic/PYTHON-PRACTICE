a=int(input("mark of subject 1:"))
b=int(input("mark of subject 2:"))
c=int(input("mark of subject 3:"))
d=int(input("mark of subject 4:"))
e=int(input("mark of subject 5:"))
f=(a+b+c+d+e)/5
if(f<35):
    print("additional class is required")
else:
    print("you are good to go")
