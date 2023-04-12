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
        pass
