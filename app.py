from flask import Flask, render_template
from portfolio import CONTENT

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html', p=CONTENT)

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.after_request
def headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
