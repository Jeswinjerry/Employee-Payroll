from pymysql import*
con=connect(host="localhost",user="root",password="root1910",database="employe_payroll")

def username(name):
	try:
		q=f"select adminpassword from admin where adminname = '{name}'"
		c=con.cursor()
		c.execute(q)
		result=c.fetchall()
		if result == ():
			status = 500
			response = "User name not found"
			
		else:
			for i in result:
				for j in i:
					response=j#print(j,end="")
			status = 200
		return status,response
	except Exception as e:
		print(f"An error occurred: {e}")
		status=500
		response ='User not found'
		return status,response

def userpassword(password_db,password_ur):
	if password_db==password_ur:
		print("login successfull!")
		status = 200
		response ="login successfull!"
	else:
		status = 500
		response = "Login faild!"
	return status, response	

def einfo(selected_table):
	try:
		empid=int(input("Enter the Emp ID:"))
		empfirstname=input("Enter the Emp First Name:")
		emplastname=input("Enter the Emp Second Name:")
		Dob=input("Enter the date of birth:")
		empmailid=input("Enter the emp mail id:")
		empcontactno=int(input("Enter the contact no:"))
		empaddress=input("Enter the emp address:")
		deptid=int(input("Enter the department id:"))
		position=input("Enter the position:")
		datehired=input("Enter the date of hired:")
		q="insert into empinfo value({0},'{1}','{2}','{3}','{4}',{5},'{6}',{7},'{8}','{9}')".format(empid,empfirstname,emplastname,Dob,empmailid,empcontactno,empaddress,deptid,position,datehired)
		c=con.cursor()
		c.execute(q)
		con.commit()
		con.close()
		status=200
		responce="Data saved..."
		return status,responce
	except Exception as e:
		print(e)
		responce=str(e)
		status=200  
		return status,responce
	
def sinfo(selected_table):
	try:
		empid=int(input("Eneter the emp id:"))
		empfirstname=input("Enter the first name:")
		emplastname=input("Enter the last name:")
		position=input("Enter the emp position:")
		datehired=input("Enter the date hired:")
		salary=int(input("Enter the salary:"))
		dailypay=int(input("Enter the daily pay amount:"))
		annualsalary=int(input("Enter the anuual salary:"))
		bonus=int(input("Eneter the bonus amount:"))
		departmentid=int(input("Enter the department id:"))
		q="insert into salaryinfo value({0},'{1}','{2}','{3}','{4}',{5},'{6}',{7},'{8}','{9}')".format(empid,empfirstname,emplastname,position,datehired,salary,dailypay,annualsalary,bonus,departmentid)
		c=con.cursor()
		c.execute(q)
		con.commit()
		con.close()
		status=200
		responce="Data saved..."
		return status,responce
	except Exception as e:
		print(e)
		responce=str(e)
		status=200  
		return status,responce
#Main function
def main():
	try:
		#get user name
		name=input("Enter the user name:")
		#get password using username function if password present will get password from user or return user not found
		status,response = username(name)
		if status == 200:
			password_ur=input("Enter the user password:")
			status, response = userpassword(response,password_ur)
			if status == 200:
				tables = ["salaryinfo","empolyeinfo"]
				for i, table in enumerate(tables, start=1):
					print(f"{i} table name :{table}")
				choice=input("Enter the table number:")
				choice=int(choice)
				if 1<=choice <=len(tables):
					selected_table=tables[choice -1]
					print(f"you selected :{selected_table}")
				else:
					print("Invalid choice .please enter a valid number..")
				if selected_table =='salaryinfo':
					status,response = sinfo(selected_table)
				else:
					status,response = einfo(selected_table)
		print(response)
	except Exception as e:
		print(f"An error occurred: {e}")
		return str(e)
		
main()
