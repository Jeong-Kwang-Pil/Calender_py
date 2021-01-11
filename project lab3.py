dates = int(input("한 달 최대 일수 입력 >> ")) #한 달 최대일수를 저장
print("첫 날 1일의 시작 요일 입력") 
day = int(input('(0=일, 1=월, 2=화, 3=수, 4=목, 5=금, 6=토) >> ')) #1일의 사작 요일은 0에서 6까지로 받음
day %= 7 #day = day%7 #6이상을 입력하면 7로 나눈 나머지를 계산

#요일 출력
print('\n',end=' ')
for i in '일월화수목금토' :
    print("%s" %i, end=' ') #%s는 문자열을 뜻함 end=' '로 한 줄에 출력
else:
    print('\n')

cnt = 0
#빈 날짜 출력
if day != 0:
    print('   ' * day, end='')
    cnt += day

#1일부터 말일까지 출력
for i in range(1, dates +1):
    print("%2d" %i, end=' ')
    cnt += 1
    if cnt %7 == 0:
        print()
else:
    print()