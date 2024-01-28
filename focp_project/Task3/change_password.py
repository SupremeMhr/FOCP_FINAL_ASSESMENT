import sys
import common

def change_password(passwd):
    username = common.get_username()
    if not common.user_exists(username, passwd):
        print('User not found.')
    else:
        current_password = common.get_password()
        if not common.check_password(current_password, passwd[common.get_user_index(username, passwd)][2]):
            print('Current password is incorrect.')
        else:
            new_password = common.get_new_password()
            passwd[common.get_user_index(username, passwd)][2] = new_password
            common.write_passwd_file(passwd)
            print('Password changed.')

if __name__ == '__main__':
    passwd = common.read_passwd_file()
    change_password(passwd)