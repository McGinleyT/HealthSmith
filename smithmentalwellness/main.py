from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/schedule")
def schedule():
    return render_template('schedule.html')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006, debug=True)