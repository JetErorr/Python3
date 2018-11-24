#14.Prompt and Pass
from sys import argv
script, name = argv
print(f"So, subject {name}, what are you in for today?")
problem = input("What problems are you facing?\n>")
print(f"{problem}?, now that's a problem.")
solution = input(f"So what do you think is the solution to {problem}?\n>")
print(f"{solution} you say. Maybe not, we do have better options on the table.")