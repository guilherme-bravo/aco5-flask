from crypt import methods
from wsgiref.util import request_uri
from flask import Flask, jsonify, render_template, request, redirect 
from flask_mail import Mail, Message 


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def cartinha():
    return render_template('index.html')



@app.route("/msg", methods=['GET', 'POST'])
def mensagem():

    if request.method == "POST":
        req = request.form

        primeiroNome = req['primeiroNome']
        segundoNome = req['segundoNome']
        mensagem = req['msg']

        print(primeiroNome, segundoNome, mensagem)

        return redirect(request.url), primeiroNome, segundoNome, mensagem

    return render_template('formulario.html')

#config do gmail 
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'correioelegante.impacta@yahoo.com',
    "MAIL_PASSWORD": 'batatafrita123'
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route('/enviar')
def index(primeiroNome, segundoNome, mensagem):
    if __name__  == '__main__':
        with app.app_context():
            msg = Message(subject='Correio Elegante Impacta 2022', 
            sender=app.config.get("MAIL_USERNAME"), 
            recipients=[f'{primeiroNome}.{segundoNome}@aluno.faculdadeimpacta.com.br'], 
            body=mensagem)
            mail.send(msg)
    return jsonify("Mensagem enviada")
app.run(debug = True)

