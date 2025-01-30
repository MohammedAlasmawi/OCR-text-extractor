import os
from models.pdf_processor import PDFProcessor
from utils.exceptions import FileProcessingError

class FileService:
    def __init__(self, upload_folder):
        self.upload_folder = upload_folder
        self.pdf_processor = PDFProcessor()
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

    def process_file(self, file):
        file_path = os.path.join(self.upload_folder, file.filename)
        try:
            file.save(file_path)
            text = self.pdf_processor.process_pdf(file_path)
            os.remove(file_path)
            return text
        except Exception as e:
            raise FileProcessingError(f"Failed to process file: {str(e)}")
