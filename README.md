# create_user.py
Create a DirectAdmin user account and assign a custom nginx template using python.

Find your custom nginx template here: /usr/local/directadmin/custombuild/custom/nginx_templates/

Update custom_template={templatename}.conf

Run with python create_user.py --username {username} --email {email_address} --password {password} --domain {domain_name}
