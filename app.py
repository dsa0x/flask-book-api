from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


shelves = [{
    'shelf_name': 'My shelf',
    'books':[
        {
            'book_name': 'Drummer boy',
            'price': 9.99
        }
    ]
}]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shelf')
def get_shelves():
    return jsonify({'stores': shelves})


@app.route('/shelf/<string:shelf_name>')
def get_shelf(shelf_name):
    for shelf in shelves:
        if shelf['shelf_name'] == shelf_name:
            return jsonify({
                'shelf': shelf
            })


@app.route('/shelf', methods=['POST'])
def post_shelf():
    try:
        request_data = request.get_json()
        new_shelf = {
            'shelf_name': request_data['shelf_name'],
            'books':[]
        }
        shelves.append(new_shelf)
        return jsonify(new_shelf)
    except:
        return jsonify({
            'message': 'Error in adding shelf'
        })


@app.route('/shelf/<string:shelf_name>')
def add_book_in_shelf(shelf_name):
    request_data = request.get_json()
    for shelf in shelves:
        if shelf['shelf_name'] == shelf_name:
            new_book = {
                'book_name': request_data['book_name'],
                'price': request_data['price']
            }
            shelf['books'].append(new_book)
            return jsonify(new_book)
    return jsonify({'message':'shelf not found'})
        


@app.route('/shelf/<string:shelf_name>/<string:book_name>')
def get_book_in_shelf(shelf_name,book_name):
        for shelf in shelves:
            if shelf['shelf_name'] == shelf_name:
                for book in shelf['books']:
                    if book['book_name'] == book_name:
                        return jsonify({
                            'books': shelf['books']
                        })
                    return jsonify({
                        'message':'Book not found'
                    })
            return jsonify({
                'message': 'Shelf not found'
            })


@app.route('/shelf/<string:shelf_name>/books')
def get_all_books(shelf_name):
        for shelf in shelves:
            if shelf['shelf_name'] == shelf_name:
                return jsonify({
                    'books': shelf['books']
                })
            return jsonify({
                'message': 'No book found'
            })

app.run(port=8000, debug=True)
