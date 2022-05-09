from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]

db = SQLAlchemy(config.APP)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    hash = db.Column(db.LargeBinary)
    admin = db.Column(db.Boolean, default=0)


def verify_user(nome, senha):
    user = Users.query.filter_by(nome=nome).first()

    from PasswordHashs import verify_hash
    senha_vereficada = verify_hash(senha, user.hash)

    if senha_vereficada:
        return True
    else:
        return False

def insert_user_banco(nome_recebido, senha_recebida):

    if Users.query.filter_by(nome=nome_recebido).all():
        return False

    else:
        from PasswordHashs import create_hash

        senha_convertida_in_hash = create_hash(senha_recebida)
        usuario = Users(
                nome=nome_recebido,
                hash=senha_convertida_in_hash.encode('utf-8'),
            )

        db.session.add(usuario)
        db.session.commit()
        return True
