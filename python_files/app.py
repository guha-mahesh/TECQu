from flask import Flask, jsonify
from flask_cors import CORS
from getdata2 import get_streak

app = Flask(__name__)
CORS(app)  # Enables frontend to communicate with backend

@app.route('/api/streak/<username>')
def api_streak(username):
    streak = get_streak(username)
    return jsonify({"username": username, "streak": streak})

if __name__ == '__main__':
    app.run(debug=True)

