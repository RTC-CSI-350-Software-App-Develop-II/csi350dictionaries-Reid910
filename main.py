push_ups = {
    "exercise":"Push-ups",
    "sets": 3,
    "reps": 15,
    "notes": "Keep your back straight, hands shoulder-width apart."
}

for x in push_ups:
    print(x)

# Update the sets of the exercise
push_ups["sets"] = 5

# Delete notes with del
del push_ups["notes"]

#Add the key back aw workout_notes with the same value that notes had
push_ups["workout_notes"] ="Keep your back straight, hands shoulder-width apart."

print(push_ups)

workout_plan = {
    "Push-ups": {
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder-width apart."
    },
    "Squats": {
        "sets": 4,
        "reps": 12,
        "notes": "Go as low as you can while maintaining proper form."
    },
    "Plank": {
        "sets": 3,
        "reps": "Hold for 60 seconds",
        "notes": "Engage your core and keep your body in a straight line."
    },
    "Lunges": {
        "sets": 3,
        "reps": 10,
        "notes": "Each leg. Step forward and lower your body until your front knee is at a 90-degree angle."
    },
    "Bicep Curls": {
        "sets": 3,
        "reps": 12,
        "notes": "Use dumbbells, keep your elbows close to your body."
    }
}

print(workout_plan["Lunges"]["notes"])

# Iterating over a dictionary
# The .items() method converts the dictionary into an iterable collection of key-value pairs (tuples).
# Each tuple contains the key as the first element and the value as the second.
# We can use a for loop to access both the key and value.

for key, value in push_ups.items():
    print(f"{key.upper()}: {value}")
