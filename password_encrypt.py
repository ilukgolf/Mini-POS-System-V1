import hashlib, random, string
def password_encrypt(username, password):
    hash_username = hashlib.sha256(username.encode()).hexdigest()
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    hash_username_password = hash_username + hash_password
    all_hash = hashlib.sha256(hash_username_password.encode()).hexdigest()
    random_str = []
    for ran in range(2):
        random_str.append ( ''.join(random.choice(string.ascii_letters) for ran_to in range(random.randint(5, 10))) )
    final_hash_password = random_str[0] + "$" + hash_username + ";" + all_hash + "$" + random_str[1]
    return final_hash_password

if __name__ == '__main__':
    import main
    main.App()