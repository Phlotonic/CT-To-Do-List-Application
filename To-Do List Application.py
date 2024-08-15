# Define a class for the To-Do List application
class ToDoListApp:
    def __init__(self):
        # Initialize the To-Do List application with an empty list of tasks
        self.tasks = []

    def display_menu(self):
        """Display the main menu of the application."""
        # Print the welcome message and menu options
        print("\nWelcome to the To-Do List App!")
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")

    def add_task(self):
        """Add a new task to the list."""
        # Prompt the user to enter the task title
        title = input("Enter the task title: ")
        # Add the new task to the list with a status of "Incomplete"
        self.tasks.append({"title": title, "status": "Incomplete"})
        # Confirm that the task has been added
        print(f"Task '{title}' added.")

    def view_tasks(self):
        """View all tasks in the list."""
        # Check if there are no tasks in the list
        if not self.tasks:
            print("No tasks available.")
        else:
            # Iterate through the tasks and print each one with its status
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task['title']} - {task['status']}")

    def mark_task_complete(self):
        """Mark a task as complete."""
        # Display the list of tasks
        self.view_tasks()
        try:
            # Prompt the user to enter the task number to mark as complete
            task_num = int(input("Enter the task number to mark as complete: "))
            # Check if the task number is valid
            if 1 <= task_num <= len(self.tasks):
                # Mark the selected task as complete
                self.tasks[task_num - 1]["status"] = "Complete"
                # Confirm that the task has been marked as complete
                print(f"Task '{self.tasks[task_num - 1]['title']}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        """Delete a task from the list."""
        # Display the list of tasks
        self.view_tasks()
        try:
            # Prompt the user to enter the task number to delete
            task_num = int(input("Enter the task number to delete: "))
            # Check if the task number is valid
            if 1 <= task_num <= len(self.tasks):
                # Remove the selected task from the list
                removed_task = self.tasks.pop(task_num - 1)
                # Confirm that the task has been deleted
                print(f"Task '{removed_task['title']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def quit_app(self):
        """Quit the application."""
        # Print a goodbye message and exit the application
        print("Quitting the application. Goodbye!")
        exit()

    def run(self):
        """Run the main loop of the application."""
        while True:
            # Display the main menu
            self.display_menu()
            try:
                # Prompt the user to select an option from the menu
                choice = int(input("Select an option: "))
                # Execute the corresponding method based on the user's choice
                if choice == 1:
                    self.add_task()
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    self.mark_task_complete()
                elif choice == 4:
                    self.delete_task()
                elif choice == 5:
                    self.quit_app()
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Please enter a valid number.")

# Create an instance of the ToDoListApp and run the application
if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
