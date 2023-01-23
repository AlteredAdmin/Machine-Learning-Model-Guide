Here are a few examples of how to collect a dataset of images of objects along with their corresponding coordinates on the screen for object detection:

Using a script: You can write a script that captures screenshots of the screen at regular intervals and saves them to a folder. The script can also use the pyautogui library to get the coordinates of the mouse cursor and save them along with the images.

Using a webcam: If you want to collect images of objects in the real-world, you can use a webcam to capture images and use the opencv library to get the coordinates of the objects in the image.

Using annotation tool: You can use annotation tools such as Labelbox, VGG Image Annotator, RectLabel to label the objects in the images and save the coordinates of the object in the images.
Note:
It's worth noting that collecting a good dataset is the most crucial part of the object detection pipeline. In order to achieve good results, it's important to have a diverse dataset, with a good representation of the objects in various poses, lighting conditions, and backgrounds.