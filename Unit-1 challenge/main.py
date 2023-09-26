def rec_fact(x):
  if x == 1:

    return 1
  else:
    return (x * rec_fact(x - 1))
num = int(input("Enter a number: "))
if num >= 1:
  print("The factorial of ", num, "is", rec_fact(num))