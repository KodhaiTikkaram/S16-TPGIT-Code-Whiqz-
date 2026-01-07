x=input("Enter Password:")
a=x.isupper
b=x.islower
c=x.isalnum
e=x.isnumeric
if (len(x)>8 and a)and(b and c and e):
    print("Password Strength:Strong")
elif b or e:
    print("Password Strength:Medium")
else:
    print("Password Strength:Weak")
