from tkinter import *

# Define question dictionary
question = {
    "In which country is the Taj Mahal?": ['New Zealand', 'Italy', 'America', 'India'],
    "Which language is spoken in Australia?": ['English', 'Hindi', 'Spanish', 'Telugu'],
    "How many sides does a hexagon have?": ['8', '6', '9', '7']
}

# Define answer list
ans = ['India', 'English', '6']

current_question = 0
name_entered = False  # To check if the name has been entered

def start_quiz():
    global name_entered
    name = name_entry.get()
    if name.strip() == "":
        name_label.config(text="Please enter your name", fg="#123")  # Change background color to lightgray
    else:
        name_label.config(text=f"Player: {name}", fg="#143", padx=10, pady=10)  # Add padx and pady for space outside the box
        name_entry.forget()
        start_button.forget()
        name_entered = True
        next_button.pack()
        next_question()

def next_question():
    global current_question
    if not name_entered:
        name_label.config(text="Please enter your name", padx=10, pady=10)  # Add padx and pady for space outside the box
        return
    if current_question < len(question):
        # Get key or question that needs to be printed
        check_ans()
        user_ans.set('None')
        c_question = list(question.keys())[current_question]
        # Clear frame to update its content
        clear_frame()
        # Printing question with space
        Label(f1, text=f"Question {current_question + 1}: {c_question}", padx=15, pady=10,
              font="calibre 12 bold", fg="green").pack(anchor=NW)  # Change text color to green
        # Printing options with space
        for option in question[c_question]:
            Radiobutton(f1, text=option, variable=user_ans,
                        value=option, padx=28, pady=5, font="calibre 15", fg="blue",activeforeground="red").pack(anchor=NW)
        current_question += 1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        output = f"   Score: {user_score.get()} out of {len(question)}   "  # Add spaces and change color
        Label(f1, text=output, font="calibre 18 bold", fg="red").pack()  # Change text color to red
        Label(f1, text="Thanks for Participating",
              font="calibre 18 bold", fg="purple").pack()  # Change text color to purple

def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[current_question - 1]:
        user_score.set(user_score.get() + 1)

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

if __name__ == "__main__":
    root = Tk()
    # Setup basic window
    root.title("GFG QUIZ APP")
    root.geometry("850x520")
    root.minsize(800, 400)

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    Label(root, text="Quiz App",
          font="calibre 40 bold",
          relief=SUNKEN, background="violet",
          padx=11, pady=12).pack()
    Label(root, text="", font="calibre 10 bold").pack()

    name_label = Label(root, text="Enter your name:", font="calibre 20 bold",fg="red")  # No padx and pady for space outside the box
    name_label.pack(padx=10, pady=10)  # Add padx and pady for space outside the box
    name_entry = Entry(root, font="calibre 20", bg="lightpink")  # No padx and pady for space outside the box
    name_entry.pack(padx=10, pady=10)  # Add padx and pady for space outside the box
    
    start_button = Button(root,
                          text="Start Quiz",
                          command=start_quiz,
                          font="calibre 20 bold",
                          bg="#143", fg="black")  # No padx and pady for space outside the box
    start_button.pack(padx=10, pady=10)  # Add padx and pady for space outside the box

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Next Question",
                         command=next_question,
                         font="calibre 17 bold", bg="orange", activebackground="yellow", pady=5)

    root.mainloop()
