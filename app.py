import os
from flask import Flask, render_template, request, flash, redirect, url_for ,send_from_directory
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'pushpendra_portfolio_key'

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'testingpushpendra@gmail.com' # Apna Gmail yahan likhein
app.config['MAIL_PASSWORD'] = 'xmvp frry iqwv ocqa'    # Apna 16-digit App Password yahan likhein

# YEH LINE ZAROORI HAI:
app.config['MAIL_DEFAULT_SENDER'] = 'testingpushpendra@gmail.com' 

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message_body = request.form.get('message')    

    # Create the message object
    msg = Message(
        subject=f"Portfolio Contact: {subject}",
        sender=app.config['MAIL_USERNAME'], 
        recipients=['testingpushpendra@gmail.com'], 
        body=f"New message from your portfolio:\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
    )

    try:
        mail.send(msg)
        flash("Success! Your message has been sent.", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
    
    # This return was missing or unreachable before
    return redirect(url_for('index'))

@app.route('/download-resume')
def download_resume():
    resume_path = os.path.join(app.root_path, 'static')
    try:
        return send_from_directory(
            directory=resume_path, 
            path='resume.pdf', 
            as_attachment=True
        )
    except FileNotFoundError:
        return "Error: File 'resume.pdf' not found in static folder!", 404
if __name__ == '__main__':
    app.run(debug=True)