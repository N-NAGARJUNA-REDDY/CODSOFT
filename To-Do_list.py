import tkinter as tk
from tkinter import messagebox

class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.title("To-Do List by Nagarjuna")
        self.geometry("400x300")

        self.label_task = tk.Label(self, text="Enter a task:", font=('Book Antiqua', 15, 'bold'))
        self.label_task.pack(pady=10)

        self.entry_task = tk.Entry(self, width=40)
        self.entry_task.pack()

        self.button_add = tk.Button(self, text="Add Task", command=self.add_task, font=('Book Antiqua', 10, 'bold'), bg = "Grey")
        self.button_add.pack(pady=5)

        self.button_remove = tk.Button(self, text="Remove Task", command=self.remove_task, font=('Book Antiqua', 10, 'bold'), bg = "Grey")
        self.button_remove.pack(pady=5)

        self.listbox_tasks = tk.Listbox(self, height=10, width=50)
        self.listbox_tasks.pack(pady=10)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.listbox_tasks.curselection()
        if selected_index:
            index = selected_index[0]
            self.listbox_tasks.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()