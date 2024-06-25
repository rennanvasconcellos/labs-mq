import pymqi

queue_manager = 'QM.01'
channel = 'C.TESTE'
host = 'localhost'
port = '1414'
queue_name = 'QL.APP.B'
message = 'Hello from Python!'
conn_info = '%s(%s)' % (host, port)

user = 'mqm-app-b'
password = 'mqm-app-b'

qmgr = pymqi.connect(queue_manager, channel, conn_info, user, password)

queue = pymqi.Queue(qmgr, queue_name)
queue.put(message)
queue.close()

qmgr.disconnect()
