import datetime
from database import  DatabaseConnection
connection = DatabaseConnection()

response = []

class UserModel():
    @staticmethod
    def register_user(name, email, password, role):
        """
        This method registers a user
        :param name:
        :param email:
        :param password:
        :param role:
        :return: 
        """
        try:
            query_to_check_for_email = "SELECT * FROM users WHERE email=%s"
            connection.cursor.execute(query_to_check_for_email, [email])
            row = connection.cursor.fetchone()
            if not row:
                register_user_query = " INSERT INTO users(name, email, password, role) VALUES (%s,%s,%s,%s)"
                connection.cursor.execute(register_user_query,(name, email, password, role))
                
                query_to_check_for_inserted_user = "SELECT * FROM users WHERE email=%s"
                connection.cursor.execute(query_to_check_for_inserted_user, [email])
                row = connection.cursor.fetchone()
                if not row:
                    return "No results to fetch"
                print(row)
                response = {
                    'id':row[0],
                    'name':row[1], 
                    'email':row[2],
                    'role' :row[4]
                    }
                return response        
            return "Email already exists"
        except Exception as exc:
            print(exc)

    @staticmethod
    def get_users():
        """
        This method gets all users
        :param: 
        :return: all users
        """
        response = []
        try:
            query_to_search_users = "SELECT * FROM users"
            connection.cursor.execute(query_to_search_users)
            rows = connection.cursor.fetchall()
            if not rows:
                return "No Users"
            for eachrow in rows:
                response.append({
                    'id':eachrow[0],
                    'name':eachrow[1], 
                    'email':eachrow[2],
                    'role' :eachrow[4]
            })
            return response
        except Exception as exc:
            print(exc)
      
    @staticmethod
    def check_if_is_valid_user(email):
        """
        This method logs in a user
        :param email: 
        :param password: 
        :return: 
        """
        try:
            query_to_check_for_user = "SELECT * FROM users WHERE email=%s"
            connection.cursor.execute(query_to_check_for_user, [email])
            row = connection.cursor.fetchone()
            if not row:
                return "user not found"
            return row
        except Exception as exc:
            print(exc)
    
    @staticmethod
    def get_user_by_id(search_id):
        try:
            query_to_search_user = "SELECT * FROM users WHERE users_id=%s"
            connection.cursor.execute(query_to_search_user,[search_id])
            row = connection.cursor.fetchone()
            if not row:
                return "No such user, check id"
            response = [{
                    'id':row[0],
                    'name':row[1], 
                    'email':row[2],
                    'role' :row[4]
                    }]
            return response[0]
        except Exception as exc:
            print(exc)