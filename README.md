# 📄 OCR Text Extraction App

## Overview
This is a **Flask-based OCR (Optical Character Recognition) application** that extracts text from **PDF, JPEG, PNG, and JPG files** using **Tesseract OCR**. The app allows users to **upload a file, extract text, and export the result as a `.txt` file**.

---

## 🚀 Features

✅ **Upload and process PDF or image files**  
✅ **Extract text using Tesseract OCR**  
✅ **Convert PDFs to images for text extraction**  
✅ **Download extracted text as a `.txt` file**  
✅ **Simple and responsive web interface**  

---

## 🏗 Project Structure

📂 uploads/ # Stores uploaded files 📂 results/ # Stores extracted text results 📂 static/css/ # Stylesheets for frontend 📂 templates/ # HTML templates 📜 app.py # Main Flask application 📜 filecontroller.py # Handles file upload requests 📜 file_service.py # Manages file processing logic 📜 pdf_processor.py # Extracts text from PDFs using OCR 📜 response.py # Standardized API response format 📜 style.css # Frontend styling 📜 index.html # User interface for file upload & text display


---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ocr-text-extraction.git

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Install Tesseract OCR

Windows: [Download Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

Linux (Ubuntu/Debian):
sudo apt install tesseract-ocr

Mac (Homebrew):
brew install tesseract

4️⃣ Set the Tesseract Path (Windows Only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

5️⃣ Run the Application
python app.py






















