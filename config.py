from os import path, urandom


# Web Server
CSRF_ENABLED = True
SECRET_KEY = urandom(30)
PROPAGATE_EXCEPTIONS = True

# Temporary Directory
TEMP_DIR = path.join(path.abspath(path.dirname(__file__)), "tmp")
