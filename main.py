import tkinter
import requests
import webbrowser

API_KEY = "c1jrhpv48v6o1292jing"
CURRENT_STOCK_NAME = "FARHAN"
stock_window = None

# global write_email, status_message


def toggle_subscription():
    global CURRENT_STOCK_NAME

    try:
        with open("./files/stocks.txt") as file:
            stock_codes = file.read().splitlines()
        index_of_stock = stock_codes.index(CURRENT_STOCK_NAME)
        remove_stock_details(CURRENT_STOCK_NAME)
    except FileNotFoundError:
        add_stock_details(CURRENT_STOCK_NAME)
    except ValueError:
        add_stock_details(CURRENT_STOCK_NAME)


def add_stock_details(stock_code):
    try:
        with open("./files/stocks.txt", mode="a") as file:
            file.write(stock_code + "\n")
    except FileNotFoundError:
        with open("./files/stocks.txt", mode="w") as file:
            file.write(stock_code + "\n")
    finally:
        get_stock_info()


def remove_stock_details(stock_code):
    try:
        with open("./files/stocks.txt") as file:
            stock_codes = file.read().splitlines()
        stock_codes.remove(stock_code)

        with open("./files/stocks.txt", mode="w") as file:
            for line in stock_codes:
                file.write(line + "\n")

        get_stock_info()
    except FileNotFoundError:
        print("File does not exist!")


def open_url(url):
    webbrowser.open_new(url)


def get_stock_info():
    parameters = {"symbol": search_bar.get().upper(), "token": API_KEY}
    stock_prices = requests.get(url="https://finnhub.io/api/v1/quote", params=parameters)
    stock_prices.raise_for_status()
    prices_data = stock_prices.json()
    print(prices_data)

    parameters2 = {"q": search_bar.get(), "token": API_KEY}
    stock_name = requests.get(url="https://finnhub.io/api/v1/search", params=parameters2)
    name_data = stock_name.json()
    print(name_data)

    create_window(prices_data, name_data)


def create_window(stock_price, stock_name):
    global CURRENT_STOCK_NAME, stock_window

    if stock_window:
        stock_window.destroy()
    stock_window = tkinter.Toplevel()
    stock_window.minsize(width=590, height=470)
    stock_window.resizable(0, 0)
    stock_window.title(f'{stock_name["result"][0]["description"]} ({stock_name["result"][0]["symbol"]})')
    stock_window.focus_force()

    stock_title = tkinter.Label(stock_window, text=f'{stock_name["result"][0]["description"]} ({stock_name["result"][0]["symbol"]})', font=("Fixedsys", 16))
    stock_title.place(x=70, y=26)

    try:
        with open("./files/stocks.txt") as file:
            stock_codes = file.read().splitlines()
        index_of_stock = stock_codes.index(stock_name["result"][0]["symbol"])
        subscribe_icon = tkinter.PhotoImage(master=stock_window, file="./images/remove.png")
    except FileNotFoundError:
        subscribe_icon = tkinter.PhotoImage(master=stock_window, file="./images/add.png")
    except ValueError:
        subscribe_icon = tkinter.PhotoImage(master=stock_window, file="./images/add.png")

    CURRENT_STOCK_NAME = stock_name["result"][0]["symbol"]
    notification_button = tkinter.Button(master=stock_window, image=subscribe_icon, highlightthickness=0, bd=0,
                                         command=toggle_subscription)
    notification_button.photo = subscribe_icon
    notification_button.place(x=470, y=20)

    canvas1 = tkinter.Canvas(stock_window, width=450, height=70, highlightthickness=2, highlightbackground="black",
                             highlightcolor="black")

    heading = tkinter.Label(stock_window, text="Recent Statistics:", bg="black", fg="white", width=56,
                            font=("Fixedsys", 12))
    canvas1.create_window(227, 10, window=heading)
    canvas1.create_text(39, 34, text="Current:", font=("Arial", 10, "bold"))
    canvas1.create_text(110, 34, text=f'${stock_price["c"]}', font=("Arial", 10))
    canvas1.create_text(188, 34, text="|         Open:", font=("Arial", 10, "bold"))
    canvas1.create_text(259, 34, text=f'${stock_price["o"]}', font=("Arial", 10))
    canvas1.create_text(337, 34, text="|        High:", font=("Arial", 10, "bold"))
    canvas1.create_text(408, 34, text=f'${stock_price["h"]}', font=("Arial", 10))
    canvas1.create_text(39, 58, text="Low:", font=("Arial", 10, "bold"))
    canvas1.create_text(110, 58, text=f'${stock_price["l"]}', font=("Arial", 10))
    canvas1.create_text(188, 58, text="|    Previous:", font=("Arial", 10, "bold"))
    canvas1.create_text(259, 58, text=f'${stock_price["pc"]}', font=("Arial", 10))
    canvas1.create_text(337, 58, text="|     Stamp:", font=("Arial", 10, "bold"))
    canvas1.create_text(408, 58, text=f'{float(stock_price["t"]):.3}', font=("Arial", 10))

    canvas1.place(x=70, y=80)

    canvas2 = tkinter.Canvas(stock_window, width=450, height=70, highlightthickness=2, highlightbackground="black",
                             highlightcolor="black")

    heading2 = tkinter.Label(stock_window, text="Next Day Predictions (work-in-progress):", bg="black", fg="white",
                             width=56, font=("Fixedsys", 12))
    canvas2.create_window(227, 10, window=heading2)
    canvas2.create_text(39, 34, text="Current:", font=("Arial", 10, "bold"))
    canvas2.create_text(110, 34, text="$1234.34    |", font=("Arial", 10))
    canvas2.create_text(188, 34, text="Open:", font=("Arial", 10, "bold"))
    canvas2.create_text(259, 34, text="$1234.34    |", font=("Arial", 10))
    canvas2.create_text(337, 34, text="High:", font=("Arial", 10, "bold"))
    canvas2.create_text(408, 34, text="$1234.34", font=("Arial", 10))
    canvas2.create_text(39, 58, text="Low:", font=("Arial", 10, "bold"))
    canvas2.create_text(110, 58, text="$1234.34    |", font=("Arial", 10))
    canvas2.create_text(188, 58, text="Previous:", font=("Arial", 10, "bold"))
    canvas2.create_text(259, 58, text="$1234.34    |", font=("Arial", 10))
    canvas2.create_text(337, 58, text="Stamp:", font=("Arial", 10, "bold"))
    canvas2.create_text(408, 58, text="$1234.34", font=("Arial", 10))

    canvas2.place(x=70, y=170)

    canvas3 = tkinter.Canvas(stock_window, width=450, height=155, highlightthickness=2, highlightbackground="black",
                             highlightcolor="black")

    heading3 = tkinter.Label(stock_window, text="Top 3 News:", bg="black", fg="white",
                             width=56, font=("Fixedsys", 12))
    canvas3.create_window(227, 10, window=heading3)
    p = {"q": stock_name["result"][0]["description"], "apiKey": "78986d36cd1f47b2964caa7babf077e1"}
    news_api = requests.get(url="https://newsapi.org/v2/everything", params=p).json()
    news1 = tkinter.Label(stock_window, text=f'By: {news_api["articles"][0]["author"]} - Click here...', font=("Arial", 10, "bold"))
    canvas3.create_window(219, 42, window=news1, width=420)
    news1.bind("<Button-1>", lambda e: open_url(news_api["articles"][0]["url"]))
    canvas3.create_line(10, 65, 440, 65)
    news2 = tkinter.Label(stock_window, text=f'By: {news_api["articles"][1]["author"]} - Click here...', font=("Arial", 10, "bold"))
    canvas3.create_window(219, 88, window=news2, width=420)
    news2.bind("<Button-1>", lambda e: open_url(news_api["articles"][1]["url"]))
    canvas3.create_line(10, 111, 440, 111)
    news3 = tkinter.Label(stock_window, text=f'By: {news_api["articles"][2]["author"]} - Click here...', font=("Arial", 10, "bold"))
    canvas3.create_window(219, 134, window=news3, width=420)
    news3.bind("<Button-1>", lambda e: open_url(news_api["articles"][2]["url"]))

    canvas3.place(x=70, y=260)


