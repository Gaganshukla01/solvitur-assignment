from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/home.html')
def index():
    return render_template('home.html', the_title='Home page')

@app.route('/form.html')
def about():
    return render_template('form.html', the_title='form page')

@app.route('/table.html')
def contact():
    return render_template('table.html', the_title='table page')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
