n = "my name is Darshan Bakshi"

print(n)


types_of_people = 10
x = f"there are {types_of_people} types of people"

binary = "binary"
do_not = "don't"

y = f"people who know {binary} and who {do_not}"

print(x)
print(y)

print(f"i said {x}")
print(f"i said '{y}'")

hilarious = "false"
joke_evaluation = "isn't that a funny joke {}" # {} is important to let the formatter know that next variable is to be considered

print(joke_evaluation.format(hilarious))

w="a"
u="b"

print(w+u)

print(f" {w}w" * 10)
print(w *10)
