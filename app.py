from __future__ import annotations

from flask import Flask, jsonify, render_template_string

APP_TITLE = 'CRM Bán Hàng SME'

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get('/')
    def dashboard():
        return render_template_string('<h1>{{ title }}</h1><p>Ứng dụng demo đang hoạt động.</p>', title=APP_TITLE)

    @app.get('/health')
    def health():
        return jsonify({'status': 'ok', 'title': APP_TITLE})

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
