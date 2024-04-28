from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

menu_items = [
    {'name': 'Spaghetti', 'price': '$10'},
    {'name': 'Pizza', 'price': '$12'},
    {'name': 'Salad', 'price': '$8'},
    {'name': 'Burger', 'price': '$9'},
    {'name': 'Steak', 'price': '$10'},
    {'name': 'Chicken Curry', 'price': '$12'},
    {'name': 'Jollof Rice', 'price': '$8'},
    {'name': 'Amala & ewedu', 'price': '$9'},
    {'name': 'Goat Stew', 'price': '$10'},
    {'name': 'BBQ Ribs', 'price': '$12'},
    {'name': 'Starch & Banga', 'price': '$8'},
    {'name': 'Coconut Rice', 'price': '$9'},
    {'name': 'Meatballs', 'price': '$10'},
    {'name': 'Suya', 'price': '$12'},
    {'name': 'Cottage Pie', 'price': '$8'},
    {'name': 'Smoked Bacon', 'price': '$9'},
    {'name': 'Tacos', 'price': '$10'},
    {'name': 'Salmon Steak', 'price': '$12'},
    {'name': 'Smoked Catfish', 'price': '$8'},
    {'name': 'French Baquette', 'price': '$9'},

]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        selected_item = request.form['item']
        return f"You ordered {selected_item}! <a href='{url_for('order')}'>Place Another Order</a>"
    return render_template('order.html', menu_items=menu_items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

