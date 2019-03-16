grade = 59;
if grade >= 60 and grade < 101:
    print("及格");
elif grade >= 0 and grade < 60:
    print("不及格");
else:
    print("error");

A=input("Please Input Here");
if A=="Left" or A == "Lift Site":
    print("You Won");
elif A == "Right" or A == "Right Site":
    print("You Lost");
else:
    print("Over");