import tkinter as tk
import cv2
import numpy as np
from keras.models import load_model
classifier = load_model(r'E:\OMKARS\OMKARS1\PROJECTS\PAINT_TOOOL\complete_code\SignR_model.h5')
basepath='E:/OMKARS/OMKARS1/PROJECTS/PAINT_TOOOL/complete_code'


window=tk.Tk()
filename = tk.PhotoImage(file = "E:/OMKARS/OMKARS1/PROJECTS/PAINT_TOOOL/complete_code/paint_sym1.png")
background_label = tk.Label(window, image=filename)
background_label.place( relwidth=1, relheight=1)

window.configure(background='white')
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
#window.grid_rowconfigure(0, weight=1)
#window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="_"*9+"Real Time Paint Tool Box"+"_"*9, bg="black", fg="white", width=100, height=2,
                    font=("Tempus Sans ITC",19,"bold"))

message.place(x=0, y=0)

def sign_recognize():

 
    classifier = load_model(basepath + '/SignR_model.h5')

    def predictor():
        import numpy as np
        from keras.preprocessing import image
        test_image = image.load_img(basepath + '/1.png', target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = classifier.predict(test_image)
   
        if result[0][0] == 1:
            return 'A'
        elif result[0][1] == 1:
            return 'B'
        elif result[0][2] == 1:
            return 'C'
        elif result[0][3] == 1:
            return 'D'
        elif result[0][4] == 1:
            return 'E'
        
    cam = cv2.VideoCapture(0)
#    update_label("Press << c >> for Gesture Detection with Voice")

    img_text = ''
    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame,1)
