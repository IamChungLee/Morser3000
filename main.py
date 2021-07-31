from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap(app)



class Message(FlaskForm):
    message = StringField('Enter your Secret Message:', validators=[DataRequired()])
    submit = SubmitField("Encode")


morse_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----'
}



@app.route('/', methods=["GET", "POST"])
def home():
    morse_coded = ''
    form = Message()
    if form.validate_on_submit():
        encoded = []
        string = form.message.data
        for char in string:
            if char != ' ':
                letter = morse_dict[char]
                encoded.append(letter)
                encoded.append(' ')
            else:
                encoded.append('/')
        morse_coded = ''.join(encoded)
    return render_template('index.html', form=form, code=morse_coded)


if __name__ == "__main__":
    app.run(debug=True)