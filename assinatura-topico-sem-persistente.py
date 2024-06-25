# stdlib
import logging

# PyMQI
import pymqi

logging.basicConfig(level=logging.INFO)

queue_manager = 'QM.01'
channel = 'C.TESTE'
host = 'localhost'
port = '1414'
topic_string = '#'
msg = 'Mensagem modelo topico'
msg2 = msg.encode('utf-8')
conn_info = '%s(%s)' % (host, port)

qmgr = pymqi.QueueManager(None)
qmgr.connect_tcp_client(queue_manager, pymqi.CD(), channel, conn_info)

sub_desc = pymqi.SD()
sub_desc['Options'] = pymqi.CMQC.MQSO_CREATE + pymqi.CMQC.MQSO_RESUME + \
    pymqi.CMQC.MQSO_NON_DURABLE + pymqi.CMQC.MQSO_MANAGED
sub_desc.set_vs('SubName', 'AssinaturaSemPersistencia')
sub_desc.set_vs('ObjectString', topic_string)

sub = pymqi.Subscription(qmgr)
sub.sub(sub_desc=sub_desc)

get_opts = pymqi.GMO(
    Options=pymqi.CMQC.MQGMO_NO_SYNCPOINT + pymqi.CMQC.MQGMO_FAIL_IF_QUIESCING + pymqi.CMQC.MQGMO_WAIT)
get_opts['WaitInterval'] = 10000

data = sub.get(None, pymqi.md(), get_opts)
logging.info('Here is the received data: [%s]' % data)

#sub.close(sub_close_options=pymqi.CMQC.MQCO_KEEP_SUB, close_sub_queue=True)
sub.close()
qmgr.disconnect()
