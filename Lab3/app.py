import os
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

instance_path = os.path.join(basedir, 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(instance_path, 'shop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
auth = HTTPBasicAuth()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(20))
    color = db.Column(db.String(20))
    weight = db.Column(db.Float)


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or user.password != password:
        return False
    return True


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)



@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    output = []
    for item in items:
        output.append({
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'size': item.size,
            'color': item.color,
            'weight': item.weight
        })
    return jsonify({'items': output})


@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify({
        'id': item.id, 'name': item.name, 'price': item.price,
        'size': item.size, 'color': item.color, 'weight': item.weight
    })


@app.route('/items', methods=['POST'])
@auth.login_required
def create_item():
    data = request.get_json()
    # Простейшая валидация
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({'message': 'Bad Request: id and name are required'}), 400

    if Item.query.get(data['id']):
        return jsonify({'message': 'Item with this ID already exists'}), 400

    new_item = Item(
        id=data['id'],
        name=data['name'],
        price=data.get('price', 0.0),
        size=data.get('size'),
        color=data.get('color'),
        weight=data.get('weight')
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item created successfully'}), 201


@app.route('/items/<int:id>', methods=['PUT'])
@auth.login_required
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()

    item.name = data.get('name', item.name)
    item.price = data.get('price', item.price)
    item.size = data.get('size', item.size)
    item.color = data.get('color', item.color)
    item.weight = data.get('weight', item.weight)

    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})


@app.route('/items/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        if not User.query.filter_by(username='admin').first():
            db.session.add(User(username='admin', password='password123'))
            db.session.commit()
            print("Admin created: admin/password123")

    app.run(debug=True, port=5001)