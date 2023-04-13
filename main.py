from flask import Flask,render_template,request
import requests


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/post')
def post():
    return render_template('post.html')
    
@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
   
    import smtplib
    my_email="kaurjaspreet200219@gmail.com"
    password="8307189293"
    with smtplib.SMTP("smtp.gmail.com", 587)  as connection:
        connection.starttls() #for safety
        connection.login(user=my_email,password=password)
        connection.sendmail(
        from_addr=my_email,to_addrs=my_email,msg=(data["message"])
    )

    return  "<h1>Successfully sent your message</h1>"


app.run(debug=True)
