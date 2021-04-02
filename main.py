import tkinter

window = tkinter.Tk()
window.title("Gusty Stocks")
window.minsize(width=800, height=600)
window.resizable(0, 0)

main_canvas = tkinter.Canvas(width=795.5, height=600, highlightthickness=2, highlightbackground="black", highlightcolor="black")

background = tkinter.PhotoImage(file="images/bg.png")
main_canvas.create_image(400, 300, image=background)

name_stroke = main_canvas.create_text(400, 200, text="Gusty Stocks", font=("Forte", 50, "bold"), fill="black")
name = main_canvas.create_text(400, 200, text="Gusty Stocks", font=("Forte", 50), fill="#B19817")
slogan = main_canvas.create_text(400, 260, text="A richer journey that leads to success", font=("Kristen ITC", 19))

search_bar = tkinter.Entry(width=40, font=("Arial", 20, "bold"), highlightthickness=2)
search_bar.configure(highlightbackground="black", highlightcolor="black")
main_canvas.create_window(380, 340, window=search_bar)

search_logo_image = tkinter.PhotoImage(file="images/search.png")
search_logo_button = tkinter.Button(image=search_logo_image, highlightthickness=4)
search_logo = main_canvas.create_window(710, 339, window=search_logo_button)

footer_text = tkinter.Label(text="Copyright © Gusty Stocks - Farhan Ali Rahmoon 2021", bg="black", fg="white", font=("Fixedsys", 13), width=78)
footer = main_canvas.create_window(400, 585, window=footer_text)

main_canvas.place(x=0, y=0)

window.mainloop()
