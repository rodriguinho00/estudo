from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/', methods=['get',  'post'])
def home():
    
 conta = None
 pessoas = None
 gorjeta = None

 if request.method == 'post':
  conta = request.form['conta']
  pessoas = request.form['pessoas']
  gorjeta = request.form['gorjeta']

 print(conta, pessoas, gorjeta)

 return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True) 