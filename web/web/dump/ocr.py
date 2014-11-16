from antigate import AntiGate

config = {'min_len': '3', 'max_len': '4', 'phrase': '1'}
img_path = '/Users/jason/Downloads/image.jpeg'
gate = AntiGate('64192b381a6a42883ee6af1c21bcfa7a', img_path, send_config=config, domain='eve.cm')
print gate
if str(gate) != '210':
	gate.abuse()
print gate.balance()
