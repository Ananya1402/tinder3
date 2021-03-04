'''
DATING APP PROJECT
MADE BY: ANANYA ROY
COLLEGE: GOVT. COLLEGE OF ENGINEERING AND TEXTILE TECHNOLOGY, SERAMPORE
MYWBUT REGISTRATION ID: TECHLWT190179
PROJECT SUBMITTED ON: 30/01/2020
'''

import mysql.connector
class DBHelper:
    '''A private constructor of class DBHelper'''
    def __init__(self):
        try:
            self._connection = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="tinder")
            self._mycursor = self._connection.cursor()
        except:
            print("Could not connect!")

    '''This method searches a table in a database using key-value pair'''
    def search(self,key1,value1,key2,value2,table):
        self._mycursor.execute("SELECT * FROM `{0}` WHERE `{1}` LIKE '{2}' AND `{3}` LIKE '{4}'".format(table,key1,value1,key2,value2))
        response = self._mycursor.fetchall()
        return response

    '''This search method searches a table in a database to check the whether the key contains the required value'''
    def search2(self,table,key,value,type):
        self._mycursor.execute("SELECT * FROM `{0}` WHERE `{1}` {2} '{3}'".format(table,key,type,value))
        response = self._mycursor.fetchall()
        return response

    '''Method to update a table in a database'''
    def update(self,key1,value1,key2,value2,key3,value3,key4,value4,key5,value5,key6,value6,key7,value7,table,user_id):

        try:
            self._mycursor.execute("UPDATE `{0}` SET `{1}` = '{2}', `{3}` = '{4}', `{5}` = '{6}', `{7}` = '{8}', "
                                   "`{9}` = '{10}', `bg` = 'Avatar.jpg', `{11}` = '{12}', `{13}` = '{14}' WHERE `{"
                                   "15}`.`user_id` = '{16}'".format(table,key1,value1,key2,value2,key3,value3,key4,
                                                                    value4,key5,value5,key6,value6,key7,value7,table,
                                                                    user_id))
            self._connection.commit()
            return 1
        except:
            return 0

    '''Method to insert new row in a database'''
    def insert(self, inputDict, table):
        cols = ""
        colValues = ""
        for i in inputDict:
            cols = cols + "`" + i + "`" + ","
            colValues = colValues + "'" + str(inputDict[i]) + "'" + ","

        cols = cols[:-1]
        colValues = colValues[:-1]
        try:
            self._mycursor.execute("INSERT INTO `{0}` ({1}) VALUES ({2})".format(table,cols,colValues))
            self._connection.commit()
            return 1
        except:
            return 0
