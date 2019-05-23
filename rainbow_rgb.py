from graphics import GraphWin, color_rgb, Rectangle, Point, Image, update
import time
from PIL import Image as PILImage
# Timer
start = time.time()

# sqrt(256^3) = 4096, so square of 4096
colours_per_row = 4096

# if we have 5 colours we need to go to x == 5 - 1
r = 0
g = 0
b = 0

x = 0 
y = 0

rgb_ppm = Image(Point(colours_per_row/2, colours_per_row/2), colours_per_row, colours_per_row)

num_colours_set = 0

for r in range(0, 256):
    
    for g in range(0, 256):
        
        for b in range(0, 256):
            # First pixel is x,y = 0,0 and rgb = 0,0,0
            rgb_ppm.setPixel(x, y, color_rgb(r, g, b))
            num_colours_set += 1
            # Increment x until x = the number of colours needed
            x = x + 1
            if x == colours_per_row:
                x = 0
                y = y + 1
                print(x, y, r, g, b)
                
            




rgb_ppm.save("rgb.ppm")

rgb_png = PILImage.open("rgb.ppm")
rgb_png.save("rgb.png", "PNG")


end = time.time()

print("Execution time: " + str(end - start))            
print(num_colours_set)

rgb_png.getattr()