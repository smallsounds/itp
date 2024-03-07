count = 0
while (count < 3): 	
  count += 1
  print("Happy Thursday")

# While is a type of loop
  
count = 0
while (count < 3): 	
  count = count + 1
  print("Happy Thursday")
else:
  print("Happy Friday")

# While loops until untrue and then bumps down to line 12 (the "else" statement)
  

# FOR Starts at 0 and goes up by one by default, range can only be an integer
for i in range(128):
  print(f"The next MIDI note value is {i}")

# Increment by 2 instead; 0 is lowest number, 128 is the highest number, 2 is the value that it increases by
for i in range(0, 128, 2):
  print(f"The next MIDI note value is {i}")

# If you want to decrease, make the first number the highest number, second number the lowest number, and the third number a negative integer



# %7 means fully divisible by 7
for index in range(1500, 2701, 1):
  if index % 7 == 0 and index % 5 == 0:
    print(index)



# both i and j are counters and if j is equal to or greater than i, then you print j and end the line. i is vertical and j is horizontal.
for i in range(10):
  for j in range(10):
    if j >= i:
      print(j, end='')
  print()



# good recursion
def factorial(n):
  if n <= 1:
    return 1
  else:
    result = factorial(n-1)
    return n*result
factorial(5)


# In Processing, the top left corner is 0 for x,y,z axis