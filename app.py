from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host')  # Get user input from query parameter
    output = os.popen(f"ping -c 1 {host}").read()  # Executes system command with user input
    return f"<pre>{output}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
