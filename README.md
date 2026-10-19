# Yash Cybersecurity Portfolio

A colorful, responsive dark-neon portfolio built with HTML, CSS, JavaScript, and Python Flask.

## Requirements
- Python 3.10 or newer
- pip

## Run locally
1. Extract the ZIP and open a terminal inside the `cybersecurity-portfolio` folder.
2. Create a virtual environment (recommended):
   - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install packages: `pip install -r requirements.txt`
4. Start the app: `python app.py`

## Customize
- Change the name, biography, skills, project descriptions, and contact details in `templates/index.html`.
- Change the visual design in `static/style.css`.
- Edit interactions in `static/script.js`.
- The skill progress bars are examples; adjust them honestly.
- The sample project cards include planned ideas. Replace them with real work as you complete it.

## Contact form
The form validates the submitted fields and displays a demo message. It does not email or save the message. Connect a trusted email provider or database before publishing it publicly.

## Deployment safety
- Do not deploy Flask's development server or `debug=True` in production.
- Set a strong `SECRET_KEY` environment variable.
- Use a production WSGI server and a trusted Python host.
- Only describe security projects you have permission to perform. Never publish passwords, API keys, or private information.
