# Fizzbuzz
I started with the Fizzbuzz homework. I took the range and nesting example and used that to create:
index in range(1, 101, 1):
    if index % 5 and index % 3:
        print("fizzbuzz")
    elif index % 5:
        print("buzz")    
    elif index % 3:
        print("fizz")
    print(index)

As I was doing this, Ghibbi asked me for help, and I helped them as I was figuring it out myself. We had pretty similar code already, so that helped. So far, my code made all the text turn into "fizz" and "buzz." The only output that wasn't "fizz" or "buzz" was 100. I realized I didn't copy a part of the example which was the "== 0" after the "index % {number}." I put that into the script and then it printed the the fizzes and buzzes and fizzbuzzes correctly-ish. I was getting this result:
1
2
fizzbuzz
3
4
buzz
5
fizzbuzz

I realized that "print(index)" wasn't taking into account the fizzes and buzzes. I added it to the whole nest by making it an "else" conditional (else: print(index)). This fixed the issue.

# Pyramid
I started the pyramid with "stacks = int(input("How big do you want the pyramid? Pick a number 1-8"))" to create a place for users to type their number of choice in. I then created "if stacks == 0 or stacks = >= 9 print("\nUh... I don't think that was in the range\n")" which notifies the user that the number they entered wasn't within the range given to them. 

I added the actual pyramid part next. I used the example in the homework markdown file to set up the framework for the pyramid. I just wanted to make sure the conditional I used (elif) worked, so I ran the program. I tested the numbers 9 and 7 to see what the program prints and fortunately, both worked as intended at that moment. I realized I should've used the code from the README example rather than the one on the homework file, so I copy and pasted that example under the elif. I tested different values to flip the pyramid around and ended with this:

for i in range(9):
    for j in range(9):
        if j >= 9 - i: 
            print("#", end='')
        else:
            print(' ', end='')
    print()

The "j >= 9 - i:" flips the triangle 180 degrees on the horizontal axis, and the "else: print('', end='')" flips it on the vertical axis. But now, I needed to integrate the stacks variable. I tried plugging in "stacks" in the i and j ranges, but it printed:
                       #      ##     ###    ####   #####  ######

My CS grad roommate was in the apartment as I was working on this, so I asked her for help. She told me my i range was correct, but everything else needed to change. Because the range is being determined in the elif statement, I didn't need the "if j >= 9 - i:" conditional. I replaced the j range with "for j in range(stacks - i - 1): print(" ", end='')" which takes care of the spaces that create the slant in the pyramid. My roommate told me that I need an additional line that includes "print("#", end='')" as well as another variable. She gave me 10-15mins or so to figure it out myself. I started with "for k in range(i): print("#", end='')." The pyramid was one row lower than the integer entered, so I added one to the range. This solved that issue, and the pyramid printed correctly!