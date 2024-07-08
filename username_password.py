main_dictionary={}

def registration():
    import pymysql
    import random
    import string
    from datetime import date,datetime  #create database user_pass with table login
    connection=pymysql.connect(host="localhost",user="root",password="",database="user_pass")
    pycursor=connection.cursor()        
    name=input("Enter Name: ")          #input from user
    today=date.today()                  #todays date
    print("Birth Date: ")               #input from user
    dd=int(input("dd "))
    mm=int(input("mm "))
    yyyy=int(input("yyyy "))
    try:
        Birth_date=datetime(yyyy,mm,dd)
    
        age=today.year-yyyy                 #age
    
        length_password=10                  #lenght of password
    
        if ((name.isalpha()) and (age>=18)):       #user must enter only alphabets in name and age should be greater than 18
        
            upper_name=name.upper()
            user_number=random.randint(1,1000)
            string_number=str(user_number)
            username=upper_name+string_number      #user name generation: user's name in uppercase + random string number
        
            ran="".join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase+string.punctuation,k=length_password))#make password
        
            keys=main_dictionary.keys()
            for key in keys:
                if(key==username)and(len(keys)<1000):
                    user_number=random.randint(1,1000)
                    string_number=str(user_number)
                    username=upper_name+string_number
            print('USERNAME: ',username)
            print("password: ",str(ran))
            password=str(ran)
            InsertRow="insert into login (Name,Age,Username,Password) values(%s,%s,%s,%s)"
            values=(name,age,username,password)
            pycursor.execute(InsertRow,values) #append data in database
        
        
            connection.commit()
            connection.close()
                
            add_dictionary={username:str(ran)}
            main_dictionary.update(add_dictionary)
        
        elif(age<18):
            print("Age less than 18")
        else:
            print("Enter only alphabets in name")
    except ValueError:
        
        print("Enter date between 1-31,month between 1-12,year positive integers")
    except:
        print("Error")


def login():
      user=input("USERNAME: ")
      user_password=input("PASSWORD: ")
      keys=main_dictionary.keys()
      flag=0
      for key in keys:
          if(key==user):
              if(main_dictionary[key]==user_password):
                  print('welcome ')
              else:
                  print('incorrect password')
          else:
              flag+=1
      if (flag==len(keys)):
          print("Invalid Username")



