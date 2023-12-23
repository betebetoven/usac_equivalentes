from parsero import parsero
#GUI
from flask import Flask, request, render_template
from ply.yacc import yacc
# import other necessary modules

app = Flask(__name__)

# Your existing lexer, parser, and other related code remains the same

# Set up your routes
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    input_text = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        p = parsero({})
        try:
            result = p.parser.parse(input_text)
        except Exception as e:
            result = {'ERROR': f"Error de sintaxis o en las variables ingresadas"}
    return render_template('index.html', result=result, input_text=input_text)



if __name__ == '__main__':
    app.run(debug=True)


