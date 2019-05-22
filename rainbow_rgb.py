from graphics import GraphWin, color_rgb, Rectangle, Point, Image, update
import time

length = 4096

# if we have 5 colours we need to go to x == 5 - 1
win = GraphWin("rainbow", length, length, autoflush=False)
r = 0
g = 0
b = 0

x = 0 
y = 0

rgb = Image(Point(length/2, length/2), "white.png")
rgb.draw(win)


for r in range(0, 1):
    
    for g in range(0, 256):
        
        for b in range(0, 256):
            x = x + 1
            if x == length - 1:
                x = 0
                y = y + 1
                print(x, y, r, g, b)
                update()
            
            
            rgb.setPixel(x, y, color_rgb(r, g, b))
        



# Y
rgb.save("rgb.ppm")
            
win.getMouse()