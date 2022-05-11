from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy


config = app_config[app_active]


db = SQLAlchemy(config.APP)


class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)


def insert_image(pic, name, mimetype):

    img = Imagem(img=pic.read(), name=name, mimetype=mimetype)
    db.session.add(img)
    db.session.commit()

def filter_animal_image(nome):    
    image_animal = Imagem.query.filter_by(name=nome).first()
    return image_animal

    
        
