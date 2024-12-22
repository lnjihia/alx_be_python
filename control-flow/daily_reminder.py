# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes or no): ").lower()

# Process the task and provide a customized reminder
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority level entered. Please specify high, medium, or low."

# Modify the reminder if the task is time-bound
if time_bound == "yes" and priority in {"high", "medium", "low"}:
    reminder += " that requires immediate attention today!"
elif time_bound == "no" and priority in {"high", "medium", "low"}:
    reminder += " Consider completing it at your convenience."

# Display the final reminder
print("\nReminder:")
print(reminder)