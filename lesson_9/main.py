from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_product_info(product_id):
    product = {
        'id':0,
        'name':'Несуществующий товар',
        'shop':0,
        'stock':0,
        'price':0,
        'number':0,
        'category_id':0,
        'category_name':'Несуществующая категория'
    }
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    sql = "SELECT products.id, products.name, products.shop, products.stock, products.price, products.number, categories.id, categories.name FROM products, categories WHERE products.id=? AND products.category_id=categories.id"
    cursor.execute(sql, product_id)
    result = cursor.fetchall()
    for row in result:
        product = {
            'id':row[0],
            'name':row[1],
            'shop':row[2],
            'stock':row[3],
            'price':row[4],
            'number':row[5],
            'category_id':row[6],
            'category_name':row[7]
        }
    conn.close()
    return product


def get_category_name(category_id):
    category = {'id':0, 'name': 'Неизвестная категория'}
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    sql = "SELECT categories.id, categories.name FROM categories WHERE categories.id=? LIMIT 1"
    cursor.execute(sql, category_id)
    result = cursor.fetchall()
    for row in result:
        category = {'id': row[0], 'name': row[1]}
    conn.close()
    return category

def get_category_list():
    categories = []
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    sql = "SELECT categories.id, categories.name FROM categories"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        categories.append({'id':row[0],'name':row[1]})
    conn.close()
    return categories

def get_products_by_category(category_id):
    products = []
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    sql = "SELECT products.id, products.name, categories.id, categories.name FROM products, categories WHERE products.category_id = categories.id AND categories.id=?"
    cursor.execute(sql, category_id)
    result = cursor.fetchall()
    for row in result:
        products.append({'id': row[0], 'name': row[1], 'category_id':row[2], 'category_name':row[3]})
    conn.close()
    return products

@app.route('/')
def index():
    categories = get_category_list()
    return render_template('index.html', categories = categories)

@app.route('/category/<category_id>')
def products(category_id):
    category = get_category_name(category_id)
    products = get_products_by_category(category_id)
    return render_template('products.html', products = products, category = category)

@app.route('/product/<product_id>')
def product(product_id):
    product = get_product_info(product_id)
    return render_template('product.html', product = product)

app.run()


'''conn = sqlite3.connect("main.db")
cursor = conn.cursor()
sql = "SELECT category.id, category.name FROM category"
cursor.execute(sql)
print(cursor.fetchall()) #Полная выборка по таблице or use fetchone()
print("Here's a listing of all the records in the table:")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY
artist"):
print(row)
print("Results from a LIKE query:")
sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
cursor.execute(sql)
print(cursor.fetchall())'''