#for loop for range 10
for i in range(10):
  print(i)
print()

#for loop for range (5, 30)
for i in range(5, 30):
  print(i)
print()

#set int k to 10
k = 10
#for loop for range 10
#print k+1
for i in range(k):
  k+1
  print(k)
print()

#assign variables
leftBorder = input("What should the left border be?")
rightBorder = input("What should the right border be?")
inner = input("What should the inner character be?")
name = input("What is your name?")
length = input("How long should the drawing be?")

#build the drawing
for i in range (length):
  print