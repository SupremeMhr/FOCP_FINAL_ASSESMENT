import sys
import common

def login(passwd):
    username = common.get_username()
    password = common.get_password()
    if common.user_exists(username, passwd) and common.check_password(password, passwd[common.get_user_index(username, passwd)][2]):
        print('Access granted.')
    else:
        print('Access denied.')

if __name__ == '__main__':
    passwd = common.read_passwd_file()
    login(passwd)