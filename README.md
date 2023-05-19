# create_user.py
Create a DirectAdmin user account and assign a custom nginx template using python via CLI.

Create File create_user.py
chmod +x create_user.py






Changes you will need to make:

Update custom_template={templatename}.conf  > Find your custom nginx template here: /usr/local/directadmin/custombuild/custom/nginx_templates/
Update endpoint = f"https://<your_directadmin_url>:2222/CMD_API_ACCOUNT_USER"
"package": "Package_Name",
"ip": "IP Assigned To User Accounts",

admin_username = "admin_username"
admin_password = "admin_password"

Run with python create_user.py --username {username} --email {email_address} --password {password} --domain {domain_name}
