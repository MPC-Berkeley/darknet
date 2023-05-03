import os

image_files = []
os.chdir(os.path.join("/home/meng/Desktop/Perception/Model_Training/darknet/data/", "test"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg") or  filename.endswith(".png"):
        image_files.append("/home/meng/Desktop/Perception/Model_Training/darknet/data/test/" + filename)
os.chdir("..")
with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
