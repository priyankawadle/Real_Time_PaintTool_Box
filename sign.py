from keras.models import load_model
import cv2
import numpy as np
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
image_x, image_y = 64, 64
def sign_recognize():
    #clear_lbl()

    #    update_label("Press << c >> for Gesture Detection with Voice")

    classifier = load_model(r'E:\OMKARS\OMKARS1\100%Main_Sign_Recognition\Main_Sign_Recognition\SignR_model.h5')

    def predictor():
        import numpy as np
        from keras.preprocessing import image
        test_image = image.load_img( 'E:/OMKARS/OMKARS1/100%Main_Sign_Recognition/Main_Sign_Recognition/1.png', target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = classifier.predict(test_image)

        if result[0][0] == 1:
            #print("All The Best")
            return 'All the best!!'
        elif result[0][1] == 1:
            #print('Very Good!!')
            return 'Very Good!!'
        elif result[0][2] == 1:
            #print('P!!')
            return 'P!!'

        elif result[0][3] == 1:
            return 'A!!'
        elif result[0][4] == 1:
            return 'Z!!'


    cam = cv2.VideoCapture(0)
    img_text = ''
    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        #update_label("Press << c >> for Gesture Detection with Voice")

        l_h = 0
        l_s = 0
        l_v = 0
        u_h = 179
        u_s = 255
        u_v = 152

        img = cv2.rectangle(frame, (425, 100), (625, 300), (0, 255, 0), thickness=2, lineType=8, shift=0)

        lower_blue = np.array([l_h, l_s, l_v])
        upper_blue = np.array([u_h, u_s, u_v])
        imcrop = img[102:298, 427:623]
        hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        cv2.putText(frame, img_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
        cv2.imshow("Sign Capture Window", frame)
        cv2.imshow("Silhouettes Image", mask)

        # if cv2.waitKey(1) == ord('c'):

        img_name = "1.png"
        save_img = cv2.resize(mask, (image_x, image_y))
        cv2.imwrite(img_name, save_img)
        #    print("{} written!".format(img_name))
        img_text = predictor()
        #        speak.Speak(img_text)

        if cv2.waitKey(1) == ord('c'):
            img_text = predictor()
            speak.Speak(img_text)

        if cv2.waitKey(1) == 27:
            cam.release()
            cv2.destroyAllWindows()
            break


sign_recognize()