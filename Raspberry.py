import serial
import serial.tools.list_ports

class Raspberry:
    def __init__ (self, baudrate=9600, timeout=0.1):
        self.port = self.get_com_port()
        self.ser = None 
        if self.port:
            try:
                self.ser = serial.Serial(self.port, baudrate, timeout=timeout)
            except Exception as e:
                self.ser = None
    
    def get_com_port(self):
        ports = list(serial.tools.list_ports.comports())
        com_ports = []

        for p in ports:
            if p.device.startswith('COM'):
                try:
                    num = int(p.device[3:])
                    com_ports.append((num, p.device))
                except ValueError:
                    pass
        if not com_ports:
            return None
        
        com_ports.sort(key=lambda x: x[0], reverse=True)
        return com_ports[0][1]
    
    def readline(self):
        if self.ser and self.ser.in_waiting:
            try:
                line = self.ser.readline().decode().strip()
                return line
            except Exception as e:
                return None
        return None
    
    def close(self):
        if self.ser:
            self.ser.close()
