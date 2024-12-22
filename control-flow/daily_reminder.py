# Prompt user for task details
task = input("Enter the task description: ")
task_priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Validate inputs
if task_priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter high, medium, or low.")
elif time_bound not in ["yes", "no"]:
    print("Invalid time sensitivity. Please enter yes or no.")
else:
    # Process the task based on priority
    match task_priority:
        case "high":
            reminder = f"The task '{task}' is a high-priority task."
        case "medium":
            reminder = f"The task '{task}' is a medium-priority task."
        case "low":
            reminder = f"The task '{task}' is a low-priority task."

    # Add time-sensitivity to the reminde
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"

    # Print the customized reminder
    print(reminder)
