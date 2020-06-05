from faker import Faker
import shutil

fake = Faker('en_US')
# print(fake.ascii_free_email())

# print(dir(fake))

# print(fake.paragraph())

content = ''

for _ in range(100):
    content += fake.paragraph() + ' '
    content += fake.email() + ' '
    content += fake.paragraph() + ' '
    content += fake.phone_number() + ' '
    content += fake.paragraph() + ' '
    content += '\n'


print(content)

with open('notes.txt', 'w+') as f:
    f.write(content)