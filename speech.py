from flask import Flask,render_template,redirect
import requests
import speech_recognition as sr

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("home.html")

@app.route("/next")
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        s = "Say something"
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            # print(text)
        except:
            print("Sorry, try again")
            # ex = "Sorry, try again"
    return render_template("home.html", random=s, txt=text)

app.run(debug=True)
