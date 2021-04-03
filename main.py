import tkinter
import requests

API_KEY = "c1jrhpv48v6o1292jing"


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
    stock_window = tkinter.Toplevel()
    stock_window.minsize(width=590, height=600)
    stock_window.resizable(0, 0)

    canvas = tkinter.Canvas(stock_window, width=590, height=600)

    stock_title = tkinter.Label(stock_window, text=f'{stock_name["result"][0]["description"]} ({stock_name["result"][0]["symbol"]})', font=("Fixedsys", 15))
    canvas.create_window(295, 30, window=stock_title)



    canvas.place(x=0, y=0)


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

footer_text = tkinter.Label(text="Copyright © Gusty Stocks - Farhan Ali Rahmoon 2021", bg="black", fg="white", font=("Fixedsys", 13), width=78)
footer = main_canvas.create_window(400, 585, window=footer_text)

main_canvas.place(x=0, y=0)

window.mainloop()
