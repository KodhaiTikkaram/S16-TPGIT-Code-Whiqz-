a=int(input("Total classes:"))
b=int(input("Classes Attended:"))
x=(b/a)*100
print("Attendence Percentage:",x)
if(x>=75):
    print("Status:Eligible")
    print("Additional Classes Required:0")
else:
    print("Status:Not Eligible")
    n=((75/100)*a)-b
    print("Additional Classes Required:",n)