from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validasi login di sini
        if username == 'user' and password == 'pass':
            return redirect(url_for('home'))
        else:
            return render_template('index.html', error='Invalid credentials')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

