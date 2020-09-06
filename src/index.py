from flask import Flask, render_template

app = Flask(__name__) #Para decirle a Python que esto arranca la aplicación

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__': #Vaidar que estoy en el principal
    app.run(debug=True) #Arranco la aplicación