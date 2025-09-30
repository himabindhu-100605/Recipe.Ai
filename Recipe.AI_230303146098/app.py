import os
from flask import Flask, request, jsonify, render_template
from recipe_matching import RecipeMatcher

app = Flask(__name__, static_folder='static', template_folder='templates')

# make DB path absolute (safe regardless of how you run the app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'data', 'recipes.db')

# create matcher (will raise clear errors if DB missing/corrupt)
matcher = RecipeMatcher(db_path=DB_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/suggest', methods=['POST'])
def suggest():
    data = request.get_json() or {}
    user_ings = [i.strip().lower() for i in data.get('ingredients', [])]
    max_results = int(data.get('max_results', 20))
    results = matcher.suggest(user_ings, max_results=max_results)
    return jsonify(results)

if __name__ == '__main__':
    # debug=True for development only
    app.run(debug=True, host='0.0.0.0', port=5003)
