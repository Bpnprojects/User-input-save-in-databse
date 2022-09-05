from turtle import circle
import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="barcode"
    )
mycursor = db.cursor()



brc= input("Hello, Please Enter the Barcode:  ")
my_data=(brc,)
#q="SELECT * FROM recycle_item"
q="SELECT * FROM recycle_item where Barcode_Id=%s"
try:
  mycursor.execute(q,my_data)
  my_data=mycursor.fetchall()
  for row in my_data:
    print(row)
#except  as e:
 # error=str(e.__dict__['orig'])
  #print(error)
except Exception as e:
    print(e)
else:
     add= input("Do you want to add the barcode (y/n) : ")
     if (str(add).lower() == 'y'):
        bc= input("Please enter the barcode  : ")
        pn= input("Please enter the product  : ")
        ci= input("Please enter the customer Id  : ")
        pt= input("Please enter the product type  : ")
        qt= input("Please enter the product Quanity : ")
        po= input("Please enter the product point  : ")
        pc= int(int(qt)*int(po))
        my_data=(bc,pn,ci,pt,qt,po,pc)
        inser = "Insert INTO recycle_item (Barcode_Id,Product_Name,Cust_ID,Product_Type,Quantity,Product_point,Points_Collected ) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        #SELECT Item_no,Barcode_Id,Product_Name,Product_Type,Quantity,Product_point,Quantity*Product_point as Points_Collected FROM barcode.recycle_item;
        mycursor.execute(inser,my_data)
        db.commit() 
        print("Record saved : ")
   
   