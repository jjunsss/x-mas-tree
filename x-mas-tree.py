import pygame
import random
import sys
import math

#초기화 #중요!
pygame.init() 

score = "Merry_christmas"
#FPS
clock = pygame.time.Clock()

#화면 크기 설정
screenWidth = 450 #가로크기
screenHeight = 400 #세로크기
screen = pygame.display.set_mode((screenWidth,screenHeight))  #가로, 세로

#배경이미지
black = pygame.Color('#061F3E')
background = screen.fill(black)

#이동할 좌표
toX = 0
toY = 0

#난수 생성
randomY = 30
poSpeed = 20

#트리 만들기 & 트리크기 측정
tree_image = pygame.image.load("many_star.png")
tree_image = pygame.transform.scale(tree_image, (10, 10))   

tree_height = tree_image.get_height()
tree_width = tree_image.get_width()

#별 만들기
star_image = pygame.image.load('star.png')
star_image = pygame.transform.scale(star_image, (10, 10))

big_star_image = pygame.image.load('star.png')
big_star_image = pygame.transform.scale(big_star_image, (50, 50))


y_top = 0

def make_tree(each, x_value, y_top):
    trees = []
    stars = []

    for i in range(each):   # if each = 5 -> total tree = 5 / star = 4
        tree = tree_image.get_rect(left=x_value, top = y_top)
        star = star_image.get_rect(left=x_value+10, top = y_top)
        
        x_value += 20 # tree와 star 사이의 간격
        trees.append(tree)
        if i < (each-1):    #무조건 stars는 tree보다 하나 작은 값이 만들어짐.
            stars.append(star)
        else:
            stars.append(None)
    
    return trees, stars

tree_star = {}

for i in range(23, 0, -1):
    tree_star[23-i] = (make_tree(i, (10 * (23 - i)), y_top - (23 - i) * tree_height))   # 만들 개수 / x_value = 10 간격범위 / 출력하는 값의 높이
last = big_star_image.get_rect(left=200, top= -220 - big_star_image.get_height())


'''원래는 아래에 있던 방식으로 해결 했었음.'''
# trees, stars = make_tree(5, x_1,   y_top - 0 * tree_height) ## y_top = 0
# trees2, stars2 = make_tree(4, x_2, y_top - 1 * tree_height)
# trees3, stars3 = make_tree(3, x_3, y_top - 2 * tree_height)
# trees4, stars4 = make_tree(2, x_4, y_top - 3 * tree_height)
# trees5, stars5 = make_tree(1, x_5, y_top - 4 * tree_height)

# tree_star = {0 :(trees, stars), 1:(trees2, stars2), 2:(trees3, stars3), 3: (trees4, stars4), 4: (trees5, stars5)}

##! snow
snow_list = []


snow_img = pygame.image.load("snow_s30.png")
snow1_size = random.randint(10, 15)
snow_img = pygame.transform.scale(snow_img, (snow1_size, snow1_size))
 
snow_img2 = snow_img.copy()
snow2_size = random.randint(5, 10)
snow_img2 = pygame.transform.scale(snow_img2, (snow2_size, snow2_size))

snow_imgX = snow_img.get_width()
snow_imgY = snow_img.get_height()

## snow list
for i in range(50):
    x = random.randrange(0, screenWidth)
    y = random.randrange(0, screenHeight)
    start = random.randrange(-180, 180)
    snow_list.append([x, y, start])


#Title
pygame.display.set_caption("x-mas")

#폰트 정의
game_font = pygame.font.Font(None,40) #폰트, 크기

#누적을 위한 종료 지정.
y_bottom = screenHeight

def end_define(check_num, end_line, tree, star = None):
    if (tree.top + 10) >= end_line:
        tree.top = end_line - tree_height
        if star is not None:
            star.top = end_line - tree_height
    
#Event
running = True

play = False
while running:  #실행창
    
    clock.tick(60)
    screen.fill(black)

    for event in pygame.event.get(): #어떤 이벤트 발생했는지 판단함
        if event.type == pygame.QUIT:
            runnign = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                play = True
            
    if play is False:
        continue
    
    #! 눈 내리기
    for i in range(len(snow_list)):
        
        if i <= len(snow_list) / 2:
            screen.blit(snow_img, (snow_list[i][0], snow_list[i][1]))       
        else:
            screen.blit(snow_img2, (snow_list[i][0], snow_list[i][1]))
        
        snow_list[i][1] += 0.5
        snow_list[i][2] += 1
        
        if snow_list[i][1] > screenHeight:
            y = random.randint(-50, -10)
            x = random.randint(0, screenWidth)
            snow_list[i][1] = y
            snow_list[i][0] = x
            snow_list[i][2] = random.randint(-180, 100)
            
        snow_list[i][0] += (0.5 * math.sin(math.radians(snow_list[i][2])))
            
    #! 트리 구성요소 내리기
    for i in range(24):
        if i == 23: #귀찮아서 걍 때려박음 마지막에
            if last.top + 50 >= 172:
                last.top = 172-50
                screen.blit(scoree, (screenWidth/4, 30))
            last.top += 2
            screen.blit(big_star_image, last)
            
        else:  
            for tree, star in zip(tree_star[i][0], tree_star[i][1]):
                end_line = y_bottom - (i * tree_height)
                end_define(i, end_line, tree, star) ## stair, end_height
                
                if star == None and tree.top + 10 <= y_bottom:
                    tree.top += 2
                    screen.blit(tree_image, tree)
                
                elif star != None and tree.top + 10 <= y_bottom:     
                    tree.top += 2
                    star.top += 2
                    screen.blit(tree_image, tree)
                    screen.blit(star_image, star)
                    
                
                #누적 출력
                
    print(tree_star[22][0])
    

            
    # 출력할 글자, , 색상
    scoree = game_font.render(str(score), True, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))  #(글자, smooth Edges , 색상 )
    
    

    #screen.blit(background, (0,0)) 
    
    #screen.blit(tree, (treeXpos , treeYpos))
   
    pygame.display.update() #화면 새로고침
