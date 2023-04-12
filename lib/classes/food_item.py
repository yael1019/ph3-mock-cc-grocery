from lib import CONN, CURSOR

class FoodItem:
    # THIS METHOD WILL CREATE THE SQL TABLE #
    @classmethod
    def create_table(cls):
        create_food_items_sql = """CREATE TABLE IF NOT EXISTS food_items (
        id INTEGER PRIMARY KEY, name TEXT, price REAL
        )
        """
        CURSOR.execute(create_food_items_sql)


    # ADD YOUR CODE BELOW #

    def __init__(self, name, price, id = None):
        self.name = name
        self.price = price
        self.id = id
    
    def __repr__(self) -> str:
        return f'<FoodItem id={self.id} name={self.name} price={self.price}>'

    def get_price(self):
        if hasattr(self, '_price'):
            return self._price
        else:
            print('Invalid price has been entered')
    
    def set_price(self, price):
        if isinstance(price, float) and price > 0:
            self._price = price
        else:
            print('Price must be a float larger than 0')

    price = property(get_price, set_price)

    def save(self, increase = 0):
        if self.id:
            self._update(increase)
        else:
            self._create_row()

    def _create_row(self):
        sql = """
            INSERT INTO food_items (name, price)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, [self.name, self.price])
        CONN.commit()
        self.id = CURSOR.execute('SELECT * FROM food_items ORDER BY id DESC').fetchone()[0]

    def _update(self, increase):
        sql = """
            UPDATE food_items
            SET name = ?, price = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, [self.name, self.price + increase, self.id])
        CONN.commit()

    def increase_price(self, increase):
        self.save(increase)
        self.price += increase
        # sql = """
        #     UPDATE food_items
        #     SET price = ?
        #     WHERE id = ?
        # """
        # CURSOR.execute(sql, [self.price + increase, self.id])
        # CONN.commit()

    @classmethod
    def query_all(cls):
        sql = """
            SELECT * FROM food_items
        """
        all = CURSOR.execute(sql).fetchall()
        return [FoodItem(data[1], data[2], data[0]) for data in all]

    @classmethod
    def query_average_price(cls):
        all = FoodItem.query_all()
        prices = [food.price for food in all]
        return sum(prices) / len(prices)
