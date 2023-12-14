from flask import Flask, render_template, request
import calendar
import locale

app = Flask(__name__)

# Configuração do local para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')

# Configuração da codificação padrão para utf-8
locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

@app.route('/calendario/<ano>/<mes>', methods=['GET'])
def mostrar_calendario(ano, mes):
    meses = {
        'janeiro': 1,
        'fevereiro': 2,
        'marco': 3,
        'abril': 4,
        'maio': 5,
        'junho': 6,
        'julho': 7,
        'agosto': 8,
        'setembro': 9,
        'outubro': 10,
        'novembro': 11,
        'dezembro': 12,
    }

    num_mes = meses.get(mes.lower())

    if num_mes is not None:
        # Gera o calendário para o mês selecionado
        cal = calendar.month(int(ano), num_mes)

        # Obtém o nome do mês com a primeira letra maiúscula
        nome_mes = mes.capitalize()

        # Renderiza o template HTML com o calendário, o nome do mês e o ano
        return render_template('index.html', ano=ano, mes=nome_mes, calendario=cal)

    return render_template('index.html', ano=None, mes=None, calendario=None)

if __name__ == '__main__':
    app.run(debug=False)
