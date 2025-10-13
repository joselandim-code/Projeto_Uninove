from flask import Flask, redirect, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    
    if request.method == "POST":
        

        nome = request.form.get("nome")
        matricula = request.form.get("matricula")
        idade = request.form.get("idade")
        data_de_nascimento = request.form.get("data_de_nascimento")
        rg = request.form.get("rg")
        cpf = request.form.get("cpf")
        rua = request.form.get("rua")
        bairro = request.form.get("bairro")
        cidade = request.form.get("cidade")
        uf = request.form.get("uf")
        curso = request.form.get("curso")
        telefone = request.form.get("telefone")
        
        
        
        
        
        