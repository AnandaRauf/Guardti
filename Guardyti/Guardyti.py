import time
from datetime import datetime as waktu

print("---------------------------------------------------------------------------------------\n")
namaaplikasi = "Guardyti (Guard Python Teknologi Informasi)"
devby= "Ananda Rauf Maududi / Retail Tech Source"
devdate="08 Februari 2021"
print(namaaplikasi)
print(devby)
print(devdate)
print("---------------------------------------------------------------------------------------\n")

class MenuGuardyti():
    def menuGuardyti():
        print("Menu Guardyti:\n")
        print
        print("1.Blokir website")
        print("2.Blokir aplikasi")

class blokirapp():
    def webapp(self):
        lokasihost = r"C:\Windows\Systems32\drivers\etc\hosts"
        redirect ="127.0.0.1"
        website1 = input("Masukan website pertama yang ingin diblokir:")
        website2 = input("Masukan website kedua yang ingin diblokir:")
        allwebsite = [website1,website2]
        print("Sukses blokir website ^-^")
        while True:
            if waktu(waktu.now().year, waktu.now().month,waktu.now().day,22) < waktu.now() < waktu(waktu.now().year, waktu.now().month,waktu.now().day,25):
               print("Maaf anda tidak dizinkan hak akses :(")
               with open(lokasihost,'r+') as file:
                   content=file.read()
                   for site in allwebsite:
                       if site in content:
                        pass
                   else:
                      file.write(redirect+""+site+"\n")
                      
                      with open(lokasihost,'r+') as file:
                        content=file.readlines()
                        file.seek(0)
                      for line in content:
                         if not any(site in line for site in allwebsite):
                            file.write(line)
                            file.truncate()
                            print("Anda diizinkan hak akses ^-^")
                         time.sleep(5)
     
    def apps(self):
        lokasihosted = r"C:\Windows\Systems32\drivers\etc\hosts"
        redirected ="127.0.0.1"
        apps1 = input("Masukan website pertama yang ingin di blokir:")
        apps2 = input("Masukan website kedua yang ingin di blokir:")
        allapps = [apps1,apps2]
        print("Sukses blokir website ^-^")
        while True:
            if waktu(waktu.now().year, waktu.now().month,waktu.now().day,22) < waktu.now() < waktu(waktu.now().year, waktu.now().month,waktu.now().day,25):
                print("Maaf anda tidak dizinkan hak akses :(")
            with open(lokasihosted,'r+') as file:
              content=file.read()
              for app in allapps:
                if app in content:
                   pass
              else:
                 file.write(redirected+""+app+"\n")
                 with open(lokasihosted,'r+') as file:
                      content=file.readlines()
                      file.seek(0)
                      for line in content:
                       if not any(app in line for ap in allapps):
                          file.write(line)
                          file.truncate()
                          print("Anda diizinkan hak akses ^-^")
                       time.sleep(3)

MenuGuardyti.menuGuardyti()
pilih = int(input("Mohon pilih menu Guardyti:"))
BlokirApp = blokirapp()
if pilih==1:
    BlokirApp.webapp()

elif pilih==2:
        BlokirApp.apps()
else:
    exit()





