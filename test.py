import requests

# Define the URLs for the endpoints
ADD_NEW_USER_URL = 'http://127.0.0.1:8000/api/add_new_user/'
GET_ID_INFO_URL = 'http://127.0.0.1:8000/api/get_id_info/'

def add_new_user(name, info, image_path):
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        data = {'name': name, 'info': info}
        response = requests.post(ADD_NEW_USER_URL, files=files, data=data)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        
        try:
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            # print(f"Error decoding JSON from response: {response.text}")
            return None
        
        return response_json

def get_id_info(image_paths):
    files = [('images', open(image_path, 'rb')) for image_path in image_paths]
    response = requests.post(GET_ID_INFO_URL, files=files)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    
    try:
        response_json = response.json()
    except requests.exceptions.JSONDecodeError:
        # print(f"Error decoding JSON from response: {response.text}")
        return None
    
    return response_json

if __name__ == "__main__":
    # # Test adding a new user
    # new_user_response = add_new_user("John Doe", "Test user", "me.jpg")
    # print("Add New User Response:", new_user_response)

    # Test getting ID info
    id_info_response = get_id_info(["me.jpg"])
    print("Get ID Info Response:", id_info_response)
