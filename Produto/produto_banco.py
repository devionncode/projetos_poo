import psycopg2

class ProdutoBanco:

    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='produto', 
            user='admin', 
            password='admin', 
            host='localhost', 
            port='5432')