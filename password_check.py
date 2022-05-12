import hashlib
def password_decrypt(username, password, user_info):
    hash_username = hashlib.sha256(username.encode()).hexdigest()
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    hash_username_password = hash_username + hash_password
    all_hash = hashlib.sha256(hash_username_password.encode()).hexdigest()
    check_username_hash = user_info[14].split(";")[0].split("$")[1]
    check_password_hash = user_info[14].split(";")[1].split("$")[0]
    if check_username_hash == hash_username and check_password_hash == all_hash and user_info[3] == 'locked':
        return 3
    elif check_username_hash == hash_username and check_password_hash == all_hash and user_info[3] == 'inactive':
        return 2
    elif check_username_hash == hash_username and check_password_hash == all_hash and user_info[3] == 'active':
        return 1
    else:
        return 0

if __name__ == '__main__':
    import main
    main.App()