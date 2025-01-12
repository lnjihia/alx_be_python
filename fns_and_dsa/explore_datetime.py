from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompt the user for the number of days to add and calculate the future date.
    """
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)  # Add the specified days
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

def main():
    """
    Main function to execute the tasks.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
