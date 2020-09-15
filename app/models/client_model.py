import datetime
from database import DatabaseConnection
connection = DatabaseConnection()
response = []


class ClientModel(object):
    def __init__(self, current_user, produce_name, quantity, price_range):
        """
        This constructor initialises category
        :param produce_name: 
        :param quantity:
        :param price_range:
        """
        self.current_user = current_user
        self.produce_name = produce_name
        self.quantity = quantity
        self.price_range = price_range
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = datetime.datetime.utcnow()

    def create_client_request(self):
        """
        Adds produce as an object to list
        :return: the produce that has just been added
        """
        try:
            query_to_add_client_request = "INSERT INTO client_request(produce_name, quantity, price_range, users_id, date_created,date_modified) VALUES(%s,%s,%s,%s,%s,%s)"
            connection.cursor.execute(query_to_add_client_request, (self.produce_name, self.quantity,
                                                                    self.price_range, self.current_user, self.date_created, self.date_modified))
            query_to_search_client_request = "SELECT * FROM client_request WHERE produce_name=%s"
            connection.cursor.execute(
                query_to_search_client_request, [self.produce_name])
            added_produce = connection.cursor.fetchone()
            result = {
                'id': added_produce[0],
                'produce_name': added_produce[1],
                'quantity': added_produce[2],
                'price_range': added_produce[3],
            }

            return result

        except Exception as exc:
            print(exc)

    @classmethod
    def get_client_requsts(cls):
        """
        This method gets all farmer produce
        :param public_id: 
        :return: all farmer produce in the store
        """
        response = []
        query_to_get_all_client_requests = 'SELECT * FROM client_request'
        connection.cursor.execute(query_to_get_all_client_requests)
        rows = connection.cursor.fetchall()
        if not rows:
            return "Client request not available"
        for row in rows:
            response.append({
                            'id': row[0],
                            'produce': row[1],
                            'quantity': row[2],
                            'unit_price': row[3],
                            })
        return response
