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

# נדרש על ידי Render כדי להאזין לפורט מתאים
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
