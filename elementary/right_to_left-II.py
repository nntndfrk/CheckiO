f = lambda phrases: ','.join([item.replace('right', 'left')for item in phrases])
print(f(["left", "right", "left", "stop"]))
print(f(["brightness wright",]))
