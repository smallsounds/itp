stacks = int(input("How big do you want the pyramid? Pick a number 1-8"))
if stacks == 0 or stacks >= 9:
    print("Uh... I don't think that was in the range", end="")
elif stacks >= 1 and stacks <= 8:
    for i in range(stacks):
        for j in range(stacks - i - 1):
            print(" ", end='')
        for k in range(i + 1):
            print("#", end='')
        print()