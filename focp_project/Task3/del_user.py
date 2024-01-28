import sys
import common

def del_user(passwd):
    username = common.get_username()
    if not common.user_exists(username, passwd):
        print('User not found.')
    else:
        passwd.pop(common.get_user_index(username, passwd))
        common.write_passwd_file(passwd)
        print('User Deleted.')

if __name__ == '__main__':
    passwd = common.read_passwd_file()
    del_user(passwd)