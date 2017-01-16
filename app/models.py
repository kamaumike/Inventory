from app import db, login_manager
from flask_login import UserMixin
from app import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


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
