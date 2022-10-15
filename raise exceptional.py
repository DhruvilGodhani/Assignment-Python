try:
    x=int(input("Enter a age upto 18:"))
    if x>18:
        raise ValueError(x)
except ValueError:
    print(x,"is out of allowed range")
else:
    print(x,"is within the allowed range")