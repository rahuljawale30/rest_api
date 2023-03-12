from flask import Flask,request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)  # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'shrirangjawale72@gmail.com'
app.config['MAIL_PASSWORD'] = 'Rjawale30@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


# message object mapped to a particular URL ‘/’
@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        msg = Message(
            'Hello',
            sender='rahuljawale101093@gmail.com',
            recipients=['receiver’shrirangjawale72@gmail.com']
        )
        msg.body = 'Hello Flask message sent from Flask-Mail'
        mail.send(msg)
        return 'Sent email'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)