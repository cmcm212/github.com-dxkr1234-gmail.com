todos = []

todos.append({'tno':1, '할일':'파이썬 공부', '종료 여부':False})
todos.append({'tno':2, '할일':'복습', '종료 여부':False})
todos.append({'tno':3, '할일':'혼자 해보기', '종료 여부':False})
tno=4

def print_todos():
    for todo in todos:
        print(todo)
    
def add_todo():
    title = input('할일 입력 : ')
    todos.append({'tno':})

while True:

    print('### 할일 목록 ###')
    print({'1':'목록', '2':'추가', '3':'변경', '4':'삭제', '999':'종료'})
    select = input('메뉴 선택 : ')

    if select=='1':
        print_todos()
    
    elif select=='2':
        print()
    
    elif select=='3':
        print()

    elif select=='4':
        print()

    elif select=='999':
        print('이용해주셔서 감사합니다.')