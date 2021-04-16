from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
# title_label.grid(row=0, column=1)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image)
wrong_button.grid(row=1, column=0)

window.mainloop()