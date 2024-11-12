from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienessomos')
def quienessomos():
    return render_template('quienessomos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Aquí podrías procesar o guardar los datos del formulario
        return redirect(url_for('index'))
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
