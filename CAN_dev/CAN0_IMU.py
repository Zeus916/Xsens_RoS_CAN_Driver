import subprocess

can0_inst = subprocess.Popen(['candump', 'can0'], stdout = subprocess.PIPE)
#out,err = p.communicate()
Xsense_670 = open(r"/home/flux/Desktop/XSENSE-670.txt", "w+")
while True:
	output = can0_inst.stdout.readline()	
	rc = can0_inst.poll()
	can_msg = output.decode()
	if("can0 " in can_msg):
		Xsense_670.writelines(can_msg.replace("can0 ", ""))
Xsense_670.close();
