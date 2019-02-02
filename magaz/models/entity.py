from magaz import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    price = db.Column(db.Integer,nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTimea, nullable=False)


class Basket(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    ticket_id = db.Column(db.Integer, db.ForeignKey("ticket.id"))
