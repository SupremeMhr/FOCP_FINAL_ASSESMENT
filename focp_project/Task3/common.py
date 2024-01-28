import hashlib
import getpass

def read_passwd_file():
    try:
        with open('passwd.txt', 'r') as f:
            return [line.strip().split(':') for line in f]
    except FileNotFoundError:
        return []

def write_passwd_file(passwd):
    with open('passwd.txt', 'w') as f:
        for u in passwd:
            f.write(f'{u[0]}:{u[1]}:{hashlib.sha256(u[2].encode()).hexdigest()}\n')

def check_password(current_password, encrypted_password):
    return hashlib.sha256(current_password.encode()).hexdigest() == encrypted_password

def get_username():
    return input('User:     ').lower()

def get_password():
    return getpass.getpass('Password:  ')

def get_realname():
    return input('Enter real name:    ')

def user_exists(username, passwd):
    return any(username == u[0] for u in passwd)

def get_user_index(username, passwd):
    return [i for i, u in enumerate(passwd) if u[0] == username][0]

def get_new_password():
    new_password = getpass.getpass('New Password:     ')
    confirm_password = getpass.getpass('Confirm Password: ')
    while new_password != confirm_password:
        print('Passwords do not match.')
        new_password = getpass.getpass('New Password:     ')
        confirm_password = getpass.getpass('Confirm Password: ')
    return new_password

