
from flask import Blueprint,render_template,session,request


clientes_blueprint = Blueprint('clientes', __name__, template_folder='templates')

@clientes_blueprint.route('/clientes')
def listar_clientes():
  return render_template('listar_clientes.html')

@clientes_blueprint.route('/clientes/criar', methods=['GET', 'POST'])
def criar_clientes():
  if request.method == 'GET':
    return render_template('criar_clientes.html')
  else:
    return request.form['nome'], request.form['senha']




@clientes_blueprint.route('/clientes/editar')
def editar_clientes():
  return render_template('editar_clientes.html')


# @bp.route('/login', methods=('GET', 'POST'))
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         db = get_db()
#         error = None
#         user = db.execute(
#             'SELECT * FROM user WHERE username = ?', (username,)
#         ).fetchone()

#         if user is None:
#             error = 'Incorrect username.'
#         elif not check_password_hash(user['password'], password):
#             error = 'Incorrect password.'

#         if error is None:
#             session.clear()
#             session['user_id'] = user['id']
#             return redirect(url_for('index'))

#         flash(error)

#     return render_template('auth/login.html')