from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data():
    username = request.form['username']
    password = request.form['pass']

    if username=='nikita' and password=='1234':
        return f'Hi Welcome {username}'
    else:
        return f'sorry username or password may be wrong '









if __name__ == '__main__':
    app.run(debug=True, port=8083)

