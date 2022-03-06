

from importlib.resources import Resource
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        else:
            return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exist".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
            return {'message': "Store created successifully"}, 201
        except: 
            return {'message': 'An error occured while creating the store.'}, 500


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        
        return {'message': 'store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': list(map( lambda x: x.json(), StoreModel.query.all())) }