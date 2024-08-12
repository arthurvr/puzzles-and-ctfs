import pickle

with open("creds-pickle.dat", "rb") as f:
    x = pickle.load(f)

    pwd = ['']*40
    user = ['']*40

    for pair in x:
        if 'ssh_pass' in pair[0]:
            index = int(pair[0].replace('ssh_pass', ''))
            pwd[index] = pair[1]
        if 'ssh_user' in pair[0]:
            index = int(pair[0].replace('ssh_user', ''))
            user[index] = pair[1]

    print(f"User: {''.join(user)}")
    print(f"Password: {''.join(pwd)}")
