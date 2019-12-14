from tkinter import *
import requests
import geocoder


def response_weather(weather):
    try:
        name = weather["name"]
        descr = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]
        final_txt = "City: %s\nConditions: %s\nTemperature (C): %s" % (name, descr, temp)
    except:
        final_txt = "The was a problem"
    return final_txt


def set_location():
    g = geocoder.ip('me')
    latit, long = g.latlng
    txt = str(latit) + ', ' + str(long)
    ntr.insert(END, txt)


def get_weather(city):
    weather_key = "3fc7d9656bfbcee25206bc72efa71ae7"
    url = "https://api.openweathermap.org/data/2.5/weather"
    if city.isalpha():
        params = {"APPID": weather_key, "q": city, "units": "metric"}
        response = requests.get(url, params=params)
        weather = response.json()
        lbl["text"] = response_weather(weather)
    else:

        letit, long = city.split(", ")
        params = {"APPID": weather_key, "lat": float(letit), "lon": float(long), "units": "metric"}
        response = requests.get(url, params=params)
        weather = response.json()
        lbl["text"] = response_weather(weather)


# txt = "api.openweathermap.org/data/2.5/forecast?q={city name},{country code}"
# key = "3fc7d9656bfbcee25206bc72efa71ae7"

HEIGHT = 600
WIDTH = 1200
root = Tk()
root.title("Weather App")
root.iconbitmap("Photo\\icon.ico")

cnv = Canvas(root, height=HEIGHT, width=WIDTH).pack()

bg_image = PhotoImage(file="Photo\\sun.png")
bg_lbl = Label(root, image=bg_image)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)


# UPPER FRAME
frm1 = Frame(root, bg="light green", bd=10)
frm1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

btn1 = Button(frm1, text="My Location", bg="gray85", font=40, command=set_location)
btn1.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)

btn2 = Button(frm1, text="Get Weather", bg="gray85", font=40, command=lambda: get_weather(ntr.get()))
btn2.place(relx=0, rely=0, relwidth=0.84, relheight=0.45)

ntr = Entry(frm1, bg="light blue", font=40)
ntr.place(relx=0, rely=0.55, relwidth=0.84, relheight=0.45)


# LOWER FRAME
frm2 = Frame(root, bg="light green", bd=10)
frm2.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.45, anchor="n")

# text = str(g.latlng[0]) + ", " + str(g.latlng[1])
lbl = Label(frm2, text="", font=("Courier", 20), anchor="nw", justify="left", bd=10)
lbl.place(relwidth=1, relheight=1)

root.mainloop()