import pymqi

queue_manager = 'QM.01'
channel = 'C.TESTE'
host = '192.168.68.119'
port = '1414'
queue_name = 'QL.TESTE'
conn_info = '%s(%s)' % (host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)

queue = pymqi.Queue(qmgr, queue_name)
message = queue.get()
print(message)
queue.close()

qmgr.disconnect()
