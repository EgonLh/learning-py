a = 1;
b = 0;

print("AND")
c = a and b
print(a and b)
print("C",c)

print("\nOR")
c = bool(a or b)
print(a or b)
print("C",c)


alpha = ["A","B","C","D"]

if "A" in alpha:
    print("Couldn't get lawyers")
elif "B" in alpha:
    print("Nothing ...")
else:
    print("Just loggin it")



for a in alpha:
    if "C"==a:
        print("Obtained :",a)
        break
    print(a)