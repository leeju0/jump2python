user_input = input("저장할 내용을 입력하세요: ")
f = open('새파일.txt', 'a')
f.write(user_input)

f.write("\n")
f.close()