# Collects user input for one distraction, calculates its cost,
# and returns the data as a dictionary
def get_distraction():
    name = input("Task name: ")
    importance = int(input("Importance (1–5): "))
    time = int(input("Time wasted (minutes): "))

    cost = importance * time

    return {
        "name": name,
        "importance": importance,
        "time": time,
        "cost": cost
    }

# Stores all distraction records as dictionaries in a list
distractions = []

# Repeatedly collects distractions until the user chooses to stop
while True:
    distraction = get_distraction()
    distractions.append(distraction)

    choice = input("Add another distraction? (y/n): ").lower()
    if choice != "y":
        break


print("\n--- Distraction Impact Summary ---")

for d in distractions:
    print(f"{d['name']} → Cost Score: {d['cost']}")

total_cost = 0

# Iterates through each stored distraction to calculate the total cost
for d in distractions:
    total_cost += d["cost"]

print(f"\nTotal Distraction Cost: {total_cost}")

# finds the distraction with the highest impact score
most_costly = max(distractions, key=lambda d: d["cost"])
print(f"\nMost costly distraction: {most_costly['name']} (Cost: {most_costly['cost']})")


