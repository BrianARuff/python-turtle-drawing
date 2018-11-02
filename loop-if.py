
num = input("Enter a number to factorize: ")

num = int(num)

for i in range(1, num + 1):
  if(num % i == 0 and i != num and i != 1):
      print("Factor of " + str(num) + " :" + str(i))