import os
import cv2

path = "/Users/homefolder/Desktop/proj105/PRO-C105-Project-Images-main"
Images = []
for file in os.listdir (path):
    name,ext = os.path.splitext(file)

    if ext in [".gif",".png",".jpg",".jpeg","jfif"]:
        file_name = path+"/"+file

        print(file_name)
        Images.apped(file_name)
        count = len(Images)
        frame = cv2.imread(Images[0])
        height,width,layers = frame.shape
        size = (width,height)
        print(size)
        out = cv2.VideoWriter("Project.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)
        for I in range (0, count-1):
            frame = cv2.imread(Images[I])
            out.write(frame)

        out.release()
        print("Done")
        