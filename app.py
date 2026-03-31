from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':  

        conta = float(request.form['conta'])
        pessoas = int(request.form['pessoas'])
        gorjeta = float(request.form['gorjeta'])

        valor_gorjeta = conta * (gorjeta / 100)
        total = conta + valor_gorjeta
        por_pessoa = total / pessoas

        if gorjeta < 5:
            classificacao = "Mão de vaca"
        elif gorjeta <= 15:
            classificacao = "Legal"
        else:
            classificacao = "Generoso"

        return render_template(
            'resultado.html',
            gorjeta=valor_gorjeta,
            total=total,
            por_pessoa=por_pessoa,
            classificacao=classificacao
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)