import requests
import json

# Test script for the BFHL API
def test_api(base_url="http://localhost:5000"):
    """
    Test the BFHL API with the examples from the PDF
    """
    print(f"Testing API at: {base_url}")
    print("=" * 50)
    
    # Test cases from the PDF
    test_cases = [
        {
            "name": "Example A",
            "data": ["a","1","334","4","R", "$"]
        },
        {
            "name": "Example B", 
            "data": ["2","a", "y", "4", "&", "-", "*", "5","92","b"]
        },
        {
            "name": "Example C",
            "data": ["A","ABcD","DOE"]
        }
    ]
    
    # Test GET endpoint
    print("\n1. Testing GET /bfhl")
    try:
        response = requests.get(f"{base_url}/bfhl")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n2. Testing POST /bfhl with examples")
    
    for test_case in test_cases:
        print(f"\n--- {test_case['name']} ---")
        
        payload = {"data": test_case["data"]}
        print(f"Request: {json.dumps(payload, indent=2)}")
        
        try:
            response = requests.post(
                f"{base_url}/bfhl",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n3. Testing error handling")
    
    # Test with invalid data
    try:
        invalid_payload = {"invalid_field": "test"}
        response = requests.post(
            f"{base_url}/bfhl",
            json=invalid_payload,
            headers={"Content-Type": "application/json"}
        )
        print(f"Invalid request - Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # You can change this URL to your deployed API URL
    api_url = "http://localhost:5000"  # Change to your deployed URL
    test_api(api_url)