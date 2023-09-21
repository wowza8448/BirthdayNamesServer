from flask import Flask, render_template, request

app = Flask(__name__)

all_rooms = {'Blue': {'name': '', 'greeting': ''}, 'Red': {'name': '', 'greeting': ''}, 'Yellow': {'name': '', 'greeting': ''}, 'Orange': {'name': '', 'greeting': ''}}

@app.route("/", methods = ['GET', 'POST'])
def create_room():
    if request.method == 'POST':
        if request.form.get('Create Page') == 'Create Page':
           greeting = request.form.get('greeting')
           color = request.form.get('color')
           name = request.form.get('name')
           all_rooms[color]['greeting'] = greeting
           all_rooms[color]['name'] = name
    return render_template('create_name.html')

@app.route("/BlueRoom", methods = ['GET', 'POST'])
def br():
    getName = all_rooms['Blue']['name']
    getGreeting = all_rooms['Blue']['greeting']
    return render_template('index.html', name=getName, greeting=getGreeting)

@app.route("/RedRoom", methods = ['GET', 'POST'])
def rr():
    getName = all_rooms['Red']['name']
    getGreeting = all_rooms['Red']['greeting']
    return render_template('red.html', name=getName, greeting=getGreeting)

@app.route("/YellowRoom", methods = ['GET', 'POST'])
def yr():
    getName = all_rooms['Yellow']['name']
    getGreeting = all_rooms['Yellow']['greeting']
    return render_template('yellow.html', name=getName, greeting=getGreeting)

@app.route("/OrangeRoom", methods = ['GET', 'POST'])
def orange_r():
    getName = all_rooms['Orange']['name']
    getGreeting = all_rooms['Orange']['greeting']
    return render_template('orange.html', name=getName, greeting=getGreeting)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
