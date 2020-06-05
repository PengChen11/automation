from automation.automation import *

def test_phone_txt():
    find_phone_num('./assets/potential-contacts.txt')
    with open('./assets/phone.txt') as phone_file:
        line=phone_file.readlines()
    assert len(line) == 101


def test_email_txt():
    find_email('./assets/potential-contacts.txt')
    with open('./assets/email.txt') as email_file:
        line=email_file.readlines()
    assert len(line) == 115