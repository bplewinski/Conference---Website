from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from functools import wraps

app = Flask(__name__)
app.secret_key = "jidejdejdoij"


@app.route('/')
def home():
    return render_template("index.html", title="Health & Fitness Conference")


@app.route('/awards', methods=['GET', 'POST'])
def awards():
    winners = []
    headers = ["Placing", "Award", "Description"]
    description = ["First prize are a set of lovely KettleBells!",
                   "Second prize is a yoga mat, because everyone should stretch!",
                   "Third prize is a coffee maker, for that extra boost!"]
    j = 0
    for i in range(1, 4):
        i = str(i)
        elements = dict(prize="Prize #" + i, description=description[j])
        winners.append(elements)
        j += 1

    if request.method == 'POST':
        return render_template("thankyou.html", title="Thanks for Voting!")

    return render_template("awards.html", winners=winners, headers=headers, title="Awards for Contestants!")


@app.route('/activities')
def activities():
    activity = ["1. meal-prepping", "2. yoga", "3. weight-lifting"]
    return render_template("activities.html", title="List of Activities", list=activity)


@app.route('/meals')
def meals():
    menu = []
    options = ["Menu 1", "Menu 2"]

    daytime = 'Breakfast'
    foods = 'Rolls, Fruit, Coffee'
    menuinfo = {'daytime': daytime, 'foods': foods}
    menu.append(menuinfo)

    daytime = 'Lunch'
    foods = 'Sandwiches, Tea, Water'
    menuinfo = {'daytime': daytime, 'foods': foods}
    menu.append(menuinfo)

    daytime = 'Dinner'
    foods1 = 'Steak, Salad, Wine'
    foods2 = "Fish, Salad, Wine"
    menuinfo = {'daytime': daytime, 'foods1': foods1, 'foods2': foods2}
    menu.append(menuinfo)

    return render_template("meals.html", title="Our Menus", menu=menu, options=options)


@app.route('/keynote')
def keynote():
    speech = []
    speakers = ["Big, Tony", "Viviana, Giuseppe"]

    speech1 = 'Big Tony has a big heart and a big passion for fitness.' \
              'When he was in the pizza business he always got a workout' \
              'by taking care of the extra weight if you know what I mean.'
    voice = {'speech1': speech1}
    speech.append(voice)

    speech2 = 'She loves to work out, and she knows how to motivate!' \
              'One look at whats in her hand, and you will be running quick! ' \
              'Dont make her mad, or you know whats next.'
    voice = {'speech2': speech2}
    speech.append(voice)

    return render_template("keynote.html", title="The Speakers", speakers=speakers, speech=speech)


@app.route('/workshopschedule')
def workshopschedule():
    morning, afternoon, evening = '9:00 a.m. - noon', '1:00 p.m. - 3:30 p.m.', '5:00 p.m. - 9:30 p.m.'
    sesh1, sesh2, sesh3 = '1. Diet', '2. Exercise', '3. Well-Being'
    rma, rmb, rmc = 'Room 1A', 'Room 1B', 'Room 1C'
    name1, name2, name3 = 'Mr.Berry', 'Mr.Jackson', 'Mrs.Frazzetta'
    a, b, c = 'Calories', 'Micros/Macros', 'Nutrition'
    d, e, f = 'Cardiovascular', 'Weight-Lifting', 'Active-Recovery'
    g, h, i = 'Stress-Management', 'Lifestyle', 'Relationships'

    elements = ['Day', 'Session', 'Health & Fitness', 'Speaker', 'Room', 'Time', 'Day 1', '', '', '', '',
                '', '', sesh1, '', '', '', '', '', '', a, name1, rma, afternoon, '', '', b, name2, rmb,
                afternoon, '', '', c, name3, rmc, afternoon, '', sesh2, '', '', '', '', '', '', d, name1,
                rma, morning, '', '', e, name2, rmb, morning, '', '', f, name3, rmc, morning, 'Day 2', '',
                '', '', '', ' ', '', sesh3, '', '', '', '', '', '', g, name1, rma, evening, '', '', h, name2,
                rmb, evening, '', '', i, name3, rmc, evening]

    return render_template("workshopschedule.html", title="Schedule", elements=elements)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        prefix = request.form.get("preselect")
        first = request.form.get("first")
        last = request.form.get("last")
        add_1 = request.form.get("add1")
        add_2 = request.form.get("add2")
        city = request.form.get("city")
        state = request.form.get("state")
        zip = request.form.get("zip")
        phone = request.form.get("phone")
        email = request.form.get("email")
        position = request.form.get("position")
        comp = request.form.get("company")
        diet = request.form.get("diet")
        exer = request.form.get("exercise")
        well = request.form.get("wellbeing")

        return render_template("thankyou.html", pre=prefix, fn=first, ln=last, add=add_1,
                               city=city, state=state, zip=zip, phone=phone, email=email,
                               pos=position, comp=comp, diet=diet, exer=exer, well=well,
                               title="Thanks for Registering")
    else:
        return render_template("registration.html", title="Register Here")


def status(func):
    @wraps(func)
    def wrapper_status(*args, **kwargs):
        if 'logged_in' in session:
            print("Yes, logged in")
            return func(*args, **kwargs)
        else:
            message = "Sorry, can't access admin page"
            return redirect(url_for('login', message=message))

    return wrapper_status


@app.route('/admin/')
@status
def admin():
    firstname = ''
    lastname = ''
    if 'firstname' in session:
        firstname = session['firstname']
    if 'lastname' in session:
        lastname = session['lastname']

    return render_template('admin.html', firstname=firstname, lastname=lastname)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    con = sqlite3.connect("conference.sqlite")
    cur = con.cursor()
    if request.method == "POST":
        un = request.form.get("username")
        pw = request.form.get("password")
        result = check_user_credentials(cur, un, pw)
        if result:
            print("User is logged in")
            return redirect(url_for('admin',
                                    firstname=session['firstname'],
                                    lastname=session['lastname'],
                                    **request.args))
        else:
            message = "Sorry, invalid"
            return render_template('login.html', message=message)
    else:
        message = ''
        if request.args:
            message = request.args['message']

        return render_template('login.html', message=message)


@app.route('/logout/', methods=['POST', 'GET'])
def logout():
    if request.method == 'POST':
        if 'firstname' in session:
            session.pop('firstname')

        if 'lastname' in session:
            session.pop('lastname')

        if 'logged_in' in session:
            session.pop('logged_in')
        return redirect(url_for('logout', message="You are now logged out."))

    else:
        return render_template('logout.html')


def check_user_credentials(cur, un, pw):
    is_valid = False
    query = "SELECT firstname, lastname FROM users " \
            " WHERE username='" + un + "' AND password='" + pw + "'"
    result = cur.execute(query)
    user = result.fetchone()
    if user is not None:
        is_valid = True
        session['firstname'] = user[0]
        session['lastname'] = user[1]
        session['logged_in'] = True
        print(session['firstname'])

    return is_valid


if __name__ == '__main__':
    app.run()
