import re

s = "Ice-Jade Teapot"

s = re.sub('[^0-9a-zA-Z]+', '_', s).replace(" ", "_")

print(s)