import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def gerarKey(password):

   file = open('sal','rb')
   sal = file.read()
   file.close()

   kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=sal,
      iterations=480000,
      backend=default_backend()
   )
   key = base64.urlsafe_b64encode(kdf.derive(password))
   return key


option = int(input("Oque você deseja fazer?\n1-Encriptar\n2-Decriptar\n>"))

if(option==1):
   my_password = input("Escolha um password: ").encode()
   key = gerarKey(my_password)

   arquivo = input("Nome do arquivo: ")
   file = open(arquivo,'rb')
   content = file.read()
   file.close()

   f= Fernet(key)
   token = f.encrypt(content)

   with open(arquivo,'wb') as file:
      file.write(token)

if(option==2):
   my_password = input("Qual é a senha? ").encode()

   key = gerarKey(my_password)

   arquivo = input("Nome do arquivo: ")
   file = open(arquivo,'rb')
   content = file.read()
   file.close()

   f= Fernet(key)
   try:
      token = f.decrypt(content)
   except Exception as err:
      print("Senha invalida")
   else:
      with open(arquivo,'w') as file:
         file.write(token.decode())
      print("Operação realizada com sucesso")
   



# token = f.decrypt(token)

