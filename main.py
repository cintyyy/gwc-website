from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< Updated upstream
=======
@app.route('/outreach')
def outreach():
    return render_template('outreach.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
# more functions here

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)