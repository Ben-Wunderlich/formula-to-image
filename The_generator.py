
from PIL import Image
import random
data = [random.randint(0, 1) for i in range(64 * 64)]

img = Image.new('1', (64, 64))
img.putdata(data)
img.save('my.png')
img.show()