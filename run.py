import os
from app import create_app

#'FLASK_CONFIG' is an environment variable.
# It loads the correct environment configured for the app
# Linux terminal use
# export FLASK_CONFIG=development
# Windows command prompt use
# set FLASK_CONFIG=development
config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

# Start the development server
if __name__ == '__main__':
    app.run()
