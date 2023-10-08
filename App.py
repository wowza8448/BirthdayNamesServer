from flask import Flask, render_template, request
import json

app = Flask(__name__)

all_rooms = {
    "Blue": {"name": "", "greeting": "", "background": "fireworks.mp4"},
    "Red": {"name": "", "greeting": "", "background": "fireworks.mp4"},
    "Yellow": {"name": "", "greeting": "", "background": "fireworks.mp4"},
    "Orange": {"name": "", "greeting": "", "background": "fireworks.mp4"},
}


@app.route("/", methods=["GET", "POST"])
def create_room():
    if request.method == "POST":
        if request.form.get("Create Page") == "Create Page":
            greeting = request.form.get("greeting")
            color = request.form.get("color")
            name = request.form.get("name")
            background = request.form.get("background")
            all_rooms[color]["greeting"] = greeting
            all_rooms[color]["name"] = name
            all_rooms[color]["background"] = background
    return render_template("create_name.html")


@app.route("/BlueRoom", methods=["GET", "POST"])
def br():
    color = "blue"
    css = f"{color}.css"
    getName = all_rooms["Blue"]["name"]
    getGreeting = all_rooms["Blue"]["greeting"]
    background = all_rooms["Blue"]["background"]
    if background != 'fireworks.mp4':
        css = f"{color}diff.css"
    return render_template(
        "index.html",
        name=getName,
        greeting=getGreeting,
        color=color,
        css=css,
        background=background,
    )


@app.route("/Getblue", methods=["GET"])
def get_blue():
    data = {
        "greeting": all_rooms["Blue"]["greeting"],
        "name": all_rooms["Blue"]["name"],
        "background": all_rooms["Blue"]["background"],
    }
    return json.dumps(data)


@app.route("/RedRoom", methods=["GET", "POST"])
def rr():
    color = "red"
    css = f"{color}.css"
    getName = all_rooms["Red"]["name"]
    getGreeting = all_rooms["Red"]["greeting"]
    background = all_rooms["Red"]["background"]
    if background != 'fireworks.mp4':
        css = f"{color}diff.css"
    return render_template(
        "index.html",
        name=getName,
        greeting=getGreeting,
        color=color,
        css=css,
        background=background,
    )


@app.route("/Getred", methods=["GET"])
def get_red():
    data = {
        "greeting": all_rooms["Red"]["greeting"],
        "name": all_rooms["Red"]["name"],
        "background": all_rooms["Red"]["background"],
    }
    return json.dumps(data)


@app.route("/YellowRoom", methods=["GET", "POST"])
def yr():
    color = "yellow"
    css = f"{color}.css"
    getName = all_rooms["Yellow"]["name"]
    getGreeting = all_rooms["Yellow"]["greeting"]
    background = all_rooms["Yellow"]["background"]
    if background != 'fireworks.mp4':
        css = f"{color}diff.css"
    return render_template(
        "index.html",
        name=getName,
        greeting=getGreeting,
        color=color,
        css=css,
        background=background,
    )


@app.route("/Getyellow", methods=["GET"])
def get_yellow():
    data = {
        "greeting": all_rooms["Yellow"]["greeting"],
        "name": all_rooms["Yellow"]["name"],
        "background": all_rooms["Yellow"]["background"],
    }
    return json.dumps(data)


@app.route("/OrangeRoom", methods=["GET", "POST"])
def orange_r():
    color = "orange"
    css = f"{color}.css"
    getName = all_rooms["Orange"]["name"]
    getGreeting = all_rooms["Orange"]["greeting"]
    background = all_rooms["Orange"]["background"]
    if background != 'fireworks.mp4':
        css = f"{color}diff.css"
    return render_template(
        "index.html",
        name=getName,
        greeting=getGreeting,
        color=color,
        css=css,
        background=background,
    )


@app.route("/Getorange", methods=["GET"])
def get_orange():
    data = {
        "greeting": all_rooms["Orange"]["greeting"],
        "name": all_rooms["Orange"]["name"],
        "background": all_rooms["Orange"]["background"],
    }
    return json.dumps(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
