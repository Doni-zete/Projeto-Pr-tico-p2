
from flask import Blueprint,render_template


moedas_blueprint = Blueprint('moedas', __name__, template_folder='templates')

@moedas_blueprint.route('/moedas')
def listar_moedas():
  return render_template('listar_moedas.html')

@moedas_blueprint.route('/moedas/editar')
def editar_moeda():
  return render_template('editar_moedas.html')

@moedas_blueprint.route('/moedas/criar', methods=('GET', 'POST'))
def criar_moeda():
  return render_template('criar_moedas.html')