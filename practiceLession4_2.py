#Write a program that assigns a grade based on a score input (90+ for A, 75-89 for B, below 75 for C).
mark=89
if mark>=90:
    print("The grade is A")
elif mark>=75 & mark<=89:
    print("The grade is B")
else:
    print("The grade is C")