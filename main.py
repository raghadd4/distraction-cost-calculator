# This program collects user input and calculates a weighted distraction cost
# based on task importance and time wasted.

# Collects user input for one distraction, calculates its cost,
# and returns the data as a dictionary
def get_distraction(): 
    name = input("Task name: ")

    while True:
        try:
            importance = int(input("Importance (1–5): "))
            if not 1 <= importance <= 5:
                raise ValueError
            break
        except ValueError:
            print("Importance must be an integer between 1 and 5.")

    while True:
        try:
            time = int(input("Time wasted (minutes): "))
            if not time >= 0:
                raise ValueError
            break
        except ValueError:
            print("Time wasted must be at least 0 or more")  


    cost = importance * time

    return {
        "name": name,
        "importance": importance,
        "time": time,
        "cost": cost
    }

# Stores all distraction records as dictionaries in a list
distractions = []

count = 0

# Repeatedly collects distractions until the user chooses to stop
while True:
    distraction = get_distraction()
    distractions.append(distraction)
    count += 1

# 'a' mode appends new data to the file without overwriting existing content
    with open("data.txt", "a") as file:
       file.write(
        f"{distraction['name']},"
        f"{distraction['importance']},"
        f"{distraction['time']},"
        f"{distraction['cost']}\n"
       )


    choice = input("Add another distraction? (y/n): ").lower()
    if choice != "y":
        break


print("\n--- Distraction Impact Summary ---")

print("You entered " + str(count) + " distractions")

total_cost = 0

# Iterates through each stored distraction to calculate the total cost
for d in distractions:
    total_cost += d["cost"]

print(f"Total Distraction Cost: {total_cost}")


average_cost = total_cost / len(distractions)
print(f"Average Distraction Cost: {average_cost}")

# finds the distraction with the highest impact score
most_costly = max(distractions, key=lambda d: d["cost"])
print(f"Most costly distraction: {most_costly['name']} (Cost: {most_costly['cost']})")

