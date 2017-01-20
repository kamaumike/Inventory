from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from . import auth
from froms import SignUpForm, LoginForm
from ..import db
from ..models import User


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Sign Up a user
    """
    # Create an instance of the SignUpForm
    form = SignUpForm()

    # Validate the SignUpForm on submit
    if form.validate_on_submit():
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            password=form.password.data)

        # Add the user to the database
        db.session.add(user)
        db.session.commit()
        flash("You successfully signed up.")

        # Redirect to the login page
        return redirect(url_for("auth.login"))

    # Render the sign up template
    return render_template("auth/signup.html", form=form)
