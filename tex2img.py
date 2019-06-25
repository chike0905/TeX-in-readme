import sys
import re

filename = sys.argv[1]
test_data = open(filename, "r")

pattern = "\$([^\$]*)\$"

for line in test_data:
  result = re.sub(pattern, r'<img src="https://latex.codecogs.com/gif.latex?\1">', line)
  print(result, end="")  

test_data.close()
