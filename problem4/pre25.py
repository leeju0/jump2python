f1 = open("새파일.txt","w")
f1.write("Lif is too short")


f1.close()
f2 = open("새파일.txt","r")
print(f2.read())


f2.close()