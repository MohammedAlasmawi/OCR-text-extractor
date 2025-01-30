class ApiResponse:
    @staticmethod
    def success(data, status=200):
        return {"status": "success", "data": data}, status

    @staticmethod
    def error(message, status=500):
        return {"status": "error", "message": message}, status
