def grade(scores):
    total = 0
    for score in scores:
        if(score.isdigit() and 0<=int(score)<=100):
            num = int(score)
            total+=num
            if(num>=90):
                print(f"{num}: A")
            elif(num>=80):
                print(f"{num}:B")
            elif(num>=70):
                print(f"{num}:C")
            elif(num>=60):
                print(f"{num}:D")
            else:
                print(f"{num}:F")
        else:
            print(f"{score}:Invalid score")
    
n = int(input("Enter a number "))
scores = []
for i in range(1,n+1):
    score = input(f"Enter score {i}:")
    scores.append(score)
grade(scores)
