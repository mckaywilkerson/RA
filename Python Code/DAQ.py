import visa
import time
import nidaqmx
#import nidaqmx.system

rm = visa.ResourceManager()
print(rm.list_resources())

system = nidaqmx.system.System.local()
for device in system.devices:
    print(device)

#with nidaqmx.Task() as task:
#    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
#    print(task.read())

#my_instrument = rm.open_resource('ASRL6::INSTR')

#my_instrument.read_termination = '\r'
#my_instrument.write_termination = '\r'

#print(my_instrument.read())