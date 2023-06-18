Computers ={
  "Laptop1" : {"brand" : ["DELL"],"OS" : ["Windows"]},
  "Laptop2" : {"brand" : ["HP"], "OS" : ["Linux"]},
  "Desktop" : {"brand" : ["Apple"],"OS" : ["Mac-OS"]}
}
print("brand of laptops:")
for i in Computers:
  print(Computers[i]["brand"][0])

print("os of laptops:")
for i in Computers:
  print(Computers[i]["OS"][0])