#        update_label("Press << c >> for Gesture Detection with Voice")

        l_h = 0
        l_s = 0
        l_v = 0
        u_h = 179 
        u_s = 255
        u_v = 152 
    
        img = cv2.rectangle(frame, (425,100),(625,300), (0,255,0), thickness=2, lineType=8, shift=0)
    
        lower_blue = np.array([l_h, l_s, l_v])
        upper_blue = np.array([u_h, u_s, u_v])
        imcrop = img[102:298, 427:623]
        hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        cv2.putText(frame, img_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
        paint_win = np.zeros((400, 500, 3), np.uint8) 
        paint_win.fill(255)
        if img_text=='A':
            cv2.rectangle(frame,(30,30),(400,400),(255,0,0),2)
            cv2.rectangle(paint_win,(30,30),(400,400),(255,0,0),2)
        if img_text=='B':
            cv2.circle(img,(300,300),100,(0,250,200))
            cv2.circle(paint_win,(300,300),100,(0,250,200))
        if img_text=='C':
            cv2.line(img,(100,100),(400,400),(0,0,2550))
            cv2.line(paint_win,(100,100),(400,400),(0,0,2550))
        if img_text=='D':
            cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
            cv2.ellipse(paint_win,(256,256),(100,50),0,0,180,255,-1)
        if img_text=='E':
            p1 = (100, 200) 
            p2 = (50, 50) 
            p3 = (300, 100) 
              
            # Drawing the triangle with the help of lines 
            #  on the black window With given points  
            # cv2.line is the inbuilt function in opencv library 
            cv2.line(img, p1, p2, (255, 0, 0), 3) 
            cv2.line(paint_win, p1, p2, (255, 0, 0), 3) 
            cv2.line(img, p2, p3, (255, 0, 0), 3) 
            cv2.line(paint_win, p2, p3, (255, 0, 0), 3) 
            cv2.line(img, p1, p3, (255, 0, 0), 3)
            cv2.line(paint_win, p1, p3, (255, 0, 0), 3)

        cv2.imshow("Sign Capture Window", frame)
        cv2.imshow("Silhouettes Image", mask)
        cv2.imshow("image", paint_win) 
        #cv2.waitKey(0)
        #if cv2.waitKey(1) == ord('c'):
            
        img_name = basepath + "/1.png"
        save_img = cv2.resize(mask, (64, 64))
        cv2.imwrite(img_name, save_img)
        
    #    print("{} written!".format(img_name))
        img_text = predictor()
#        speak.Speak(img_text)
        
        if cv2.waitKey(1) == ord('c'):
            img_text = predictor()
            
            
        if cv2.waitKey(1) == 27:
            cam.release()
            cv2.destroyAllWindows()
            break









def colour():
    import numpy as np
    import cv2
    from collections import deque

    # Define the upper and lower boundaries for a color to be considered "Blue"
    blueLower = np.array([100, 60, 60])
    blueUpper = np.array([140, 255, 255])
    #skin =np.array([231,158,109])

    # Define a 5x5 kernel for erosion and dilation
    kernel = np.ones((5, 5), np.uint8)

    # Setup deques to store separate colors in separate arrays
    bpoints = [deque(maxlen=512)]
    gpoints = [deque(maxlen=512)]
    rpoints = [deque(maxlen=512)]
    ypoints = [deque(maxlen=512)]
    opoints = [deque(maxlen=512)]
    vpoints = [deque(maxlen=512)]
    ipoints = [deque(maxlen=512)]
    bindex = 0
    gindex = 0
    rindex = 0
    yindex = 0
    oindex = 0
    vindex = 0
    iindex = 0

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255),(255, 165 , 0),(238 , 130, 238),(75,0 ,130)]

    colorIndex = 0

    # Setup the Paint interface
    paintWindow = np.zeros((471, 636, 3)) + 255
    paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
    paintWindow = cv2.rectangle(paintWindow, (160, 1), (255, 65), colors[0], -1)
    paintWindow = cv2.rectangle(paintWindow, (275, 1), (370, 65), colors[1], -1)
    paintWindow = cv2.rectangle(paintWindow, (390, 1), (485, 65), colors[2], -1)
    paintWindow = cv2.rectangle(paintWindow, (505, 1), (600, 65), colors[3], -1)
    paintWindow = cv2.rectangle(paintWindow, (620, 1), (715, 65), colors[4], -1)
    paintWindow = cv2.rectangle(paintWindow, (735, 1), (830, 65), colors[5], -1)
    paintWindow = cv2.rectangle(paintWindow, (850, 1), (945, 65), colors[6], -1)
    cv2.putText(paintWindow, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "ORANGE", (640,33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 165 , 0),2,cv2.LINE_AA)
    cv2.putText(paintWindow, "VIOOLET", (762, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 165, 0), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "INDIGO", (882, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 165, 0), 2, cv2.LINE_AA)
    cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

    # Load the video
    camera = cv2.VideoCapture(0)

    # Keep looping
    while True:
        # Grab the current paintWindow
        (grabbed, frame) = camera.read()
        frame = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Add the coloring options to the frame
        frame = cv2.rectangle(frame, (40, 1), (140, 65), (122, 122, 122), -1)
        frame = cv2.rectangle(frame, (160, 1), (255, 65), colors[0], -1)
        frame = cv2.rectangle(frame, (275, 1), (370, 65), colors[1], -1)
        frame = cv2.rectangle(frame, (390, 1), (485, 65), colors[2], -1)
        frame = cv2.rectangle(frame, (505, 1), (600, 65), colors[3], -1)
        frame = cv2.rectangle(frame, (620, 1), (715, 65), colors[4], -1)
        frame = cv2.rectangle(frame, (735, 1), (830, 65), colors[5], -1)
        frame = cv2.rectangle(frame, (850, 1), (945, 65), colors[6], -1)
        cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 2, cv2.LINE_AA)
        cv2.putText(frame, "ORANGE", (640, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 153, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "VIOLET", (762, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 153, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "INDIGO", (882, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 153, 255), 2, cv2.LINE_AA)
        # Check to see if we have reached the end of the video
        if not grabbed:
            break

        # Determine which pixels fall within the blue boundaries and then blur the binary image
        blueMask = cv2.inRange(hsv, blueLower, blueUpper)
        blueMask = cv2.erode(blueMask, kernel, iterations=2)
        blueMask = cv2.morphologyEx(blueMask, cv2.MORPH_OPEN, kernel)
        blueMask = cv2.dilate(blueMask, kernel, iterations=1)

        # Find contours in the image
        (ret, cnts, _) = cv2.findContours(blueMask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        center = None

        # Check to see if any contours were found
        if len(cnts) > 0:
            # Sort the contours and find the largest one -- we
            # will assume this contour correspondes to the area of the bottle cap
            cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
            # Get the radius of the enclosing circle around the found contour
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)
            # Draw the circle around the contour
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            # Get the moments to calculate the center of the contour (in this case Circle)
            M = cv2.moments(cnt)
            center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

            if center[1] <= 65:
                if 40 <= center[0] <= 140:  # Clear All
                    bpoints = [deque(maxlen=512)]
                    gpoints = [deque(maxlen=512)]
                    rpoints = [deque(maxlen=512)]
                    ypoints = [deque(maxlen=512)]
                    opoints = [deque(maxlen=512)]
                    vpoints = [deque(maxlen=512)]
                    ipoints = [deque(maxlen=512)]
                    bindex = 0
                    gindex = 0
                    rindex = 0
                    yindex = 0
                    oindex = 0
                    vindex = 0
                    iindex = 0


                    paintWindow[67:, :, :] = 255
                elif 160 <= center[0] <= 255:
                    colorIndex = 0  # Blue
                elif 275 <= center[0] <= 370:
                    colorIndex = 1  # Green
                elif 390 <= center[0] <= 485:
                    colorIndex = 2  # Red
                elif 505 <= center[0] <= 600:
                    colorIndex = 3  # Yellow
                elif 620 <= center[0] <= 715:
                    colorIndex = 3  # Orange
                elif 735 <= center[0] <= 830:
                    colorIndex = 3  # Violet
                elif 850 <= center[0] <= 945:
                    colorIndex = 3  # Indigo
            else:
                if colorIndex == 0:
                    bpoints[bindex].appendleft(center)
                elif colorIndex == 1:
                    gpoints[gindex].appendleft(center)
                elif colorIndex == 2:
                    rpoints[rindex].appendleft(center)
                elif colorIndex == 3:
                    ypoints[yindex].appendleft(center)
                elif colorIndex ==4:
                    opoints[oindex].apppendleft(center)
                elif colorIndex ==5:
                    vpoints[vindex].apppendleft(center)
                elif colorIndex == 6:
                    ipoints[iindex].apppendleft(center)
        # Append the next deque when no contours are detected (i.e., bottle cap reversed)
        else:
            bpoints.append(deque(maxlen=512))
            bindex += 1
            gpoints.append(deque(maxlen=512))
            gindex += 1
            rpoints.append(deque(maxlen=512))
            rindex += 1
            ypoints.append(deque(maxlen=512))
            yindex += 1
            opoints.append(deque(maxlen=512))
            oindex += 1
            vpoints.append(deque(maxlen=512))
            vindex += 1
            ipoints.append(deque(maxlen=512))
            iindex += 1

        # Draw lines of all the colors (Blue, Green, Red and Yellow)
        points = [bpoints, gpoints, rpoints, ypoints,opoints,vpoints,ipoints]
        for i in range(len(points)):
            for j in range(len(points[i])):
                for k in range(1, len(points[i][j])):
                    if points[i][j][k - 1] is None or points[i][j][k] is None:
                        continue
                    cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                    cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

        # Show the frame and the paintWindow image
        cv2.imshow("Tracking", frame)
        cv2.imshow("Paint", paintWindow)

        # If the 'q' key is pressed, stop the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            camera.release()
            break

    # Cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()





def Write():
    from subprocess import call
    call(["python", "Write.py"])


def new_rec():
    # Python3 program to draw rectangle
    # shape on solid image
    import numpy as np
    import cv2

    # Creating a black image with 3
    # channels RGB and unsigned int datatype
    img = np.zeros((400, 400, 3), dtype="uint8")

    # Creating rectangle
    cv2.rectangle(img, (60, 30), (300, 200), (255, 255, 255), 5)

    cv2.imshow('dark', img)

    # Allows us to see image
    # untill closed forcefully
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Shape = tk.Label(window, text="--SHAPES--", fg="black", bg="cyan", width=20, height=2,
                     font=("Tempus Sans ITC",15,"bold"))
Shape.place(x=130, y=200)






shape = tk.Button(window, text="Shape", command=sign_recognize, fg="black", bg="green yellow", width=20, height=2,
                     font=("Tempus Sans ITC",15,"bold"))
shape.place(x=1000, y=600)

Ops = tk.Label(window, text="--OPERATIONS--", fg="black", bg="green yellow", width=20, height=2,
                     font=("Tempus Sans ITC",17,"bold"))
Ops.place(x=965, y=200)

colour = tk.Button(window, text="Colour", command=colour, fg="black", bg="green yellow", width=20, height=2,
                     font=("Tempus Sans ITC",15,"bold"))
colour.place(x=1000, y=300)


Write = tk.Button(window, text="Write", command=Write, fg="black", bg="green yellow", width=20, height=2,
                     font=("Tempus Sans ITC",15,"bold"))
Write.place(x=1000, y=500)



window.mainloop()