a=int(input("Enter the total items:"));
for i in range(a):
    item=input()
    price=int(input())
    quantity=int(input())
    print(item,price,quantity)
    x=quantity*price
    print(item,quantity,"*",price,"=",x)
for y in range(a):
    y=y+x
print("Total Amount:",y)
s=y/10
print("Discount",s)
r=y-s
print("Final Amount",r)
