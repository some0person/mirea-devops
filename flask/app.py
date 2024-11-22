from flask import Flask, render_template, request, redirect, url_for

from database import Products


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']

        Products().addProduct(name=title, price=price)

        return redirect(url_for('index'))
    
    products = Products().getProducts()

    return render_template('index.html', products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
