#DemoDict.py

device = {"아이폰":5, "윈도우":10}
print(device)
print(len(device))
print(device["아이폰"])

device["맥북"] = 15

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

del device["아이폰"]
print(device)

for v in device.values():
    print(v)

for k in device.keys():
    print(k)