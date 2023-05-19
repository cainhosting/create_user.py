import requests
import argparse
import base64
from urllib.parse import unquote

def create_directadmin_user(username, password, email, domain, custom_template=templatename.conf):
    endpoint = f"https://<your_directadmin_url>:2222/CMD_API_ACCOUNT_USER"
    data = {
        "action": "create",
        "add": "Submit",
        "username": username,
        "email": email,
        "passwd": password,
        "passwd2": password,
        "domain": domain,
        "package": "Package_Name",
        "ip": "IP Assigned To User Accounts",
        "notify": "no"
    }
    admin_username = "admin_username"
	  admin_password = "admin_password"
    auth_string = f"{admin_username}:{admin_password}"
    auth_encoded = base64.b64encode(auth_string.encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_encoded}"
    }
    response = requests.post(endpoint, data=data, headers=headers)
    if response.status_code == 200:
        response_text = response.text.strip()
        decoded_response_text = unquote(response_text)
        if decoded_response_text.startswith("error=0"):
            print(f"User {username} created successfully. Details: {decoded_response_text}")
            if custom_template:
                set_custom_nginx_template(username, custom_template)
        else:
            print(f"Error creating user {username}. Response: {decoded_response_text}")
    else:
        print(f"Error creating user {username}. Status code: {response.status_code}. Response: {response.text}")
		
def set_custom_nginx_template(username, custom_template):
    endpoint = f"https://<your_directadmin_url>:2222/CMD_API_CUSTOM_HTTPD"
    data = {
        "domain": username,
        "action": "save",
        "select0": custom_template
    }
    admin_username = "admin_username"
    admin_password = "admin_password"
    auth_string = f"{admin_username}:{admin_password}"
    auth_encoded = base64.b64encode(auth_string.encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_encoded}"
    }
    response = requests.post(endpoint, data=data, headers=headers)
    if response.status_code == 200:
        response_text = response.text.strip()
        decoded_response_text = unquote(response_text)
        if decoded_response_text.startswith("error=0"):
            print(f"Custom nginx template '{custom_template}' set successfully for user {username}.")
        else:
            print(f"Error setting custom nginx template for user {username}. Response: {decoded_response_text}")
    else:
        print(f"Error setting custom nginx template for user {username}. Status code: {response.status_code}. Response: {response.text}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Create a user via DirectAdmin API")
    parser.add_argument("--username", required=True, help="Username for the new user")
    parser.add_argument("--password", required=True, help="Password for the new user")
    parser.add_argument("--email", required=True, help="Email address for the new user")
    parser.add_argument("--domain", required=True, help="Domain for the new user")
    parser.add_argument("--custom_template", help="Custom nginx template for the new user")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    create_directadmin_user(args.username, args.password, args.email, args.domain)
