import psycopg2
import hashlib
from faker import Faker
import random2
import pandas as pd

conn = psycopg2.connect(
    host="10.235.81.97",
    database="CodeGames",
    user="postgres",
    password="Demo123$",
    port="8083"
)

cur = conn.cursor()
cur.execute("Select * FROM customer_prod limit 10" )
rows = cur.fetchall()

columns = input('Give column names to mask as csv:')
type = input('give the following column type respectively as csv [Name, Address, Email, ID, Mobile, Text]:')

def mask_email(email):
    # email = email.replace(",'NA@NA')
    if '@' in email:
        username, domain = email.split("@")
        masked_username = username[:3] + "*" * 5 + username[-3:]
        return masked_username + "@" + domain
    else:
        return email

def scramble_string(input_string):
    # Convert the input string to a list of characters
    if input_string == 'None':
        return input_string
    else:
        char_list = list(input_string)   
        # Shuffle the list of characters randomly
        random2.shuffle(char_list)
        # Join the shuffled characters back into a string
        scrambled_string = ''.join(char_list)
        return scrambled_string

# def datamask(rows,columns,type):

# print(columns)
mask_column_names = columns.split(',')
# print(type)
mask_type = type.split(',')

# print(mask_column_names)
# print(mask_type)

map = dict(zip(mask_column_names, mask_type))

# print(result_dict)

message = b'This is a secret message.'
sha256 = hashlib.sha256()
fake = Faker()
sha256.update(message)

encrypted_data = []


column_headers = [desc[0] for desc in cur.description]

df = pd.DataFrame(rows, columns=column_headers)

for column in mask_column_names:
    column_type = map[column]
    df[column] = df[column].astype(str)

    if column_type == 'Email':
        df[column] = df[column].apply(
        lambda x: 
        mask_email(x)
        )
    if column_type == 'Mobile':
        df[column] = df[column].apply(
        lambda x: 
        scramble_string(x)
        )
    if column_type == 'ID' or column_type == 'Text':
        df[column] = df[column].apply(
        lambda x: 
        hashlib.sha256(x.encode()).hexdigest()
        )
    if column_type == 'Name':
        df[column] = df[column].apply(
        lambda x: 
        fake.name().split(' ')[0]
        )
    if column_type == 'Address':
        df[column] = df[column].apply(
        lambda x: 
        fake.address()
        )
            
print(df['first_name'])

conn.close()

