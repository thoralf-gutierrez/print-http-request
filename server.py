from flask import Flask
from flask import request

app = Flask(__name__)

HEADER_TEMPLATE="""
Headers
=======
{}"""

@app.route('/')
def print_request():
	print(HEADER_TEMPLATE.format(request.headers))
	return ""
