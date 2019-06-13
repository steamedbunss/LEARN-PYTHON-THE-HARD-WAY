print("How old are you?",)
age = input()
print("How tall are you?"),
height = input()
print("How much do you weigh?"),
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))


#SHOULD SEE
How old are you? 21 years
How tall are you? 5'11"
How much do you weigh? 73 lbs
So, you're '21 years' old, '5\'11"' tall and '73 lbs' heavy.

#raw_input() is python2
#input() is python3