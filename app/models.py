from app import db
from app import login_manager
from flask_login import UserMixin
from app import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime


class User(UserMixin, db.Model):
    """
    Create a Users table
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60), index=True)
    lastname = db.Column(db.String(60), index=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    sales = db.relationship('SalesTransaction', backref='user', lazy='dynamic')

    @hybrid_property
    def password(self):
        """
        Return the password supplied by the user
        """
        return self.password_hash

    @password.setter
    def set_password(self, plaintext):
        """
        Hash the users plaintext password
        """
        self.password_hash = bcrypt.generate_password_hash(
            plaintext).decode('utf-8')

    def verify_password(self, plaintext):
        """
        Verify if the existing password hash and
        the users' plaintext password are a match
        """
        return bcrypt.check_password_hash(self.password_hash, plaintext)

    def __repr__(self):
        return '<User: {}>'.format(self.firstname)


@login_manager.user_loader
def load_user(user_id):
    """
    Return the corresponding user object
    based on the supplied user_id
    """
    return User.query.get(int(user_id))


class ProductCategory(db.Model):
    """
    Create a product_category table
    """
    __tablename__ = 'product_categories'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(60), index=True, unique=True)
    products = db.relationship(
        'Product',
        backref='productcategory',
        lazy='dynamic')

    def __repr__(self):
        return '<Product Category: {}>'.format(self.category)


class Product(db.Model):
    """
    Create a products table
    """

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), index=True)
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    date_added = db.Column(db.DateTime, default=datetime.now)
    category_id = db.Column(db.ForeignKey('product_categories.id'))
    sales = db.relationship(
        'SalesTransaction',
        backref='product',
        lazy='dynamic')

    def __repr__(self):
        return '<Product: {}>'.format(self.description)


class SalesTransaction(db.Model):
    """
    Create a sales_transaction table
    """

    __tablename__ = 'sales_transaction'

    id = db.Column(db.Integer, primary_key=True)
    transaction_timestamp = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.ForeignKey('users.id'))
    product_id = db.Column(db.ForeignKey('products.id'))

    def __repr__(self):
        return '<Sales Transaction #: {}>'.format(self.id)
