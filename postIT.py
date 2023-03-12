from tkinter import *
from tkinter.ttk import Button, Label

# Define the PostApp class
class PostApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Post App")
        self.pack()
        self.posts = {}
        self.create_widgets()

    def create_widgets(self):
        # Create the post entry widget
        self.post_entry = Entry(self)
        self.post_entry.pack()

        # Create the post button
        self.post_button = Button(self, text="Post", command=self.post)
        self.post_button.pack()

        # Create the posts listbox
        self.posts_listbox = Listbox(self)
        self.posts_listbox.pack()

        # Create the like button
        self.like_button = Button(self, text="Like", command=self.like)
        self.like_button.pack()

        # Populate the posts listbox
        self.populate_posts_listbox()

    def post(self):
        # Get the text of the post
        text = self.post_entry.get()

        # Insert the post into the dictionary
        id = len(self.posts) + 1
        self.posts[id] = {'text': text, 'likes': 0}

        # Clear the post entry widget
        self.post_entry.delete(0, END)

        # Update the posts listbox
        self.populate_posts_listbox()

    def like(self):
        # Get the id of the selected post
        selection = self.posts_listbox.curselection()
        if len(selection) == 0:
            return
        id = int(self.posts_listbox.get(selection[0]).split(':')[0])

        # Increment the likes count in the dictionary
        self.posts[id]['likes'] += 1

        # Update the posts listbox
        self.populate_posts_listbox()

    def populate_posts_listbox(self):
        # Clear the posts listbox
        self.posts_listbox.delete(0, END)

        # Populate the posts listbox
        for id, post in self.posts.items():
            text = post['text']
            likes = post['likes']
            self.posts_listbox.insert(END, f"{id}: {text} (likes: {likes})")

# Create the Tkinter window and start the app
root = Tk()
app = PostApp(master=root)
app.mainloop()
