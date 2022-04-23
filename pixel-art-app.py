from pygame import *
from random import randint
init()

zoom = 1 # Fist launch zoom level
image_size = 40
height, width = 1910, 1080
default_color = (170,140,170)
test_mode = False # Set to True if you are testing this on a computer // It only makes the size smaller
circle_buttons = [(0.9,0.5),(0.1,0.5),(0.5,0.85),(0.5,0.15),(0.08,0.15,0.05),(0.08,0.85,0.05)]
rect_buttons = [[0.3,0.75,0.15,(255,255,255)],[0.3,0.3,0.15],[0.7,0.3,0.1]]
border = 3

if test_mode: height,width = height//2,width//2

random = lambda : randint(0,255)
rand_color = lambda : (random(),random(),random())
screen = display.set_mode((width,height))

tools_height = height-width
drawboard = Surface((width,width))
tools = Surface((width,tools_height))

make_pixels = lambda a: [[a() for y in range(image_size)] for x in range(image_size)]
pixels = make_pixels(lambda:(255,255,255))
text_surf = lambda t,s=50: font.Font('freesansbold.ttf',s).render(t, True, (0,0,0))

circle_buttons_icons = [text_surf(t) for t in [' >','<',' ^ ',' ^ ']]+[text_surf(t,33) for t in ['+','-']]
circle_buttons_icons[2]= transform.rotate(circle_buttons_icons[3],180)
rect_buttons_icons = [text_surf(t[0],t[1]) for t in {'':50,'P':50,'R':35}.items()]

def draw_rec(x,y,color,size):
    if x*size<=width:
        if y*size<=width:
            draw.rect(drawboard,color,Rect(size*x,size*y,size-1,size-1))

def refresh_board():
    unit_size = width*zoom/image_size
    drawboard.fill((0,0,0))
    for x in range(len(pixels[0])):
        for y in range(len(pixels)):
            draw_rec(x-stx,y-sty,pixels[x][y],unit_size)

def draw_tools():
    tools.fill((255,255,255))
    draw.rect(tools,(255,225,255),Rect(width*0.05,tools_height*0.05,width*0.9,tools_height*0.9))
    # drawing circle_buttons
    for t,i in zip(circle_buttons,range(len(circle_buttons))):
        radius = width*0.1 if len(t)==2 else width*t[2]
        draw.circle(tools,default_color,(width*t[0],tools_height*t[1]),radius)
        if i<len(circle_buttons_icons): tools.blit(circle_buttons_icons[i],Rect(width*t[0]-radius/2, tools_height*t[1]-radius/2,radius,radius))
    # drawing rect_buttons
    for t,i in zip(rect_buttons,range(len(rect_buttons))):
        a = width*0.1 if len(t)<3 else width*t[2]
        color = default_color if len(t)<4 else t[3]
        draw.rect(tools,default_color,Rect(width*t[0]-a/2-border,tools_height*t[1]-a/2-border,a+border,a+border))
        draw.rect(tools,color,Rect(width*t[0]-a/2,tools_height*t[1]-a/2,a,a))
        if i<len(rect_buttons_icons): tools.blit(rect_buttons_icons[i],Rect(width*t[0]-a/4, tools_height*t[1]-a/4, a, a))

def get_tool(pos):
    for t in circle_buttons:
        if len(t)==2:
            x,y=t
            r = 0.1
        else:
            x,y,r=t
        if (x-r)*width<pos[0]<(x+r)*width:
            if (y-r)*tools_height<pos[1]-width<(y+r)*tools_height:
                return circle_buttons.index(t)


    for t in rect_buttons:
        if len(t)>3:
            x,y,a,c=t
        elif len(t)>2:
            x,y,a=t
        else:
            x,y=t
            a = 0.1
        if (x-a)*width<pos[0]<(x+a)*width:
            if (y-a)*tools_height<pos[1]-width<(y+a)*tools_height:
                return len(circle_buttons)+rect_buttons.index(t)




def color_pixel(pos,color):
    if pos[1]>width: return
    unit_size = width*zoom/image_size
    pos = (pos[0]+stx*unit_size, pos[1]+sty*unit_size)
    x,y=0,0
    for i in range(len(pixels[0])):
        if pos[0]<i*unit_size: break
        x = i

    for i in range(len(pixels)):
        if pos[1]<i*unit_size:
            break
        y=i

    pixels[x][y]=color

def stal(pos,color):
    if pos[1]>width: return

    for x in range(len(pixels)):
        for y in range(len(pixels)):
            pixels[x][y]=color

colors = [
    (255,255,255),
    (255,0,0),
    (0,255,0),
    (0,0,255),
    (255,255,0),
    (255,0,255),
    (0,255,255),
    (0,0,0)
]
modes = ['P','S','F']


stx,sty,ci,mi=0,0,0,0
color, mode=colors[ci],modes[mi]
pressing=False
clock = time.Clock()

# main app
refresh_board()
draw_tools()
while True:
    for e in event.get():
        if e.type==QUIT:
            exit()
        if e.type == MOUSEBUTTONDOWN:
            pressing = True
            tool = get_tool(mouse.get_pos())
            if tool == 4:
                zoom*=2
            if tool == 5:
                zoom = 1 if zoom < 3 else zoom//2
            if tool == 6:
                ci+=1
                color = colors[ci%len(colors)]
                rect_buttons[0][-1]=color
                draw_tools()
            if tool == 7:
                mi+=1
                mode=modes[mi%len(modes)]
                rect_buttons_icons[1]=text_surf(mode)
                draw_tools()
            if tool==8:
                pixels = make_pixels(rand_color)
            if mode=='P':
                color_pixel(mouse.get_pos(),color)
            if mode=='S':
                stal(mouse.get_pos(),color)
        if e.type == MOUSEBUTTONUP:
            pressing=False
            if pressing:
                if tool == 0:
                    stx+=1
                if tool ==1:
                    stx-=1
                if tool == 2:
                    sty+=1
                if tool == 3:
                    sty-=1
                if stx>len(pixels)*(1-1/zoom):
                    stx=len(pixels)*(1-1/zoom)
                if sty>len(pixels)*(1-1/zoom):
                    sty=len(pixels)*(1-1/zoom)
                if stx<0:
                    stx=0
                if sty<0:
                    sty=0
                if mode=='F':
                    color_pixel(mouse.get_pos(),color)
        refresh_board()
        screen.blit(drawboard,(0,0))
        screen.blit(tools,(0,width))
        clock.tick(45)
        display.update()
