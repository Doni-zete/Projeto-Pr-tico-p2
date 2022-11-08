
from flask import Blueprint,render_template


clientes_blueprint = Blueprint('clientes', __name__, template_folder='templates')

@clientes_blueprint.route('/clientes')
def listar_clientes():
  return render_template('listar_clientes.html')

@clientes_blueprint.route('/clientes/criar')
def criar_clientes():
  return render_template('criar_clientes.html')

@clientes_blueprint.route('/clientes/editar')
def editar_clientes():
  return render_template('editar_clientes.html')