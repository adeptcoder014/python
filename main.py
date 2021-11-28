from tkinter import *
import requests


# print(quotes)
def get_quote():
    api_endpoint="https://api.kanye.rest"
    response=requests.get(api_endpoint)
    response.raise_for_status()
    quotes=response.json()
    canvas.itemconfig(quote_text,text=quotes["quote"])



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50,bg="steel blue")

canvas = Canvas(width=300, height=414,bg="steel blue",highlightthickness=0)
background_img = PhotoImage(file="background.png",)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 18, "bold"), fill="white")
canvas.grid(row=0, column=0)
get_quote()

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,bg="steel blue")
kanye_button.grid(row=1, column=0)



window.mainloop()