import re
import shutil

def find_phone_num(path):
    '''find phone number in a giving file with path, write it to assets folder, phone.txt file in ascending order, with no duplications'''
    filter = r'[(]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})'
    with open(path) as potential:
        file = potential.read()

    phone = set(re.findall(filter, file))#remove duplications
    modified_phone = list(phone)
    modified_phone.sort()
    
    numbers = ''
    for i in modified_phone:
        number = '-'.join(i)
        numbers+=number+'\n'

    with open('./assets/phone.txt','w+') as phone_file:
        phone_file.write(numbers)


def find_email(path):
    '''find email address in a giving file with path, write it to assets folder, email.txt file in ascending order, with no duplications'''
    filter = r'\w+[._]*\w+@\w+[-]*\w+\.(?:com|org|info|net|biz)'
    with open(path) as potential:
        file = potential.read()

    email = set(re.findall(filter, file))#remove duplications
    modified_email = list(email)
    modified_email.sort()
    
    emails = ''
    for email in modified_email:
        emails+=email+'\n'

    with open('./assets/email.txt','w+') as email_file:
        email_file.write(emails)


if __name__ == "__main__":
    find_phone_num('./assets/potential-contacts.txt')
    find_email('./assets/potential-contacts.txt')
