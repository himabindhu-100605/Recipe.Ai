# Recipe.Ai
A minimal Flask project that suggests recipes based on available ingredients.
This repo includes a seeded SQLite database (`data/recipes.db`) with a few sample recipes
and substitutions.

## How to run

1. Create a virtualenv (optional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
  ```

2. Run the app:
   ```bash
   python app.py
   ```
3. Structure:










<img width="295" height="319" alt="Screenshot 2025-09-30 at 8 43 52 PM" src="https://github.com/user-attachments/assets/4346ca0d-4c79-422e-bf66-6b78626714aa" />

4. Open http://localhost:5000 in your browser.

## What is included

- `app.py` — Flask app
- `recipe_matching.py` — core matching logic
- `substitution.py` — substitution lookup
- `templates/index.html` — simple frontend
- `static/styles.css` — basic styling
- `data/recipes.db` — seeded SQLite DB

 ## Results:
 <img width="1206" height="721" alt="Screenshot 2025-09-30 at 8 46 23 PM" src="https://github.com/user-attachments/assets/bc0edb9f-5f6a-4bb0-b062-453c70c6d2b4" />

