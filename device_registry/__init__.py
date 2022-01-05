import markdown
import os

from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    # Open the readme file and present it in the home page

    with open(os.path.dirname(app.root_path) + 'README.md', 'r') as markdown_file:
        # read the file content
        content = markdown_file.read()

        # convert to html
        return markdown.markdown(content) 