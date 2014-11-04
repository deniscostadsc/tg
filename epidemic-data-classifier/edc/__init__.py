import sys

from unipath import Path

# This line fix the path, and let GAE see the installed libs
BASE_DIR = Path(__file__).parent
sys.path.append(Path(BASE_DIR, "lib"))

from flask import Flask

app = Flask(__name__)

from views import *
