import paramiko

def make_me_ssh(func):
    def wrapper(*args, **kwargs):
        host = '151.80.70.41'
        user = 'qauto'
        secret = 'hsgaGDS2$25D1'
        port = 22
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=secret, port=port)
        func(*args, **kwargs)
        client.close()
    return wrapper
