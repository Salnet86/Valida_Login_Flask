from flask import Flask , render_template,request,redirect, url_for
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    


@app.route('/login',methods=['GET', 'POST'])
def login():
    Verifica_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    message=""
    if request.method == 'POST':
        email=request.form['email'].strip()
        password=request.form['password']
        message="Email inserite con sucesso"
     
        
    if not re.match(Verifica_email, email):
        message="Email inserita non è valida"
    
    if not email and not password:
        message = "I campi inseriti sono vuoti"


           
        
       
        redirect(url_for('index'))
    return render_template('index.html',email=email,password=password,message=message)
    

    if __name__ == "__main__":
        app.run(debug=True)