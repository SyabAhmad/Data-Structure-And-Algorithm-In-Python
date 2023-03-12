from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Button

class SnippetApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Snippet App")
        self.master.geometry("400x400")

        # Create a text widget for displaying snippets
        self.snippet_text = ScrolledText(self.master, width=40, height=10)
        self.snippet_text.pack(pady=10)

        # Create a button for uploading snippets
        self.upload_button = Button(self.master, text="Upload Snippet", command=self.upload_snippet)
        self.upload_button.pack(pady=5)

        # Create a dictionary for storing snippets and their likes
        self.snippets = {}

    def upload_snippet(self):
        # Create a file dialog for selecting a file
        file_path = filedialog.askopenfilename(initialdir=".", title="Select a file",
                                               filetypes=(("Python files", "*.py"), ("Text files", "*.txt")))

        if not file_path:
            messagebox.showerror("Error", "No file selected.")
            return

        try:
            # Read the contents of the file and add it to the snippets dictionary
            with open(file_path, "r") as f:
                content = f.read()
                self.snippets[content] = 0
                self.snippet_text.insert(END, content + "\n\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = Tk()
app = SnippetApp(master=root)
app.mainloop()
