import sys

class block:
    def __init__(self, durability:int, isEmpty:bool):
        self.durability = durability
        self.isEmpty = isEmpty

class Robot:
    def __init__(self, num:int, next = None):
        self.num = num
        self.next = next

N, K = map(int, input().split()) # N <= 100
belt = [0]
robot_head = Robot(0)
robot_tail = robot_head
durability = list(map(int, input().split()))
for i in range(N + N):
    belt.append(block(durability[i], True))

leftTop = 1
rightTop = N

def get_pre(num:int):
    global N
    if num == 1:
        return 2 * N
    else:
        return num - 1

def get_next(num:int):
    global N
    if num == 2 * N:
        return 1
    else:
        return num + 1

def get_robot_off():
    global rightTop, belt, robot_head, robot_tail
    if belt[rightTop].isEmpty == True:
        return
    belt[rightTop].isEmpty = True
    temp = robot_head.next.next
    robot_head.next = temp
    if temp == None:
        robot_tail = robot_head

def belt_moves():
    global leftTop, rightTop, N
    leftTop = get_pre(leftTop)
    rightTop = get_pre(rightTop)
    get_robot_off()

def put_robot_on():
    global robot_head, robot_tail, leftTop, belt
    if belt[leftTop].isEmpty == False or belt[leftTop].durability == 0:
        return
    belt[leftTop].isEmpty = False
    belt[leftTop].durability -= 1

    temp = Robot(leftTop)
    robot_tail.next = temp
    robot_tail = temp

def robots_move():
    global robot_head, belt
    temp = robot_head.next
    while temp != None:
        if belt[get_next(temp.num)].durability == 0 or belt[get_next(temp.num)].isEmpty == False:
            temp = temp.next
            continue
        belt[temp.num].isEmpty = True
        temp.num = get_next(temp.num)
        belt[temp.num].durability -= 1
        belt[temp.num].isEmpty = False
        temp = temp.next
        get_robot_off()
            
round = 1
while(True):
    belt_moves()
    robots_move()
    put_robot_on()

    #check durability of all blocks
    cnt = 0
    for i in range(1, 2 * N + 1):
        if belt[i].durability == 0:
            cnt += 1
    if cnt >= K:
        break
    round += 1

print(round)
