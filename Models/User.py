from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from passlib.hash import pbkdf2_sha512


config = app_config[app_active]

db = SQLAlchemy(config.APP)


def create_hash(password):
    pass_hash = pbkdf2_sha512.hash(password.encode("utf-8"))

    return pass_hash


def verify_hash(password, hash_password):
    if pbkdf2_sha512.verify(password, hash_password):
        return True

    else:
        return False
    

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    hash = db.Column(db.LargeBinary)
    admin = db.Column(db.Boolean, default=0)



def verify_user(nome, senha):
    user = Users.query.filter_by(nome=nome).first()

    
    senha_vereficada = verify_hash(senha, user.hash)

    if senha_vereficada:
        return True
    else:
        return False

def insert_user_banco(nome_recebido, senha_recebida):

    if Users.query.filter_by(nome=nome_recebido).all():
        return False

    else:
        

        senha_convertida_in_hash = create_hash(senha_recebida)
        usuario = Users(
                nome=nome_recebido,
                hash=senha_convertida_in_hash.encode('utf-8'),
            )

        db.session.add(usuario)
        db.session.commit()
        return True
