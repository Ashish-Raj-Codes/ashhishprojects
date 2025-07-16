import flask
from flask import Flask

# Create Flask app
myapp = Flask(__name__)

# Define the route and function (no extra indentation!)
@myapp.route('/info')
def lwinfo():
    return 'this is LW, Work for making India'

# Run the app
if __name__ == '__main__':
    myapp.run(debug=True)
