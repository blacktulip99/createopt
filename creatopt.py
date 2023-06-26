from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifica se il nome utente e la password sono corretti
        if username == 'nostronome@gmail.com' and password == '1234':
            # Invia il codice OTP all'indirizzo specificato
            otp_code = '123456'  # Esempio di codice OTP
            send_otp(username, otp_code)

            # Reindirizza all'endpoint per la verifica del codice OTP
            return redirect('/verify_otp')
        else:
            return 'Nome utente o password non corretti'

    return render_template('login.html')


@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        otp = request.form['otp']
        expected_otp = '123456'  # Esempio di codice OTP atteso

        if otp == expected_otp:
            return 'Accesso effettuato correttamente'
        else:
            return 'Codice OTP non valido'

    return render_template('verify_otp.html')


def send_otp(email, otp):
    # Qui puoi implementare la logica per inviare il codice OTP all'indirizzo email specificato
    # Ad esempio, utilizzando una libreria di invio email come smtplib o un servizio di terze parti
    pass


if __name__ == '__main__':
    app.run()
