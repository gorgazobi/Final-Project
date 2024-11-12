# Habit class
class Habit:
    def __init__(self, name, frequency):
        self.name = name  # Name of the habit (e.g., "Exercise")
        self.frequency = frequency  # Daily, Weekly, etc.
        self.streak = 0  # Keeps track of consecutive completions

    def complete_habit(self):
        """Marks the habit as complete for the day and updates streak."""
        self.streak += 1
        print(f"{self.name} completed! Current streak: {self.streak}")

    def reset_streak(self):
        """Resets streak to 0 if the habit is missed."""
        self.streak = 0
        print(f"{self.name} streak reset.")


# HabitTracker class
class HabitTracker:
    def __init__(self):
        self.habits = []  # List to store all habits

    def add_habit(self, name, frequency):
        """Adds a new habit to the tracker."""
        habit = Habit(name, frequency)
        self.habits.append(habit)
        print(f"Habit '{name}' added with frequency '{frequency}'.")

    def mark_habit_complete(self, name):
        """Marks a specific habit as complete."""
        for habit in self.habits:
            if habit.name == name:
                habit.complete_habit()
                return
        print(f"Habit '{name}' not found.")

    def show_progress(self):
        """Displays all habits and their current streaks."""
        for habit in self.habits:
            print(f"Habit: {habit.name}, Streak: {habit.streak}")

# Example usage:
if __name__ == "__main__":
    tracker = HabitTracker()
    tracker.add_habit("Exercise", "Daily")
    tracker.add_habit("Read", "Weekly")
    tracker.mark_habit_complete("Exercise")
    tracker.show_progress()
