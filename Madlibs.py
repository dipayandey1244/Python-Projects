
# youtube = 'as'
# print(f'sub to {youtube}')
# print('sub to {} '.format(youtube))


    
# Prompt the user for various types of words
name = input("Enter a name: ")
verb1 = input("Enter a verb (present tense): ")
noun1 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
adverb1 = input("Enter an adverb: ")
verb2 = input("Enter another verb (present tense): ")
noun2 = input("Enter another noun: ")
adjective2 = input("Enter another adjective: ")

# Create the story template with placeholders for the user's input
story = f"\nOnce upon a time, there was a person named {name}. {name} was known for their {adjective1} {noun1}. " \
        f"One day, {name} decided to {verb1} {adverb1} to the {noun2}. " \
        f"At the {noun2}, {name} encountered a {adjective2} {noun2}. " \
        f"The {noun2} challenged {name} to a {verb2} contest. " \
        f"{name} accepted the challenge and {verb2}ed as {adverb1} as possible. " \
        f"After a fierce competition, {name} emerged victorious and became the {adjective1} {noun1} {verb2}er in the land."

# Print out the completed Madlibs story with formatting
print("\nHere's your Madlibs story:\n")
print("----------------------------------------------------")
print(story)
print("----------------------------------------------------")

# Call the function to play the Madlibs game
madlibs()