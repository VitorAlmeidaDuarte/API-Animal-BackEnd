from Models.Animals import *
from Models.Images import filter_animal_image, insert_image
from Models.User import *
from config import app_config, app_active
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy

config = app_config[app_active]


def create_app(condig_name):
    app = Flask(__name__, template_folder="templates")

    app.secret_key = config.SECRET
    app.config.from_object(app_config[condig_name])
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route("/Cadastro/usuario", methods=["POST"])
    def register_user():
        body = request.get_json()

        if insert_user_banco(body["nome"], body["password"]):
            return {"Sucesso": "usuario cadastrado"}

        else:
            return {"Error": "usuario já existente"}


    @app.route("/Cadastro/animal", methods=["POST"])
    def register_animal():
        body = request.get_json()

        user_verify = verify_user(body["nome"], body["password"])

        if user_verify == True:
            insert_animal_banco(
                body["nomeAnimal"],
                body["qtnEspecies"],
                body["comportamento"],
                body["alimentacao"],
            )

            return {
                "Sucesso": "Animal adicionado, não esqueça de adicionar uma foto dele :)"
            }

        else:
            return {"ERROR": "usuario não encontrado"}

    @app.route("/Animal/mostrar-informações/<nomeAnimal>", methods=["GET"])
    def show_information_animals(nomeAnimal):
        animal_or_ecxeption = show_animals(nomeAnimal.capitalize())

        return animal_or_ecxeption

    @app.route('/Animal/adicionar-foto', methods=['POST'])
    def adicionar_foto():
        file = request.files['imagem']
        body = request.form

        if verify_user(body['nome'], body['password']):
            minetype = file.mimetype
            insert_image(file, body['nomeAnimal'], minetype)
            return {'Sucesso': 'foto do animal adicionado!!'}

        else:
            return {'ERROR': 'voce não tem permissão para isso'}


    @app.route("/Animal/imagem/<nomeAnimal>", methods=["GET"])  
    def show_animal_picture(nomeAnimal):
        animal_or_eception = filter_animal_image(nomeAnimal.capitalize())
        
        try:
            return Response(animal_or_eception.img, mimetype=animal_or_eception.mimetype)
        except:
            return {'ERROR': 'Aninaml não encontrado'}
        
    @app.route("/Animal/modificar", methods=["PUT"])
    def edit_animal():
        body = request.get_json()

        user_verify = verify_user(body["nome"], body["password"])

        if user_verify == True:
            modify_animal_origin(
                nomeAnimal_modify=body["nomeAnimalModificate"],
                new_qtn_especies=body["newQtnEspecies"],
                new_alimentacao=body["newAlimentacao"],
            )

            return {"Sucesso": "animal modificado com exito"}

        else:
            return {"Error": "usuario não encontrado"}

    @app.route("/Animal/deletar", methods=["DELETE"])
    def delete_animal():
        body = request.get_json()

        user_verify = verify_user(body["nome"], body["password"])

        if user_verify:
            delete_animal_origin(body["nomeAnimalDelete"])

            return {"Sucesso": "Animal deletado"}

        else:
            {"Error": "usuario não econtrado"}

    return app