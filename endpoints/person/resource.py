from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Person
from app import db
from sqlalchemy.exc import IntegrityError

obj_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'size': fields.Float,
    'weight': fields.Float,
    'strong_hand': fields.Boolean,
    'experience_id': fields.Integer
}

obj_list_fields = {
    'count': fields.Integer,
    'persons': fields.List(fields.Nested(obj_fields)),
}

obj_post_parser = reqparse.RequestParser()
obj_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')
obj_post_parser.add_argument('size', type=float, required=True, location=['json'],
                              help='size parameter is required')
obj_post_parser.add_argument('weight', type=float, required=True, location=['json'],
                              help='weight parameter is require')
obj_post_parser.add_argument('strong_hand', type=bool, required=True, location=['json'],
                              help='strong hand parameter is required')
obj_post_parser.add_argument('experience_id', type=int, required=True, location=['json'],
                              help='experience_id parameter is required')


class PersonsResource(Resource):
    def get(self, person_id=None):
        if person_id:
            obj = Person.query.filter_by(id=person_id).first()
            if obj:
                return marshal(obj, obj_fields)
            return {'message': 'Person not found'}
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            obj = Person.query.filter_by(**args).order_by(Person.id)
            if obj:
                if limit:
                    obj = obj.limit(limit)

                if offset:
                    obj = obj.offset(offset)

                obj = obj.all()

                return marshal({
                    'count': len(obj),
                    'persons': [marshal(t, obj_fields) for t in obj]
                }, obj_list_fields)
            return {'message': 'Person not found'}

    
    def post(self):
        args = obj_post_parser.parse_args()
        try:
            obj = Person(**args)
            db.session.add(obj)
            db.session.commit()

            return marshal(obj, obj_fields)
        except IntegrityError:
            return {'message': 'Person not saved.'}

    def put(self, person_id=None):
        obj = Person.query.get(person_id)
        if obj:
            if 'name' in request.json:
                obj.name = request.json['name']

            if 'size' in request.json:
                obj.size = request.json['size']

            if 'weight' in request.json:
                obj.weight = request.json['weight']

            if 'strong_hand' in request.json:
                obj.strong_hand = request.json['strong_hand']

            if 'experience_id' in request.json:
                obj.experience_id = request.json['experience_id']
                
            db.session.commit()
            return marshal(obj, obj_fields)
        return {'message': 'Person not found'}

    def delete(self, person_id=None):
        obj = Person.query.get(person_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

            return marshal(obj, obj_fields)
        return {'message': 'Person not found'}