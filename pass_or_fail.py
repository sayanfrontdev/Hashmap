sub1=int(input("Enter first subject marks : "))
sub2=int(input("Enter second subject marks : "))
sub3=int(input("Enter third subject marks : "))

if(sub1<33, sub2<33, sub3<33):
    print("You are fail because you have less than 33% in one of tha subject")
if(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations! You are passed ")
