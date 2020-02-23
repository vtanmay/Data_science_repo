import mysql.connector


def getDBConnectionObject(ejdbserver=None,ejdbname=None,ejdbport=None,ejdbuser=None,ejdbpassword=None):
    mydb = mysql.connector.connect(
            host=ejdbserver,
            port=ejdbport,
            user=ejdbuser,
            passwd=ejdbpassword,
            database=ejdbname
    )
    return mydb
def executeSelectQuery(ejdbconnobj=None,ejselectquery=None):
        mycursor = ejdbconnobj.cursor()
        mycursor.execute(ejselectquery)
        myresult = mycursor.fetchall()
        return myresult
def executeInsertQuery(ejdbconnobj=None,ejinsertQuery=None):
        mycursor = ejdbconnobj.cursor()
        mycursor.execute(ejinsertQuery)
        ejdbconnobj.commit()
def executeDeleteQuery(ejdbconnobj=None,ejDelQuery=None):
        mycursor = ejdbconnobj.cursor()
        mycursor.execute(ejDelQuery)
        ejdbconnobj.commit()
def generateInsertQuery(ejtablename=None,ejcolumnarr=None,ejvaluearr=None):
        sql="INSERT INTO "+ejtablename+" "+str(tuple(ejcolumnarr)).replace("'","")+" VALUES "+str(tuple(ejvaluearr))+""
        return sql
def generateDeleteQuery(ejtablename=None,ejWhereConditionColumnNameArr=None,ejWhereConditionColumnValueArr=None):
        sql = "DELETE from " + ejtablename + " where ";part1="";
        for c in range(0,len(ejWhereConditionColumnNameArr)):
                if c <len(ejWhereConditionColumnNameArr)-1:
                  part1=part1+ejWhereConditionColumnNameArr[c]+"='"+ejWhereConditionColumnValueArr[c]+"' and "
                else:
                  part1=part1+ejWhereConditionColumnNameArr[c]+"='"+ejWhereConditionColumnValueArr[c]+"'"
        return sql+part1

def createtable(ejdbconnobj=None,ejtablename=None,ejcolumnarr=None):
        sqlstr1="CREATE TABLE "+ ejtablename +" (id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
        sqlstr2="";sqlstr3=""
        for col in ejcolumnarr:
                sqlstr2=sqlstr2+col+" VARCHAR(100),"
        sqlstr3="reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"
        crtblquery=sqlstr1+sqlstr2+sqlstr3
        mycursor = ejdbconnobj.cursor()
        mycursor.execute(crtblquery)
        ejdbconnobj.commit()

