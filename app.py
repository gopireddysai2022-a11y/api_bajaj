from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def process_data(data_array):
    """
    Process the input data array according to the requirements
    """
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with your actual details
        "email": "john@xyz.com",         # Replace with your actual email
        "roll_number": "ABCD123",        # Replace with your actual roll number
        "odd_numbers": [],
        "even_numbers": [],
        "alphabets": [],
        "special_characters": [],
        "sum": "0",
        "concat_string": ""
    }
    
    numbers = []
    alphabets = []
    
    try:
        for item in data_array:
            item_str = str(item)
            
            # Check if item is a number
            if item_str.isdigit():
                num = int(item_str)
                numbers.append(item_str)  # Keep as string as per requirement
                if num % 2 == 0:
                    response["even_numbers"].append(item_str)
                else:
                    response["odd_numbers"].append(item_str)
            # Check if item is alphabetic (single character or string)
            elif item_str.isalpha():
                response["alphabets"].append(item_str.upper())
                # Store individual characters in lowercase for concat_string
                alphabets.extend(list(item_str.lower()))
            # Otherwise, it's a special character
            else:
                response["special_characters"].append(item_str)
        
        # Calculate sum of all numbers
        total_sum = sum(int(num) for num in numbers)
        response["sum"] = str(total_sum)
        
        # Create concat_string: reverse order with alternating caps
        if alphabets:
            reversed_alphabets = alphabets[::-1]
            concat_result = ""
            for i, char in enumerate(reversed_alphabets):
                if i % 2 == 0:
                    concat_result += char.upper()
                else:
                    concat_result += char.lower()
            response["concat_string"] = concat_result
        
    except Exception as e:
        response["is_success"] = False
        response["error"] = str(e)
    
    return response

@app.route('/bfhl', methods=['POST'])
def handle_post():
    """
    POST endpoint that processes the data array
    """
    try:
        # Get JSON data from request
        request_data = request.get_json()
        
        if not request_data or 'data' not in request_data:
            return jsonify({
                "is_success": False,
                "error": "Invalid request format. Expected 'data' field in JSON."
            }), 400
        
        data_array = request_data['data']
        
        if not isinstance(data_array, list):
            return jsonify({
                "is_success": False,
                "error": "Data field must be an array."
            }), 400
        
        # Process the data
        result = process_data(data_array)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500

@app.route('/bfhl', methods=['GET'])
def handle_get():
    """
    GET endpoint for testing
    """
    return jsonify({
        "operation_code": 1
    }), 200

@app.route('/', methods=['GET'])
def home():
    """
    Home route for basic info
    """
    return jsonify({
        "message": "BFHL API is running",
        "endpoints": {
            "POST /bfhl": "Main processing endpoint",
            "GET /bfhl": "Returns operation code"
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)