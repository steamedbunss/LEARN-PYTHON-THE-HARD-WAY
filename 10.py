tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat"

# \\ prints a single \
# """/''' prints strings with multiple lines

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

#SHOULD SEE

	I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat

I'll do a list:
		* Cat food
		*Fishies
		*Catnip
		*Grass