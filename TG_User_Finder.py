
#!/usr/local/bin/python3
# coded by:swagkarna
from telephon import TelegramClient, events, sync
from telephon.tl.types import InputPhoneContact
from telephon import functions, types

def check(phone_number, usr):
    try:
        contact = InputPhoneContact(client_id = 0, phone = phone_number, first_name="__test__", last_name="__last_test__")
        contacts = client(functions.contacts.ImportContactsRequest([contact]))
        username = contacts.to_dict()['users'][0]['username']
        return username
        dell = client(functions.contacts.DeleteContactsRequest(id=[username]))
    except:
        res = "__err__"
        return res

def list_checker():
    list_file = input("List of numbers: ")
    usr = input("Username Target: ")
    list = open(list_file, 'r').read().splitlines()
    for num in list:
        try:
            ress = check(num, usr)
            if ress == '__err__':
                print ("Number: {} <{}>".format(num, "ERROR!"))
            elif ress.lower() == usr.lower():
                f = open("hit.txt", "a")
                f.write(ress+":"+num)
                f.close()
                print ("Number: {} <{}>".format(num, "OK:)"))
                break
            else:
                print ("Null")
        except:
            print ("Null")

if __name__ == '__main__':
    phone = '+19028120412'
    client = TelegramClient(phone, 1890509, '4c7e4382ca697761d7e9056a56498f74')
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    list_checker()
