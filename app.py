from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    data = request.json
    name = data.get('name', 'Guest')
    return jsonify({'message': f'Hello, {name}!'}), 200#httpstatuscode

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, ssl_context=('cert.pem', 'key.pem'))#forhttpscertificateissues
