import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from pdf2image import convert_from_path
import pytesseract

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
RESULTS_FOLDER = './results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update if necessary

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = None
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(file_path)

            try:
                # Convert PDF pages to images or process image directly
                images = convert_from_path(file_path)
                extracted_text = ""
                for image in images:
                    extracted_text += pytesseract.image_to_string(image) + "\n"
            except Exception as e:
                extracted_text = f"Failed to process file: {e}"
    return render_template("index.html", extracted_text=extracted_text)

@app.route("/export", methods=["POST"])
def export():
    text = request.form.get("text")
    if text:
        result_path = os.path.join(RESULTS_FOLDER, "ocr_result.txt")
        with open(result_path, "w", encoding="utf-8") as f:
            f.write(text)
        return send_file(result_path, as_attachment=True)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
