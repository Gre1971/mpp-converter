from flask import Flask, request, jsonify, send_from_directory
import os
import mpparser

app = Flask(__name__)

@app.route("/convert", methods=["POST"])
def convert():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    filename = file.filename
    base_name = os.path.splitext(filename)[0]
    mpp_path = os.path.join("/tmp", filename)
    csv_path = os.path.join("/tmp", base_name + ".csv")

    file.save(mpp_path)

    try:
        project = mpparser.MPPDocument(mpp_path)
        with open(csv_path, "w", encoding="utf-8") as f:
            f.write("id,name,start,end,duration,outline_level,wbs\n")
            for task in project.tasks:
                if task and task.start and task.finish:
                    f.write(f"{task.id},{task.name},{task.start},{task.finish},{task.duration},{task.outline_level},{task.wbs}\n")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "message": "File converted",
        "original": filename,
        "converted": base_name + ".csv"
    })

@app.route("/tmp/<filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory("/tmp", filename, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
