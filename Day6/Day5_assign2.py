from random import shuffle
from itertools import groupby

# Input participants
n = int(input("Enter number of participants: "))

participants = []

print("\nEnter participant names:")
for i in range(n):
    name = input(f"Participant {i+1}: ")
    participants.append(name)

# Shuffle names randomly
shuffle(participants)

print("\nShuffled Participants:")
print(participants)

# Divide into 2 teams
mid = (len(participants) + 1) // 2

team1 = participants[:mid]
team2 = participants[mid:]

print("\n--- Team 1 ---")
for member in team1:
    print(member)

print("\n--- Team 2 ---")
for member in team2:
    print(member)

# Group names alphabetically
participants.sort()

print("\n--- Names Grouped Alphabetically ---")

for letter, names in groupby(participants, key=lambda x: x[0].upper()):
    print(letter, ":", list(names))

# Display team with maximum members
print("\n--- Team with Maximum Members ---")

if len(team1) > len(team2):
    print("Team 1 has maximum members.")
    print("Members:", team1)
elif len(team2) > len(team1):
    print("Team 2 has maximum members.")
    print("Members:", team2)
else:
    print("Both teams have equal members.")