from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "this is first project in 2 december 2022 2 video <button>click here for index </button> <button>click here for bootstrap </button> <button>click here for staticfile </button>"

@app.route("/index")
def rahul():
    name = "rahul"
    return render_template('index.html',name2 = name)

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

@app.route("/static")
def stat():
    return render_template("stat.html")

app.run(debug=True)
