from app import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import app


# Create an instance of Migrate
migrate = Migrate(app, db)

# Create an instance of Manager
manager = Manager(app)

# Connect the script manager and flask-migrate.
#'db' is a command to be run
manager.add_command('db', MigrateCommand)

from app import models

# Start the script manager
if __name__ == '__main__':
    manager.run()
