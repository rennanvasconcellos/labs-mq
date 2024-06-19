import pymqi

# Configuração da conexão
queue_manager = pymqi.connect('QM.01', 'C.TESTE', '192.168.68.119(1414)')
q = pymqi.Queue(queue_manager, 'QL.TESTE')

# Criação da mensagem
message = 'Ola Cesinha'

# Criação do Message Descriptor (MD) e do Put Message Options (PMO)
md = pymqi.MD()
pmo = pymqi.PMO()

# Definindo a confirmação de entrega (COA)
md.Report = pymqi.CMQC.MQRO_COA | pymqi.CMQC.MQRO_COD

# Especificando a fila de resposta (substitua 'REPLY_QUEUE' pelo nome da sua fila de resposta)
md.ReplyToQ = b'QL.REPORT'

# Enviando a mensagem com as opções configuradas
print("Starting putmsg")
q.put(message, md, pmo)
print("Putting 1 message into queue")
print("Ending putmsg")

# Fechando a fila e desconectando do Queue Manager
q.close()
queue_manager.disconnect()

