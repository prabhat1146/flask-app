from flask import Flask,render_template,request
import mysql.connector
application = Flask(__name__)

try:
   
    # application.config['MYSQL_HOST']='database-1.cfdjejptjfup.ap-south-1.rds.amazonaws.com'
    # application.config['MYSQL_USER']='admin'
    # application.config['MYSQL_PASSWORD']='admin123'
    # application.config['MYSQL_DB']='users'
    # print("connecting...")
    host='database-1.cfdjejptjfup.ap-south-1.rds.amazonaws.com'
    
    database='users'
    user='admin'
    password='admin123'

    
    # cursor = connection.cursor()
    # print("connected")
except:
    print("")



@application.route('/api/signup/submit',methods=['GET','POST'])
def hello_world():
    x=0
    try:
        connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        if request.method=='POST':
            username=request.form['name']
            email=request.form['email']
            cur=connection.cursor()
            x = cur.execute("INSERT INTO signup (name, email) VALUES (%s, %s)",(username, email))

            connection.commit()
            cur.close()
    except:
        return render_template('error.html')
    if x==0:
        return render_template('error.html')
    else:
        return  render_template('success.html')
    

@application.route('/')
def myApp2():
    return render_template('index.html')

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)