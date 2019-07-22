f=open("guests.txt", 'w')

for i in range(1,3001):
    str_i=str(i)
    realname="jack"+str_i
    phone=13555555555+i
    email="jack"+str_i+"@email.com"
    sql='INSERT INTO sign_guest(realname,phone,email,sign,event_id) VALUE ' \
        '("'+realname+'",'+str(phone)+',"'+email+'",0,1);'
    f.write(sql)
    f.write("\n")
f.close()