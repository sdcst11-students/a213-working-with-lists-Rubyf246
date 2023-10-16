#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
people = ['kimmy', 'ruby', "swagrid", "chelsea", "sarah"]
replace= input("Give my the name you want to replace:")
Add= input(f"Who do you want to replace {replace}?")
Index= people.index(replace)
people.remove (replace)
people.insert(Index, Add)
print(people)