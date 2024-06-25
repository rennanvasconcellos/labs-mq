import pymqi

queue_manager = 'QM.01'
channel = 'C.TESTE'
host = 'QL.TESTE'
port = '1414'
queue_name = 'QL.TESTE'
conn_info = '%s(%s)' % (host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)

queue = pymqi.Queue(qmgr, queue_name)
message = queue.get()
print(message)
queue.close()

qmgr.disconnect()
