class DailyRoutine:
    """Class to handle daily routine check."""
    
    def __init__(self):
        """Initialize the DailyRoutine instance."""
        self.routine_items = [
            "Did you go for a run at 7 AM?",
            "Did you have breakfast?",
            "Did you read for 30 minutes?",
            "Did you do your homework?",
            "Did you exercise in the evening?",
            "Did you prepare for tomorrow's class?"
        ]
        self.responses = {}
        self.completed_count = 0
        self.missed_count = 0
    
    def get_user_response(self, prompt):
        """Helper method to get valid user response (Y/N)."""
        while True:
            response = input(prompt + " ").strip().upper()
            if response in ['Y', 'N']:
                return response
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
    
    def check_routine(self):
        """Method to check the user's daily routine."""
        for item in self.routine_items:
            response = self.get_user_response(item)
            self.responses[item] = response
            
            # Count completed and missed tasks
            if response == 'Y':
                self.completed_count += 1
            else:
                self.missed_count += 1
    
    def print_summary(self):
        """Method to print the summary of the routine check."""
        print("\n--- Routine Summary ---")
        for item, response in self.responses.items():
            status = "Completed" if response == "Y" else "Not Completed"
            print(f"{item}: {status}")

        print("\n--- Overall Summary ---")
        print(f"Total Completed: {self.completed_count}")
        print(f"Total Missed: {self.missed_count}")

def display_welcome_message():
    """Function to display a welcome message before starting the routine check."""
    print("Welcome to the Daily Routine Check Program!\nLet's see how well you're sticking to your routine.")

def main():
    """Main function to run the routine check."""
    display_welcome_message()
    
    # Create an instance of the DailyRoutine class
    routine = DailyRoutine()
    
    # Perform the routine check
    routine.check_routine()
    
    # Print the routine summary
    routine.print_summary()

if __name__ == "__main__":
    main()

