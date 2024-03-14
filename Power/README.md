# Power
I started the project by copy and pasting the template into my python file. I first typed in "return x ** n" under the get_power def to make sure x (number) is being raised by the exponent n. I saw there was still an error in the file for "def print_graph(n)" and the for statement. Aftering five minutes of concentrated thinking, I realized they went together. I pushed "def get_power" and its return to start at line one and put "def print_graph(n)" on top of the for statement. I also indented the for statement. From here, it was 10:10am on Thursday, and I had a class at 11, so time was running out on figuring out this part of the script. I asked my cs grad roommate (her name is Christina) for help. Christina told me that "n" represents the number of asterisks in each line. This information led to me creating this:

    def print_graph(n):
        for i in range(-8, 9):
            x = i
            y = get_power(x, 2)

This sets up the equation y = x^2. After that, I needed to figure out how to print the graph. So, I started with this:

    for i in range(-8, 9):
        x = i
        y = get_power(x, 2)
        if y > 0:
            print('*' * (n * y))
        else: 
            print('*')
print_graph(1)

Which printed:

\****************************************************************

\*************************************************

\************************************

\*************************

\****************

\*********

\****

\*

\*

\*

\****

\*********

\****************

\*************************

\************************************

\*************************************************

\****************************************************************

I needed to get rid of the asterisk in the middle of the graph where y=0 to match the graph in the homework assignment. I also realized the last else statement was redundant because it's an exponential equation, and there would be no negative values (but it would've been good to add if I wanted to check for negative numbers in case anything was going wrong in my script). I set up an elif statement for when y=0 that looks like this:

    def get_power(x, n):
        return x ** n

    def print_graph(n):
        for i in range(-8, 9):
            x = i
            y = get_power(x, 2)
            if y > 0:
                print('*' * (n * y))
            elif y == 0:
                print('' * n)
    print_graph(1)

Which printed a result identical to the graph in the homework assignment.