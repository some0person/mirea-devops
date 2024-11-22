import psycopg2
from os import environ
from datetime import datetime, timezone


class Products:
    def __init__(self) -> None:
        hostname = environ["DATABASE_HOST"]
        username = environ["POSTGRES_USER"]
        password = environ["POSTGRES_PASSWORD"]
        database = environ["POSTGRES_DB"]
        
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
    
    def __del__(self) -> None:
        self.cur.close()
        self.connection.close()

    def getProducts(self) -> list[dict]:
        self.cur.execute(f"SELECT * FROM products")
        
        data = [{"product_id": element[0],
                "prduct_name": element[1],
                "product_price": element[2],
                "updated_at": element[3],
                "created_at": element[4]} for element in self.cur.fetchall()]

        return data

    def addProduct(self, name: str, price: float) -> None:
        current_time = datetime.now(timezone.utc)
        self.cur.execute(f"""INSERT INTO products (product_name, product_price, updated_at, created_at) 
                             VALUES (%(product_name)s, %(product_price)s, %(updated_at)s, %(created_at)s)""",
                             {
                                 "product_name": name,
                                 "product_price": price,
                                 "updated_at": current_time,
                                 "created_at": current_time
                             })
        
        self.connection.commit()
