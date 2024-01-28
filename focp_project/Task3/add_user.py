import sys
import common

def add_user(passwd):
    username = common.get_username()
    if common.user_exists(username, passwd):
        print('Cannot add. Most likely username already exists.')
    else:
        realname = common.get_realname()
        password = common.get_password()
        passwd.append([username, realname, password])
        common.write_passwd_file(passwd)
        print('User Created.')

if __name__ == '__main__':
    passwd = common.read_passwd_file()
    add_user(passwd)