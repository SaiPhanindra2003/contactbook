import pymysql

# entire connection object will stored in conn variable
try:
    con=pymysql.connect(
       host="localhost",
       user="root",
       password="Saiphani@2003"
    )
    print("database connected susessfully")
except Exception as e:
    print("error occured in connection",e)
cursor=con.cursor()


def showcontacts():
    try:
        cursor.execute("use contact_book")
        query="select * from contacts"
        cursor.execute(query)
        rows=cursor.fetchall()
        cursor=con.cursor()
        if len(rows)==0:
            print("no records found")
        else:
            for row in rows:
                print(f"col1_name:{row[0]}")
                print(f"col2_name:{row[1]}")
                print(f"col3_name:{row[2]}")
                print(f"col4_name:{row[3]}")
                print("---------------")
    except Exception as e:
        print("error occured while searching the data")

def create_contact():
        try:
            cursor.execute("use contact_book")
            name=input("enter name:")
            ph_number=input("enter phone number:")
            query="""insert into contacts(name,ph_number) values(%s,%s)"""
            values=(name,ph_number)
            cursor.execute(query,values)
            con.commit()
            cursor.execute("""
            create table contacts(
            name varchar(100),
            ph_number bigint)                                            
            """)
            print("contact created sucessfully")
        except Exception as e:
            print("error occured while creating contact",e)
def update_contact():
        try:
            name=input("enter contact name")
            cursor.execute("use contact_book")
            print("choose 1 for uodate name")
            print("choose 2 for update phone_number")
            choose=int(input("enter the choice"))       
            if choose==1:
                new_name=input("enter new name:")
                query="""update contacts set name =%s where name=%s"""
                cursor.execute(query,(new_name,name))
                print("updated sucessfully")
            elif choose==2:
                new_ph_number=int(input("enter new number:"))
                query="""update contacts set ph_number =%s where name=%s"""
                cursor.execute(query,(new_ph_number,name))
                print("updated sucessfully")
            else:
                print("invalid choose")
        except Exception as e:
            print("unable to update",e)

def search_contact():
        try:
           cursor.execute("use contact_book")
           name=input("enter the name to search")
           query="""select * from contacts where name=%s"""
           cursor.execute(query,name)
           print("contact searched sucessfully")
        except Exception as e:
            print("error occurred while searching the data",e)

def delete_contact():
        try:
           cursor.execute("use contact_book")
           id=int(input("enter the id"))
           query="""delete from contacts where id=%s"""
           cursor.execute(query,id)
           print("contact deleted sucessfully")
        except Exception as e:
            print("error occurred while deleting the data",e)

def menu():
        print("enter 1 for creating contact")
        print("enter 2 for show contacts")
        print("enter 3 for update contacts")
        print("enter 4 for search contacts")
        print("enter 5 for delete contacts")

        choice=int(input("enter ur choice"))
        if choice==1:
            create_contact()
        elif choice==2:
            showcontacts()
        elif choice==3:
            update_contact()
        elif choice==4:
            search_contact()
        elif choice==5:
            delete_contact()
        else:
            print("invalid choice")
menu()   

cursor.close()
con.commit()
        