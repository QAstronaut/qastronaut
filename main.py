from functions.create_postman import create_collection, create_folder, create_request
from functions.fetch_data_postman import fetch_request_data
from functions.welcome import welcome

api_key, collection_name, folder_name = welcome()

new_collection = create_collection(api_key, collection_name)
print("New Collection created:\n")
print(new_collection)

collection_id = new_collection['collection']['id']

new_folder = create_folder(api_key, collection_id, folder_name, collection_name)
print("\nNew Folder created:\n")
print(new_folder)

folder_id = new_folder['collection']['id'] #isso aqui não ficou muito legal porém quando coloquei folder e mexi na função create_folder deu erro

request_name, request_method, request_url, test_script = fetch_request_data()

new_request = create_request(api_key, collection_name, collection_id, folder_name, folder_id, request_name, request_method, request_url, test_script) 
print("\nNew Request created:\n")
print(new_request)

