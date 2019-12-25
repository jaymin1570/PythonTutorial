age = int(input("please input your age:"))
if age <= 0:
    print("invalid age")
elif 0<age<=3:
    print("ticket price: Free")
elif 3<age<=10:
    print("Ticket price : 150")
elif 10<age<=60:
    print("Ticket price : 250")
else:
    print("Ticket price : 350")