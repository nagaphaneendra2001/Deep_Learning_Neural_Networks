#print grades based on user input
score = int(input("enter the grade score :"))
if (score > 90) & (score <=100):
  print("A grade")
elif (score > 80) & (score <= 90):
  print("B grade")
elif (score > 70) & (score <= 80):
  print("C grade")
elif (score > 60) & (score <= 70):
  print("D grade")
else:
  print("Fail")
