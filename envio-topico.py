import pymqi

queue_manager = 'QM.01'
channel = 'C.TESTE'
host = 'localhost'
port = '1414'
topic_string = 'TP.TESTE/TP.TESTE'
msg = 'Mensagem modelo topico'
msg2 = msg.encode('utf-8')
conn_info = '%s(%s)' % (host, port)

qmgr = pymqi.QueueManager(None)
qmgr.connect_tcp_client(queue_manager, pymqi.CD(), channel, conn_info)

topic = pymqi.Topic(qmgr, topic_string=topic_string)
topic.open(open_opts=pymqi.CMQC.MQOO_OUTPUT)
topic.pub(msg2)
topic.close()
print(msg2)
qmgr.disconnect()


s = "1.3961"
# Converte a string Unicode para bytes
b = s.encode('utf-8')
