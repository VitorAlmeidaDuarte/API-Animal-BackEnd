from unittest import expectedFailure
from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]

db = SQLAlchemy(config.APP)

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    qtn_especies = db.Column(db.Integer)
    comportamento = db.Column(db.String(14))
    alimentacao = db.Column(db.String(16))


class AnimalsManage():
    def insert_animal_banco(nome_r, qtn_especies_r, comportamento_r, alimentacao_r):
        animal = Animals(
            nome=nome_r,
            qtn_especies=qtn_especies_r,
            comportamento=comportamento_r,
            alimentacao=alimentacao_r
        )

        db.session.add(animal)
        db.session.commit()

    def show_animals(nomeAnimal_r):
        animal_object = Animals.query.filter_by(nome=nomeAnimal_r).first()

        
        try:
            animal_json = {
            'nomeAnimal': animal_object.nome,
            'Especies': animal_object.qtn_especies,
            'Comportamento': animal_object.comportamento,
            'Alimentacao': animal_object.alimentacao

        }
        except:
            return {'ERROR': 'animal não econtrado'}
        return animal_json

    def modify_animal_origin(nomeAnimal_modify, new_qtn_especies, new_alimentacao):

        animal = Animals.query.filter_by(nome=nomeAnimal_modify).first()

        animal.qtn_especies = new_qtn_especies
        animal.alimentacao = new_alimentacao

        db.session.commit()

    def delete_animal_origin(nomeAnimal_delete):
        animal = Animals.query.filter_by(nome=nomeAnimal_delete).first()

        db.session.delete(animal)
        db.session.commit()
