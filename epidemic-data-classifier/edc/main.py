import os
import sys

# This line fix the path, and let GAE see the installed libs
SRC_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(SRC_DIR, "lib"))

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
