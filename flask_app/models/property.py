from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Property:
    db_name="property"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.information = db_data['information']
        self.under30 = db_data['under30']
        self.date_made = db_data['date_made']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO property (name, description, information, under30, date_made, user_id) VALUES (%(name)s, %(description)s, %(information)s, %(under30)s, %(date_made)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM property WHERE id = %(id)s"
        results =  connectToMySQL(cls.db_name).query_db(query, data)
        return results[0] 

    @classmethod
    def update(cls, data):
        query = "UPDATE property SET name=%(name)s, description =  %(description)s, information=%(information)s, under30=%(under30)s, date_made =%(date_made)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM property;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_property= []
        for row in results:
            all_property.append(row)
        return all_property
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM property WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_property(property):
        is_valid = True
        if len(property['name'])<3:
            flash('Name of the property must be at least 3 characters', "property")
            is_valid=False
        if len(property['information'])<3:
            flash('Information must be at least 3 characters', "property")
            is_valid=False
        if len(property['description'])<3:
            flash('Description must be at least 3 characters', "property")
            is_valid=False
        if property['date_made'] == "":
            flash('Please enter a date', "property")
            is_valid=False
        return is_valid
    
    