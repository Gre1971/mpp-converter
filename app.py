from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    filename = file.filename
    base_name = os.path.splitext(filename)[0]
    mpp_path = os.path.join('/tmp', filename)
    csv_path = os.path.join('/tmp', base_name + '.csv')

    file.save(mpp_path)

    # כאן תבוא ההמרה האמיתית בעתיד
    with open(csv_path, 'w', encoding='utf-8') as f:
        f.write("task,start,end\nMock Task,2025-01-01,2025-01-10\n")

    return jsonify({
        "message": "File converted",
        "original": filename,
        "converted": base_name + '.csv'
    })

@app.route('/tmp/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('/tmp', filename, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
