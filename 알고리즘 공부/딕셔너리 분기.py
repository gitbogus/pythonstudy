def hello():
    print("hello")

def world():
    print("world")

# 딕셔너리를 이용하면 효율적으로 분기할수 있다.
action = input("h or w 입력")
funct = dict(h = hello, w = world)
funct[action]()

# 보통은 if문을 사용하여 다음과 같이 분기문을 작성한다

# action = "h"

# if action == "h":
#     hello()
# elif action == "w":
#     world()

