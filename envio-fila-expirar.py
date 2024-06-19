import pymqi

# Configuração da conexão
queue_manager = pymqi.connect('QM.01', 'C.TESTE', '192.168.68.119(1414)')
q = pymqi.Queue(queue_manager, 'QL.TESTE')

# Criação da mensagem
message = 'Hello from Python!'

# Criação do Message Descriptor (MD) e do Put Message Options (PMO)
md = pymqi.MD()
pmo = pymqi.PMO()

# Definindo o tempo de expiração em decisegundos (por exemplo, 30 segundos = 300 decisegundos)
expiry_time = 15
md.Expiry = expiry_time

# Enviando a mensagem com as opções configuradas
print("Starting putmsg")
q.put(message, md, pmo)
print("Putting 1 message into queue")
print("Ending putmsg")

# Fechando a fila e desconectando do Queue Manager
q.close()
queue_manager.disconnect()

