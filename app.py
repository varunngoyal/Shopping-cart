from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify, request

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Shopping_cart"

mongo = PyMongo(app)


@app.route('/')
def home_page():
    return "We are live!"


@app.route('/item/add', methods=['POST'])
def add_item():
    json = request.json

    if ('name' in json) and ('price' in json) and ('in_stock' in json) \
            and request.method == 'POST':
        pass
    else:
        return not_found()

    mongo.db.item.insert_one(json)

    res = jsonify("Item added successfully!")

    return res


@app.route('/items')
def get_items():

    items = mongo.db.item.find()

    res = dumps(items)

    return res


@app.route('/item/<id>')
def get_item(id):

    item = mongo.db.item.find_one({"_id": ObjectId(id)})

    res = dumps(item)

    return res


@app.route('/item/delete/<id>', methods=['DELETE'])
def delete_item(id):

    mongo.db.item.delete_one({"_id": ObjectId(id)})

    res = jsonify("Item deleted successfully!")

    return res


@app.route('/item/update/<id>', methods=['PUT'])
def update_item(id):
    _id = id
    json = request.json

    if ('name' in json or 'price' in json or 'in_stock' in json) \
            and request.method == 'PUT':
        pass
    else:
        return not_found()

    mongo.db.item.update_one(
        {'_id': ObjectId(_id)},
        {
            '$set': json
        }
    )

    res = jsonify("Item updated successfully!")

    return res


@app.route('/user/add', methods=['POST'])
def add_user():
    json = request.json

    if ('name' in json) and ('phone_no' in json) and request.method == 'POST':
        pass
    else:
        return not_found()

    mongo.db.user.insert_one(json)

    res = jsonify("User added successfully!")

    return res


@app.route('/users')
def get_users():

    users = mongo.db.user.find()

    res = dumps(users)

    return res


@app.route('/user/<id>')
def get_user(id):

    user = mongo.db.user.find_one({"_id": ObjectId(id)})

    res = dumps(user)

    return res


@app.route('/user/delete/<id>', methods=['DELETE'])
def delete_user(id):

    mongo.db.user.delete_one({"_id": ObjectId(id)})

    res = jsonify("User deleted successfully!")

    return res


@app.route('/user/update/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    json = request.json

    if ('name' in json or 'phone_no' in json) \
            and request.method == 'PUT':
        pass
    else:
        return not_found()

    mongo.db.user.update_one(
        {'_id': ObjectId(_id)},
        {
            '$set': json
        }
    )

    res = jsonify("User updated successfully!")

    return res


@app.route('/user/<u_id>/cart/add/<item_id>', methods=['POST'])
def add_cart_item(u_id, item_id):
    json = request.json

    item = mongo.db.item.find_one({"_id": ObjectId(item_id)})

    mongo.db.user.update_one(
        {'_id': ObjectId(u_id)},
        {
            '$addToSet': {'cart': item}
        }
    )

    res = jsonify("Cart item added successfully!")

    return res


@app.route('/user/<uid>/cart/delete', methods=['DELETE'])
def delete_cart(uid):

    mongo.db.user.update_one(
        {'_id': ObjectId(uid)},
        {
            '$set': {'cart': []}
        }
    )
    res = jsonify("Cart discarded successfully!")

    return res


@app.route('/user/<uid>/cart/delete/<item_id>', methods=['DELETE'])
def delete_cart_item(uid, item_id):

    mongo.db.user.update_one(
        {'_id': ObjectId(uid)},
        {
            '$pull': {'cart': {'_id': ObjectId(item_id)}},
        },
        upsert=True
    )
    res = jsonify("Cart item removed successfully!")

    return res


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status_code': 404,
        'message': 'Not found '+request.url
    }

    res = jsonify(message)

    res.status_code = 404

    return res


if __name__ == "__main__":
    app.run(port=5000, debug=True)
