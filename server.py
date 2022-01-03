from flask_app import app
from flask_app.controller import users_controller
from flask_mail import Mail, Message
import os






if __name__ == "__main__":
    app.run(debug=bool(os.environ.get("DEBUG_STATUS")))