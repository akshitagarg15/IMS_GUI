import pymysql

class Connection:
    __Con=None
    def __init__(self):
        self.errormessage=""
        if Connection.__Con is None:
                Connection.__Con=pymysql.connect("localhost","python_275","COOLBUDDY","python275")



    def CloseConnection(self):
        if Connection.__Con is not None:
            Connection.__Con.close()
        Connection.__Con=None

    def GetErrorMessage(self):
        return self.errormessage

    def InsertQuery(self,query):
        try:
            if Connection.__Con is not None:
                cursor=Connection.__Con.cursor()
                cursor.execute(query)
                Connection.__Con.commit ()
                return True
            else:
                self.errormessage="Connection Failure"
                return False
        except BaseException as ex:
            self.errormessage=ex.args[1]
            return False

    def CreateInsertQuery(self,table_Name,column_values):
        query="insert into "+ table_Name +"("
        count=0
        for key in column_values:
            count+=1
            query+=key
            if len(column_values)!=count:
                query+=","
        query+=")values("
        count=0
        for key in column_values:
            count+=1
            Value=column_values[key]
            if isinstance(Value,int) or isinstance(Value,float):
                query+=str(Value)
            else:
                query+="'"+ Value+"'"
            if len(column_values)!=count:
                query+=","
        query+=")"
        return query

    def ExecuteQuery(self,query):
        records=None
        try:
            if Connection.__Con is not None:
                cursor=Connection.__Con.cursor()
                cursor.execute(query)
                records=cursor.fetchall()
            else:
                self.errormessage="Connection Failure"
                return False
        except BaseException as ex:
            self.errormessage=ex.args[1]
        return records



    def CreateUpdateQuery(self,table_Name,column_values,primary_values):
        query="update "+ table_Name +" set "
        count=0
        for key in column_values:
            count+=1
            query+=key +" = "
            value=column_values[key]
            if isinstance(value,int) or isinstance(value,float):
                query+=str(value)
            else:
                query+="'"+value+ "'"
            if len(column_values)!=count:
                query+=","
        query+=" where "
        count=0
        for key in primary_values:
            count+=1
            query+=key+" = "
            Value=primary_values[key]
            if isinstance(Value,int) or isinstance(Value,float):
                query+=str(Value)
            else:
                query+="'"+ Value+"'"
            if len(primary_values)!=count:
                query+=" and "

        return query


    def CreateDeleteQuery(self,table_Name,primary_values):

        query="delete from "+ table_Name +"  where "
        count=0

        for key in primary_values:
            count+=1
            query+=key+"="
            value=primary_values[key]
            if isinstance(value,int) or isinstance(value,float):
                query+=str(value)
            else:
                query += "'" + value + "'"

            if len(primary_values)!=count:
                query+=" and  "
        return query

    def CreateSelectQuery(self, column_values, table_name):
        query = "select "
        count = 0
        for key in column_values:
            count += 1
            query += key
            if len(column_values) != count:
                query += ","
        query += " from " + table_name
        return query


    def CreateJoinQuery(self,column_values,table1,table2):
        query="select "
        count=0
        for key in column_values:
            count += 1
            query += key
            if len(column_values) != count:
                query += ","
        query+=" from "+table1 +" natural join "+ table2
        return query
