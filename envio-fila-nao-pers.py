import pymqi

print("Starting putmsg")

# Conexão ao Queue Manager
queue_manager = pymqi.connect('QM.01', 'C.TESTE', '192.168.68.119(1414)')

# Abertura da fila
q = pymqi.Queue(queue_manager, 'QL.TESTE')

# Definição das opções da mensagem (não persistente)
put_opts = pymqi.pmo()
put_opts.Options = pymqi.CMQC.MQPMO_NO_SYNCPOINT

# Definição das opções da mensagem (não persistente)
md = pymqi.md()
md.Persistence = pymqi.CMQC.MQPER_NOT_PERSISTENT

# Envio da mensagem
q.put('Hello from Python!', md, put_opts)
print("Putting 1 message into queue")

# Fechamento da fila e desconexão do Queue Manager
q.close()
queue_manager.disconnect()

print("Ending putmsg")

