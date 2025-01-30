import os
from flask import request, jsonify
from models.response import ApiResponse
from services.file_service import FileService
from utils.exceptions import FileProcessingError

class FileController:
    def __init__(self, app):
        self.file_service = FileService(app.config['UPLOAD_FOLDER'])
        app.add_url_rule('/upload', 'upload_file', self.upload_file, methods=['POST'])

    def upload_file(self):
        if 'file' not in request.files:
            return ApiResponse.error("No file uploaded", 400)

        file = request.files['file']
        if file.filename == '':
            return ApiResponse.error("No file selected", 400)

        try:
            result = self.file_service.process_file(file)
            return ApiResponse.success({"text": result})
        except FileProcessingError as e:
            return ApiResponse.error(str(e), 500)
