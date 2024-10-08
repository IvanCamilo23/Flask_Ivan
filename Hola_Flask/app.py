from flask import Flask
import numpy as np
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"

@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1> El resultado es: {resultado}</h1> <hr>"

@app.route("/Edades")
@app.route("/Edades/<int:Edad>")
def Edades(Edad=0):
    if Edad<18:
        R="Menor de edad"
    elif(Edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"

@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglos=np.random.randint(valores, size=columnas)
    else:
        arreglos=np.random.randint(valores, size=(filas, columnas))
        
    return f"<h1>El arreglo aleatorio es: {arreglos}</h1> <hr>"    

if __name__ == "__main__":
    app.run(debug=True)