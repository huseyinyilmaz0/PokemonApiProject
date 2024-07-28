import requests
import json
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image

screen_tk = tkinter.Tk()
screen_tk.title("Pokemon features")
screen_tk.minsize(width=250,height=250)
screen_tk.config(width=20, height=20)

img = ImageTk.PhotoImage(Image.open("abc.gif"))
panel = tkinter.Label(screen_tk, image = img)
panel.pack()


label = tkinter.Label(text="Enter Pokemon Name or Id")
label.pack()

enter_tk = tkinter.Entry()
enter_tk.pack()
pokemon_name = enter_tk.get()

label1 = tkinter.Label()
label2 = tkinter.Label()
label3 = tkinter.Label()
label4 = tkinter.Label()



def pokemon_info():
    pokemon_name = enter_tk.get()
    url = "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_name)
    response = requests.get(url)
    pokemon_dict = response.json()
    if response.status_code==200:
        if pokemon_name:
            info_name = pokemon_dict["name"]
            info_id = pokemon_dict["id"]
            info_height = pokemon_dict["height"]
            info_weight = pokemon_dict["ability"]
            info_id = pokemon_dict["id"]
            label1.config(text=info_name)
            label2.config(text=f"Height: {info_height}")
            label3.config(text=f"Weight: {info_weight}")
            label4.config(text=f"Id: {info_id}")
            label1.pack()
            label4.pack()
            label2.pack()
            label3.pack()
        else:
            tkinter.messagebox.showerror("show warning", "ENTER POKEMON NAME!")
    else:
        tkinter.messagebox.showerror("show warning",f"{response.status_code} Error!")













enter_button_tk = tkinter.Button(text="Enter",command=pokemon_info)
enter_button_tk.pack()
screen_tk.mainloop()













