from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import mimetypes
import magic
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        try:
            data = request.json.get('data', [])
            file_b64 = request.json.get('file_b64', '')

            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]
            highest_lowercase = max(
                [item for item in alphabets if item.islower()], default=None)

            file_valid = False
            file_mime_type = None
            file_size_kb = None

            if file_b64:
                try:
                    file_data = base64.b64decode(file_b64)
                    file_valid = True
                    mime = magic.Magic(mime=True)
                    file_mime_type = mime.from_buffer(file_data)
                    file_size_kb = len(file_data) / 1024
                except:
                    pass

            response = {
                "is_success": True,
                "user_id": "ujjwal_sharma_16042003",  # Replace with actual user ID
                "email": "ua7664@srmist.edu.in",  # Replace with actual email
                "roll_number": "RA2111003010310",  # Replace with actual roll number
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
                "file_valid": file_valid,
                "file_mime_type": file_mime_type,
                "file_size_kb": f"{file_size_kb:.2f}" if file_size_kb else None
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({"is_success": False, "error": str(e)}), 400

    elif request.method == 'GET':
        return jsonify({"operation_code": 1}), 200


if __name__ == '__main__':
    app.run(debug=True)
