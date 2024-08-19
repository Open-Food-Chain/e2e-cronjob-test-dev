import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_integration_test_endpoint(base_url):
    # Define the endpoint URL
    url = f"{base_url}"
    
    try:
        # Make a GET request to the /integration_test endpoint
        response = requests.get(url)
    
        # Parse the JSON response
        data = response.json()
        
        print(data)

        # Check if the status code is 200 (OK)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


        # Check that the message key is in the response and has the expected value
        assert 'message' in data, f"Expected key 'message' not found in the response"
        assert data['message'] == "nice", f"Expected message 'nice', but got '{data['message']}'"
        
        print("All checks passed for the /integration_test endpoint.")

    except requests.exceptions.RequestException as e:
        print(f"Test failed: {e}")
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"Test failed: An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Get the base URL from the environment variable
    base_url = os.getenv("PIPELINE_BACKEND_URL")
    test_integration_test_endpoint(base_url)