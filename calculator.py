x=int(input("enter your first number "))
y=input("enter operation")
z=int(input("enter second number"))
if y=="+":
    result=x+z
    print(f"{x} + {z}={result}")
if y=="-":
    result=x-z
    print(f"{x} - {z}={result}")
if y=="/":
    result=x/z
    print(f"{x} / {z}={result}")
if y=="*":
    result=x*z
    print(f"{x} * {z}={result}")
if y=="%":
    result=x%z
    print(f"{x} % {z}={result}")
else:
    print("finished")
