from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from . import auth
from forms import SignUpForm, LoginForm
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

        # Redirect to the login page if sign up is successful
        return redirect(url_for("auth.login"))

    # Render the sign up template
    return render_template("auth/signup.html", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login a user
    """
    # Create an instance of the LoginForm
    form = LoginForm()

    # Validate the LoginForm on submit
    if form.validate_on_submit():
        # Search the user from the User table based on email supplied
        user = User.query.filter_by(email=form.email.data).first()

        # Verify if the users' login credentials are correct
        if user is not None and user.verify_password(form.password.data):
            # Login the user
            login_user(user)

            # Display message if login successful
            flash("Login successful")

            # Redirect to the dashboard page
            return redirect(url_for("home.dashboard"))
        # Display message if the users' login credentials are incorrect
        else:
            flash("Invalid email or password! Please try again.")

    # Render the login template
    return render_template("auth/login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    """
    Logout a user
    """
    logout_user()
    flash("Successfully loged out.")

    # Redirect to the login page
    return redirect(url_for("auth.login"))
