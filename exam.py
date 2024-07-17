import psycopg2
import threading
import time 

#1 
# \\\QUESTION \\
db_exam = {
    'database':  "n44r",
    'user': 'postgres',
    'password': '123',
    'host': 'localhost',
    'port': 5432
}

conn = psycopg2.connect(**db_exam)
cursor = conn.cursor()

create_product_query = """ 
CREATE TABLE IF NOT EXISTS product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    price NUMERIC NOT NULL,
    color VARCHAR(100) NOT NULL,
    image VARCHAR(100) NOT NULL
)
"""


cursor.execute(create_product_query)
conn.commit()
# 2 \\\question\\\

# product_insert()
def product_insert():
    name = str(input("Enter name:"))
    price = int(input("Enter price:"))
    color = str(input("Enter  color:"))
    image = str(input("Enter  image:"))
    insert_into_query = """INSERT INTO product(name,price,color,image )
    VALUES ( %s,%s,%s,%s);'
    insert_into = (name,price,color,image)"""
    cursor.execute(insert_into_query,insert_into)
    conn.commit()
   


    

# select_all_products()
def select_all_products():
    select_product = 'SELECT * FROM product;'
    cursor.execute(select_product)
    rows = cursor.fetchall()
    for row in rows:
        print(row)



        
#update_product()
def update_product():
    select_all_products()
    _id = int(input("enter id :"))
    name = str(input(" enter name:"))
    price = int(input(" enter price  :"))
    color = str(" enter color:")
    image = str(" enter image :")
    update_query = 'update product set name = %s, price = %s,color =%S,image =%s where id = %s;'
    update_proddd = (_id,name,price,color,image)
    cursor.execute(update_query,update_proddd)
    conn.commit()
    


    
#delete_product()\
def delete_product():
    select_all_products()
    _id = int(input('Enter product id:'))
    delete_query = 'delete from product where id = %s;'
    cursor.execute(delete_query,(_id,))
    conn.commit()
# 3\\\ QUESTION \\\
class albhabet:
       def __init__(self):
            self.letter = "abcdefghijklmnopqrstuvwxyz"
            self.index = 0
        
        
         def __iter__(self):
            return self 
       
        
        
        
         def __next__(self):
            if self.index <len(self.letters):
                 letter = self.letter[self.index]
                 self.index +=1
                 return letter
            else :
                 raise StopIteration
            
alifbe =albhabet()
for latter in alifbe:
     print (latter)
              

#4 \\\ QUESTION\\\ 

def print_number():
     for i in range (1,6):
          print (i)

def print_latters():
    for letter in "ABCDE":
        print(letter)
        time.sleep(1)


number_thread = threading.Thread(target=print_number)
letter_thread = threading.Thread(target=print_latters)


number_thread.start()
letter_thread.start()

number_thread.join()


# 5 \\\QUESTION\\\
class Product:
    def init(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
            connection = psycopg2.connect(
                host="localhost",
                database="n48",
                user="postgres",
                password="123"
            )
            cursor = connection.cursor()

            insert_query = '''
             insert into product (name, price, color, image) 
             values (%s, %s, %s, %s)
            '''
            cursor.execute(insert_query, (self.name, self.price, self.color, self.image))
            connection.commit()


    
            
            cursor.close()
            connection.close()

product = Product('samsung', 1.200, 'black', None)
product = Product('iphone15', 1.500, 'white', None)
product = Product('samsungs24', 1.600, 'black', None)

product.save()

# 6 question |||




class DbConnect:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

with DbConnect(host="localhost", database="n48", user="postgres", password="123") as (conn, cursor):
    cur.execute("SELECT * FROM product")
    products = cursor.fetchall()
    for product in products:
        print(product)

# 7 misol \\\\

import requests 

response = requests.get("https://dummyjson.com/products")
data = response.json()


for item in data['products']:
    name = item['title']
    price = item['price']
    color = item.get('color', 'N/A')  
    image = item.get('thumbnail', None)
    
    product = Product(name, price, color, image)
    product.save()