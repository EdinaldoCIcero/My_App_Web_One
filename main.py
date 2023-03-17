from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/salvar', methods=['POST'])

def salvar():
	nome_arquivo = request.form['nome_arquivo']
	codigo = request.form['codigo']
	diretorio = request.form['diretorio']

	with open(diretorio + nome_arquivo, 'w') as f:
		f.write(codigo)

	return 'Arquivo salvo com sucesso!'


if __name__ == '__main__':
	app.run(debug=True
