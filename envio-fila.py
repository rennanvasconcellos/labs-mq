import pymqi

print("Starting putmsg")
queue_manager = pymqi.connect('QM.01', 'C.TESTE', '192.168.68.119(1414)')
q = pymqi.Queue(queue_manager, 'QL.TESTE')
q.put('Hello from Python!')
print("Putting 1 message into queue")
print("Ending putmsg")
