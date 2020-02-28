import subprocess

can1_inst = subprocess.Popen(['candump', 'can1'], stdout = subprocess.PIPE)
#out,err = p.communicate()
CAN1 = open(r"/home/flux/Desktop/CAN1.txt", "w+")
CAN2 = open(r"/home/flux/Desktop/CAN2.txt", "w+")
while True:
	output = can1_inst.stdout.readline()	
	rc = can1_inst.poll()
	#print (output)
	can_msg = output.decode()
	if("can1  01" in can_msg):
		CAN1.writelines(can_msg.replace("can1 ", ""))
	if("can1  02" in can_msg):
		CAN2.writelines(can_msg.replace("can1 ", ""))
CAN1.close();
CAN2.close();
