from pymysql import*
con=connect(host="localhost",user="root",passwd="root1910",database="employe_payroll")

def delinfo():
    try:
        name=input("Enter the Emp_First_Name:")
        q="select * from empinfo where Emp_First_Name='{0}'".format(name)
        c=con.cursor()
        r=c.execute(q)
        result=c.fetchone()
        if result:
            for i in result:
                print(i)
        else:
            print("No value found...")
    except Exception as a:
        print(a)

delinfo()    
