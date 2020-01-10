import sys
import os
from PIL import Image, ImageFilter

# grab the first and second arguments
# try:
#     if sys.argv[1]:
#         Name = str(sys.argv[1])

# except:
#     print("no argument given - using DERP")
#     Name = "DERP"


first_arg = sys.argv[1]
sec_arg = sys.argv[2]

print(f' Source folder = {first_arg} \n destination folder = {sec_arg}')

# check if new exists, else create it
if not os.path.exists(sec_arg):
    os.makedirs(sec_arg)
    print("Created the folde")
else:
    print("Folder already exists")
    pass


for filename in os.listdir(first_arg):
    rest = filename.split('.', 1)[0]
    img = Image.open(f'./{first_arg}{filename}')
    img.save(f"./{sec_arg}{rest}.png", 'png')
    print("all done!!!!")
