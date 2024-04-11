from flask import Flask, render_template, request, redirect, session,flash
import secrets
import sqlite3
app = Flask(__name__)
app.secret_key="123"

sqlconnection =sqlite3.connect("admin.db")
sqlconnection.execute("create table if not exists users(username text,password integer, email text)")
sqlconnection.close()

# Route for the home  page
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/aerators')
def aerators():
    return render_template("aerators.html")
    
@app.route('/blowers')
def blowers():
    return render_template("blowers.html")

@app.route('/carpet')
def carpet():
    return render_template("carpet.html")

@app.route('/compactors')
def compactors():
    return render_template("compactors.html")

@app.route('/concrete')
def concrete():
    return render_template("concrete.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/coredrill')
def coredrill():
    return render_template("coredrill.html")

@app.route('/dc')
def dc():
    return render_template("dc.html")

@app.route('/demolitions')
def demolition():
    return render_template("demolition.html")

@app.route('/drain')
def drain():
    return render_template("drain.html")

@app.route('/drainclean')
def drainclean():
    return render_template("drainclean.html")

@app.route('/floor')
def floor():
    return render_template("floor.html")

@app.route('/flr')
def flr():
    return render_template("flr.html")

@app.route('/grinder')
def grinder():
    return render_template("grinder.html")

@app.route('/largerent')
def largerent():
    return render_template("largerent.html")

@app.route('/login', methods=["GET", "POST"])
def log():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        sqlconnection = sqlite3.connect('admin.db')
        sqlconnection.row_factory = sqlite3.Row
        cur = sqlconnection.cursor()

        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        data = cur.fetchone()
        if( data):
            session['username'] = data["username"]
            session['password'] = data["password"]
            return redirect("/")
        else:
            flash("Invalid Username and Password", "danger")
            return redirect('/login')
    return render_template('login.html')


@app.route('/signup', methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            
            sqlconnection = sqlite3.connect('admin.db')

            cur = sqlconnection.cursor()
            cur.execute("INSERT INTO users(username, email, password) VALUES (?, ?, ?)", (username, email, password))
            
            sqlconnection.commit()
           
        except:
            flash("Error in Insert Operation", "danger")
        finally:
            sqlconnection.close()
            return redirect('/login')

    return render_template("signup.html")



@app.route('/paint')
def paint():
    return render_template("paint.html")

@app.route('/paints')
def paints():
    return render_template("paints.html")

@app.route('/pressure')
def pressure():
    return render_template("pressure.html")

@app.route('/rent')
def rent():
    return render_template("rent.html")

@app.route('/rentform')
def rentform():
    return render_template("rentform.html")

@app.route('/rentacc')
def rentacc():
    return render_template("rentacc.html")

@app.route('/sales')
def sales():
    return render_template("sales.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/truck')
def truck():
    return render_template("truck.html")

@app.route('/cartform')
def cartform():
    return render_template("cartform.html")

@app.route('/salesacc')
def salesacc():
    return render_template("salesacc.html")  

@app.route('/admin')
def admin():
    return render_template("admin.html")  



@app.route('/rentform')
def welcome():
    return render_template('rentform.html')
@app.route('/order')
def aorders():
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id,name, email, fdate, tdate, address, phone, city, state FROM orders")
    order_data = cursor.fetchall()
    conn.close()
    return render_template('order.html',order_data=order_data)

def connect_db():
    return sqlite3.connect('admin.db')

# Create a function to initialize the database tables
def init_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    fdate DATE,
                    tdate DATE,
                    address TEXT,
                    phone TEXT,
                    city TEXT,
                    state TEXT
                )''')
    conn.commit()
    conn.close()

# Initialize the database tables when the app starts
init_db()

# Route to render the checkout page
@app.route('/rentform')
def checkout():
    return render_template('rentform.html')

# Route to handle the checkout form submission
@app.route('/rentform', methods=['POST'])
def process_checkout():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        fdate = request.form['fdate']
        tdate = request.form['tdate']
        address = request.form['address']
        phone = request.form['phone']
        city = request.form['city']
        state = request.form['state']

        # Save form data to the database
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO orders (name, email, fdate, tdate, address, phone, city, state) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (name, email, fdate, tdate, address, phone, city, state))
        conn.commit()
        conn.close()

        return redirect('/rentacc')  # Redirect to a thank you page after successful submission


@app.route('/cartform')
def welcomea():
    return render_template('cartform.html')
@app.route('/cartorder')
def cartorders():
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id,name, email, address, phone, city, state FROM cartorders")
    order_data = cursor.fetchall()
    conn.close()
    return render_template('cartorder.html',order_data=order_data)

def connect_db():
    return sqlite3.connect('admin.db')

# Create a function to initialize the database tables
def init_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS cartorders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    address TEXT,
                    phone TEXT,
                    city TEXT,
                    state TEXT
                )''')
    conn.commit()
    conn.close()

# Initialize the database tables when the app starts
init_db()

# Route to render the checkout page
@app.route('/cartform')
def checkoutt():
    return render_template('cartform.html')

# Route to handle the checkout form submission
@app.route('/cartform', methods=['POST'])
def process_checkoutt():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        
        address = request.form['address']
        phone = request.form['phone']
        city = request.form['city']
        state = request.form['state']

        # Save form data to the database
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO cartorders (name, email, address, phone, city, state) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, email, address, phone, city, state))
        conn.commit()
        conn.close()

        return redirect('/salesacc')  # Redirect to a thank you page after successful submission

if __name__ == '__main__':
    app.run(debug=True)

