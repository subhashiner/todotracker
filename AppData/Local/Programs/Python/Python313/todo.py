def add_task(title):
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    print(f"Task '{title}' added.")
def start_task(task_id):
    start_time = datetime.now().isoformat()
    cursor.execute("UPDATE tasks SET start_time = ? WHERE id = ?", (start_time, task_id))
    conn.commit()
    print(f"Started task {task_id} at {start_time}.")

def stop_task(task_id):
    end_time = datetime.now().isoformat()
    cursor.execute("UPDATE tasks SET end_time = ? WHERE id = ?", (end_time, task_id))
    conn.commit()
    print(f"Stopped task {task_id} at {end_time}.")
def calculate_time_spent(task_id):
    cursor.execute("SELECT start_time, end_time FROM tasks WHERE id = ?", (task_id,))
    result = cursor.fetchone()
    if result and result[0] and result[1]:
        start_time = datetime.fromisoformat(result[0])
        end_time = datetime.fromisoformat(result[1])
        time_spent = (end_time - start_time).total_seconds() / 60  # time in minutes
        print(f"Time spent on task {task_id}: {time_spent:.2f} minutes.")
    else:
        print("Task has not been completed yet.")
def view_tasks():
    cursor.execute("SELECT id, title, is_complete FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        status = "Complete" if task[2] else "Incomplete"
        print(f"{task[0]}. {task[1]} - {status}")
def main():
    while True:
        print("\nTo-Do List & Productivity Tracker")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Start Task")
        print("4. Stop Task")
        print("5. Calculate Time Spent")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '3':
            task_id = int(input("Enter task ID to start: "))
            start_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to stop: "))
            stop_task(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to calculate time: "))
            calculate_time_spent(task_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")

    conn.close()

if __name__ == "__main__":
    main()