def add_email():
    print("test")
    # global write_email, status_message
    # if write_email.get():
    #     with open("./files/email.txt", mode="w") as email_file:
    #         email_file.write(write_email.get())
    #     status_message.config(text="Email successfully added to our database...", font=("Arial", 9, "bold"), fg="#1fa743")
    #     write_email.delete(0, tkinter.END)
    # else:
    #     status_message.config(text="Please enter an email...", font=("Arial", 9, "bold"), fg="#e75151")


def create_email_window():
    # global write_email, status_message
    email_window = tkinter.Toplevel()
    email_window.minsize(width=430, height=10)
    email_window.resizable(0, 0)
    email_window.focus_force()

    # Header
    add_an_email = tkinter.Label(master=email_window, text="Please enter an email", font=("Berlin Sans FB Demi", 20, "bold"))
    add_an_email.place(x=20, y=15)

    # Entry Box
    write_email = tkinter.Entry(master=email_window, width=25, font=("Arial", 17, "bold"), highlightthickness=2)
    write_email.place(x=22, y=65)
    write_email.focus()

    add_image = tkinter.PhotoImage(master=email_window, file="./images/add_email.png")
    add_button = tkinter.Button(master=email_window, image=add_image, highlightthickness=0, bd=0, command=add_email)
    add_button.photo = add_image
    add_button.place(x=368, y=66.5)

    # Empty placeholder
    # status_message = tkinter.Label(email_window, text="Test testt")
    # status_message.place(x=22, y=15)


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
search_logo_button = tkinter.Button(image=search_logo_image, highlightthickness=4, command=get_stock_info)
search_logo = main_canvas.create_window(710, 339, window=search_logo_button)

send_email_image = tkinter.PhotoImage(file="images/send.png")
send_email = main_canvas.create_image(340, 400, image=send_email_image)

send_email_button = tkinter.Button(text="Send Email", highlightthickness=4, font=("Arial", 8, "bold"))
main_canvas.create_window(340, 440, window=send_email_button)

add_email_image = tkinter.PhotoImage(file="images/email.png")
add_email = main_canvas.create_image(440, 400, image=add_email_image)

add_email_button = tkinter.Button(text="Add Email", highlightthickness=4, font=("Arial", 8, "bold"), command=create_email_window)
main_canvas.create_window(440, 440, window=add_email_button)

footer_text = tkinter.Label(text="Copyright © Gusty Stocks - Farhan Ali Rahmoon 2021", bg="black", fg="white", font=("Fixedsys", 13), width=78)
footer = main_canvas.create_window(400, 585, window=footer_text)

main_canvas.place(x=0, y=0)

window.mainloop()
