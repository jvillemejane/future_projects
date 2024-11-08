from pylablib.devices import Thorlabs

kenesis_list = Thorlabs.kinesis.list_kinesis_devices()
print(kenesis_list)