def get_user_response(prompt):
    """Helper function to get valid user response (Y/N)."""
    while True:
        response = input(prompt + " ").strip().upper()
        if response in ['Y', 'N']:
            return response
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

def routine_check():
    """Main function to check the user's daily routine."""
    routine_items = [
        "Did you go for a run at 7 AM?",
        "Did you have breakfast?",
        "Did you read for 30 minutes?",
        "Did you do your homework?",
        "Did you exercise in the evening?",
        "Did you prepare for tomorrow's class?"
    ]

    responses = {}
    completed_count = 0
    missed_count = 0

    # Collect responses from the user
    for item in routine_items:
        response = get_user_response(item)
        responses[item] = response
        
        # Count completed and missed tasks
        if response == 'Y':
            completed_count += 1
        else:
            missed_count += 1

    # Print summary
    print("\n--- Routine Summary ---")
    for item, response in responses.items():
        status = "Completed" if response == "Y" else "Not Completed"
        print(f"{item}: {status}")

    print("\n--- Overall Summary ---")
    print(f"Total Completed: {completed_count}")
    print(f"Total Missed: {missed_count}")

if __name__ == "__main__":
    routine_check()
