# import
import os
import pygame
from random import *
################################################################
# 기본, 수정없이 그대로 사용하면 된다.
# You can use it as it is without any modification.
pygame.init() 

# 화면 크기 설정 (Set screen size)
screen_width = 480 # 가로pip
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정(set game title)
pygame.display.set_caption("set title") # game name

# FPS init
clock = pygame.time.Clock()
################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
# 이곳에 게임 초기화 코드 추가한다. (Add game initialization code here.)
# Background, gameimg, Coordinates, speed, font, etc ...

# game name
pygame.display.set_caption("똥 피하기")
# Background
background = pygame.image.load("imgs/bath.jpg") # input Path about "bath.jpg

# time
# pygame.time.get_ticks()

# 캐릭터 불러오기
class character:
    def __init__(self,screen_width,screen_height):
        self.character = pygame.image.load("imgs/sonic.png") # input Path about "sonic.png" in img/
        self.size = self.character.get_rect().size # 이미지 크기 구해오기
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = (screen_width / 2) - (self.width / 2) # 캐릭터 위치 x 좌표 : 가로 중앙
        self.y_pos = screen_height - self.height # 캐릭터 위치 y 좌표 : 바닥
        self.speed = 0.3
        # 방향 0:정면 1:왼쪽 2:오른쪽
        self.direction = 0

# 똥 불러오기
class poop:
    def __init__(self,screen_width,screen_height):
        self.poop = pygame.image.load("imgs/poop.png") # input Path about "poop.png" in img/
        self.size = self.poop.get_rect().size # 이미지 크기 구해오기
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = randrange(0,screen_width-self.width)
        self.y_pos = randrange(0,self.height)
        # 떨어지는 속도를 객체마다 랜덤
        self.speed = randrange(1,10)
        # FPS 보정을 위해 실수형으로 변경하고 나누기 10
        self.speed = float(self.speed/10)
    
    # 다음 클래스의 멤버함수가 호출될 때마다 y좌표의 이동을 준다.
    def drop(self):
        # 속도 FPS 보정
        self.y_pos += self.speed*dt
        # 끝까지 떨어져서 화면에서 사라졌을 때 처음 시작 위치, 속도 초기화
        if (self.y_pos >= screen_height):
            self.x_pos = randrange(0,screen_width-self.width)
            self.y_pos = randrange(0,self.height)
            # 떨어지는 속도를 객체마다 랜덤
            self.speed = randrange(1,10)
            # FPS 보정을 위해 실수형으로 변경하고 나누기 10
            self.speed = float(self.speed/10)

# 총 시간
total_time = 30
# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 틱 정보 받아오기

sonic = character(screen_width,screen_height)
poop1 = poop(screen_width,screen_height)
poop2 = poop(screen_width,screen_height)
poop3 = poop(screen_width,screen_height)


# 이동할 좌표
# 좌우 이동 변수를 2가지로 나누었다. 빠르게 키보드를 입력할 시 멈추는 현상을 해결 할 수 있다.
to_x = 0
to_x_left = 0
to_x_right = 0
to_y = 0

# 게임실행
running = True
while running:
    dt = clock.tick(60)
    # 2. 이벤트 처리,키보드,마우스 (Event Handler)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 이곳에 이벤트 처리 코드를 추가(Add Event Handler Code here)
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x_left -= sonic.speed
                sonic.direction=1
            elif event.key == pygame.K_RIGHT:
                to_x_right += sonic.speed
                sonic.direction=2
        if event.type == pygame.KEYUP: #키를 뗐는지 확인 - 왼쪽 키 오른쪽 키각각 처리...
            if event.key == pygame.K_LEFT:
                to_x_left = 0
                sonic.direction=0
            elif event.key == pygame.K_RIGHT:
                to_x_right = 0
                sonic.direction=0
        # 오른쪽 왼쪽 따로 처리한 것을 더함
        to_x = to_x_left + to_x_right
    # 키보드 이벤트 발생 후 캐릭터 이동, 프레임별 보정.
    if sonic.direction == 0:
        sonic.character = pygame.image.load("imgs/sonic.png") # input Path about "sonic.png"
    elif sonic.direction == 1:
        sonic.character = pygame.image.load("imgs/sonic_left.png") # input Path about "sonic_left.png" in img/
    elif sonic.direction == 2:
        sonic.character = pygame.image.load("imgs/sonic_right.png") # input Path about "sonic_right.png" in img/
    sonic.x_pos += to_x * dt # FPS 보정
    # 가로 경계 처리
    if sonic.x_pos < 0:
        sonic.x_pos = 0
    elif sonic.x_pos > screen_width - sonic.width:
        sonic.x_pos = screen_width - sonic.width

    # 똥 좌표 처리(언제든 poop 추가 가능)
    poop1.drop()
    poop2.drop()
    poop3.drop()
    # 3. 게임캐릭터 위치 정의
    # 여기에 게임캐릭터 위치 코드 추가(Add Game Character Location Code here)



    # 4. 충돌 처리
    # 여기에 충돌처리 코드 추가(Add Conflict Handling Code here)
    # 충돌 처리,rect정보 최신화 (왼쪽과 위쪽 기준으로 이미지 좌표 저장되기 때문)
    sonic_rect = sonic.character.get_rect()
    sonic_rect.left = sonic.x_pos
    sonic_rect.top = sonic.y_pos

    poop1_rect = poop1.poop.get_rect()
    poop1_rect.left = poop1.x_pos
    poop1_rect.top = poop1.y_pos

    poop2_rect = poop2.poop.get_rect()
    poop2_rect.left = poop2.x_pos
    poop2_rect.top = poop2.y_pos

    poop3_rect = poop3.poop.get_rect()
    poop3_rect.left = poop3.x_pos
    poop3_rect.top = poop3.y_pos

    # 충돌 체크
    if sonic_rect.colliderect(poop1_rect):
        print("충돌했어요")
        running = False
    elif sonic_rect.colliderect(poop2_rect):
        print("충돌했어요")
        running = False
    elif sonic_rect.colliderect(poop3_rect):
        print("충돌했어요")
        running = False


    # 5. 화면에 그리기
    # 여기에 화면 그리기 코드 추가(Add Screen Drawing Code here)
    # 배경 그리기
    screen.blit(background,(0,0))
    # 캐릭터 그리기
    screen.blit(sonic.character,(sonic.x_pos,sonic.y_pos))
    screen.blit(poop1.poop,(poop1.x_pos,poop1.y_pos))
    screen.blit(poop2.poop,(poop2.x_pos,poop2.y_pos))
    screen.blit(poop3.poop,(poop3.x_pos,poop3.y_pos))

    # 타이머 삽입
    # 경과시간 계산 1000을 나눠서 초(s) 단위로 표시
    elapsed_time = ((pygame.time.get_ticks()) - start_ticks) / 1000
    # int 형 변환으로 소수점 버리기 render는 str형식을 그린다.(출력할 글자,True,글자색상)
    # timer = game_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))
    # screen.blit(timer,(10,10))

    if total_time-elapsed_time <= 0:
        running = False
    ################################################################
    # You can use it as it is without any modification.
    pygame.display.update()
    ################################################################

################################################################
# You can use it as it is without any modification.

# 2초간 대기
pygame.time.delay(2000)

# pygame End
pygame.quit()
################################################################
