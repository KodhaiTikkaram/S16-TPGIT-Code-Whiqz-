n=int(input("Enter the Students:"))
for i in range(1,n+1):
    name=input("\n")
    department=input("\n")
    print(name,department)
    print("Seat",i,"-",name,"(",department,")")
