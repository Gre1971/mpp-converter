from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    filename = file.filename
    filepath = os.path.join('/tmp', filename)
    file.save(filepath)

    # כאן בעתיד תבוא ההמרה האמיתית

    return jsonify({
        "message": "File received and saved",
        "filename": filename
    })
