def fqdn():
    import socket
    fi=open('fqdn.txt','r')
    fo=open('ip.csv','w')
    fo.write('IP Address'+','+'Host Name'+'\n')
    for i in fi:
        #print i
        try:
            a=socket.gethostbyname(i.strip())
        except:
            a=['Host Name not found',',',i.strip()]
        print a
        fo.write(i.strip()+ ',' +a+'\n')
    fi.close()
    fo.close()

fqdn()
