import bluetooth  
  
#Ver todos os dispositivos e coloca em uma lista os endereços MAC  
print("Buscando dispositivos")  
nearby_devices = bluetooth.discover_devices()
#Executa e lista os disositivos encontrados
num = 0  
print("Selecione o seu disositivo")  
for i in nearby_devices:  
	num+=1  
	print(str(num) + ": " + bluetooth.lookup_name( i ))  
     
#Permite a seleção do aduino
selection = int(input("> ")) - 1  
bd_addr = nearby_devices[selection]  
port = 1  
  
#Mostra a seleção de usuários
print("Você selecionou: " + bluetooth.lookup_name(nearby_devices[selection]))  
  
# Conectando ao endereço e a porta bluetooth
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )  
sock.connect((bd_addr, port))  

# Enviando a informação via bluetooth 
# Testar self.sock.send(data)
data = "H"  
sock.send(data)  

#data = "L"  
#sock.send(data)  
  
data = sock.recv(1024)  
print(data)  
# Print out appearsto be those of Serial.println and not bluetooth.println  
     
sock.getsockname()  
sock.getpeername()  
  
sock.close()  

