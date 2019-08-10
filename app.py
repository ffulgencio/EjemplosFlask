from flask import Flask
from flask import render_template
from flask import request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', 
                            name = 'Mark Zuckember',
                            email = 'mz@facebook.com',
                            phone = '18009201516')

@app.route('/products/<int:id>')
def getProductById(id, methods=['GET','POST']):
    products = ['Mause', 'Teclado','Procesador','tarjeta de video']
    product = products[id]
    return render_template('product-detail.html', product = product, products = products)


@app.route('/form')
def formulario():
    return render_template('test.jinja2')

@app.route('/form/procesar',methods=['POST','GET'])
def procesarForm():
    #nombre = request.form['nombre']
    # telefono = request.form['telefono']
    return jsonify(request.form)


@app.route('/empleados')
def getEmpleados():
    empleados = [
        {'nombre':'juan', 'telefono':'809-476-6000'},
        {'nombre':'Manuel', 'telefono':'809-476-6000'},
        {'nombre':'Jose', 'telefono':'809-476-6000'},
        {'nombre':'Ramon', 'telefono':'809-476-6000'},
    ]

    return render_template('empleados.html', empleados=empleados)

if  __name__ == '__main__':
    app.run(port=4200)