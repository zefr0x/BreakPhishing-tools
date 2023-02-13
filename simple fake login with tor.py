import requests
import random
import string
import time

#url where the username and the password will be sent (include http or https)
url = 'http://???.com/index.php'

#where the username and password will be sent
send_name_to_value= 'username'
send_pass_to_value= 'password'

#how meny fake user you want to send??
repetition = 1000


start_time = time.time()

def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}


    print("tor ip:" + session.get("http://httpbin.org/ip").text)
    print("real ip:" +requests.get("http://httpbin.org/ip").text)

    return session

#start a tor session
tor_session = get_tor_session()



chars = string.digits + string.ascii_letters + '!@#$%^&*()'


#opining names and passwords lists
names = open('./lists/names.list', 'r').read().splitlines()
passwords = open('./lists/passwords.list', 'r').read().splitlines()



for i in range(repetition):
    name_extra_len = random.randint(0, 4)
    pass_extra_len = random.randint(3, 9)

    name_extra = ''.join(random.sample(string.digits, name_extra_len))
    pass_extra = ''.join(random.sample(chars, pass_extra_len))

    if random.randint(0, 2) == 0:
        secend_name = '_' + random.choice(names).lower()
    else:
        secend_name = ''

    username = random.choice(names).lower() + secend_name + name_extra
    password = random.choice(passwords) + pass_extra




    try:
        tor_session.post(url, allow_redirects=False, data={
        send_name_to_value: username,
        send_pass_to_value: password
    })

        print(f'{i}) sent      username--> {username}      password--> {password} \n') 


    except KeyboardInterrupt:
        print(f"\n-     {i} fake user was sent in {round(time.time() - start_time, 2)}s")
        exit()
