import random
frame_size = random.randrange(50, 100, 3)
print("Framing with a frame size : ", frame_size)

network_layer = open("sender.txt", "r")
physical_layer = open("frames.txt", "w")
frame_len = 0

physical_layer.write('xH')

# Code for Sender side
# Considering 'x' as the flag byte and ESC as '\0'

while 1:
  byte = network_layer.read(1)
  if not byte:
    break
  
  if frame_len%frame_size == 0 and frame_len != 0:
    byte = 'Tx\nxH' + byte

  if byte == 'x':
    byte = '\\' + byte

  elif byte == '\\':
    byte = '\\' + byte

  physical_layer.write(byte)

  if frame_len%frame_size == 0 and frame_len != 0:
    frame_len = 0
  else: 
    frame_len = frame_len + 1

network_layer.close()
physical_layer.close()

# Code for Receiver side

physical_layer = open("frames.txt", "r")
receiver = open("receiver.txt", "w")

while True:
  line = physical_layer.readline()
  if not line:
    break
  line = line[2:-3]
  s = ""
  for ch in line:
    if ch != '\\':
      s = s + ch
  receiver.write(s)

receiver.close()
physical_layer.close()
