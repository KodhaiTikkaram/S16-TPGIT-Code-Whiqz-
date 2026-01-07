x=input("Enter Password:")
if x.isdigit and x.isupper and x.islower :
    print("Password Strength:Strong")
elif x.isdigit or x.isalpha:
    print("Password Strength:Medium")
else:
    print("Password Strength:Weak")