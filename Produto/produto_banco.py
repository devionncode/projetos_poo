import psycopg2

class ProdutoBanco:

    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='produtodb', 
            user='postgres', 
            password='admin', 
            host='localhost', 
            port='5432')