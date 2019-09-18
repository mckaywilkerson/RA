#import time
import nidaqmx
#import nidaqmx.system

system = nidaqmx.system.System.local()
for device in system.devices:
    print(device)

while (1):
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        temp = float(task.read()) * 16.562 - 12.369
        print(temp)