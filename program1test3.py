a=int(input("enter the marks in maths"))
b=int(input("enter the marks in social"))
c=int(input("enter the marks in physics"))
d=int(input("enter the marks in english"))
e=int(input("enter the marks in telugu"))
total=a+b+c+d+e
avg=total/5
if(avg>=91 and avg==100):
    print("Grade is A1")
elif(avg>=81 and avg<=90):
    print("Grade is A2")
elif(avg>=71 and avg<=80):
    print("Grade is B1")
elif(avg>=61 and avg<=70):
    print("Grade is B2")
elif(avg>=51 and avg<=60):
    print("Grade is C1")
elif(avg>=41 and avg<=50):
    print("Grade is C2")
elif(avg>=33 and avg<=40):
    print("Grade is D")
else:
    print("Grade is E")
    
    
    
