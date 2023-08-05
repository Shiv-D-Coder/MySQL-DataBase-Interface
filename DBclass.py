import mysql.connector as connector


# HERE WE ARE MAKING CLASS AND METHODS
class mydb:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     user='root',
                                     port=3306,
                                     password='$ShivD37Code',
                                     database='main_sql')
        q1 = "create table if not exists demo (id int, name varchar(20),addres varchar(20));"
        fire = self.con.cursor()
        fire.execute(q1)
        print('TABLE IS CREATED') 
          
# METHOD 1: INSERT INTO TABLE
    def add_into(self,id,name,add):
        q2 = "insert into demo (id,name,addres) values ({},'{}','{}')".format(id,name,add);  
        fire = self.con.cursor()
        fire.execute(q2)
        self.con.commit()
        return True
        
# METHOD 2: FETCHING INTO TABLE
    def fetch(self):
        q3 = "select * from demo;"
        fire = self.con.cursor()
        fire.execute(q3)
        for row in fire:
            print("USERID: ",row[0])
            print("USERNAME: ",row[1])
            print("USERADDRES: ",row[2])
            print()
            print()
        return True
    
# METHOD 3: DELETING FROM TABLE
    def delete(self,userid):
        q4 = "delete from demo where id= {}".format(userid)
        fire = self.con.cursor()
        fire.execute(q4)
        self.con.commit()
        print("DELETED SUCCESSFULLY")
        return True   

        
# METHOD 4: UPDATING VALUES FROM TABLE        
    def toUpdate(self,col1_name,n_name,col2_name,n_add,userid):
        q5 = "update demo set {} = '{}',{} = '{}' where id={}; ".format(col1_name,n_name,col2_name,n_add,userid) 
        fire = self.con.cursor()
        fire.execute(q5)
        self.con.commit()
        return True   
        
        
      
