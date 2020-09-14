import datetime
from database import  DatabaseConnection
connection = DatabaseConnection()
response = []

class ProduceModel(object):
    def __init__(self, current_user, produce_name, quantity, unit_price):
        """
        This constructor initialises category
        :param produce_name: 
        :param quantity:
        :param unit_price:
        """
        self.produce_name = produce_name
        self.quantity = quantity
        self.current_user=current_user
        self.unit_price = unit_price
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = datetime.datetime.utcnow()

    def create_produce(self):
        """
        Adds produce as an object to list
        :return: the produce that has just been added
        """
        try:
            query_to_add_produce = "INSERT INTO farmer_produce(produce_name, quantity, unit_price,users_id ,date_created,date_modified) VALUES(%s,%s,%s,%s,%s,%s)"
            connection.cursor.execute(query_to_add_produce,( self.produce_name,self.quantity, self.unit_price, self.current_user, self.date_created, self.date_modified))
            query_to_search_product = "SELECT * FROM farmer_produce WHERE produce_name=%s"
            connection.cursor.execute(query_to_search_product, [self.produce_name])
            added_produce = connection.cursor.fetchone()
            print("added_produce")
            result = {
                        'id': added_produce[0],
                        'produce_name': added_produce[1],
                        'quantity':added_produce[2],
                        'Unit _price': added_produce[3],
                        }

            return result
            
        except Exception as exc:
            print(exc)
    
    @classmethod        
    def get_farmer_produce(cls):
        """
        This method gets all farmer produce
        :param public_id: 
        :return: all farmer produce in the store
        """
        response =[]
        query_to_get_all_farmer_product = 'SELECT * FROM farmer_produce'
        connection.cursor.execute(query_to_get_all_farmer_product)
        rows = connection.cursor.fetchall()
        if not rows:
            return "Farmer produce not available"
        for row in rows:
            response.append({
                            'id': row[0],
                            'createdby': row[1],
                            'category': row[2],
                            'product':row[3],
                            })
        return response