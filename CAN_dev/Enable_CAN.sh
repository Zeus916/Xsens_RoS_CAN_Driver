sudo modprobe can
sudo modprobe can_raw
sudo modprobe mttcan

busybox devmem 0x0C303000 32 0x0000C400
busybox devmem 0x0C303008 32 0x0000C458
busybox devmem 0x0C303010 32 0x0000C400
busybox devmem 0x0C303018 32 0x0000C458

ip link set can0 down
ip link set can1 down
ip link set can0 type can bitrate 1000000 berr-reporting on
ip link set can1 type can bitrate 1000000 dbitrate 5000000 berr-reporting on fd on

ip link set can0 up
ip link set can1 up
