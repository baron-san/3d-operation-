# statsの構造の例
# 各行は [左上のx座標, 左上のy座標, 幅, 高さ, 面積]
import cv2
import numpy as np
import win32api
import win32con
import time 
import keyboard
import serial
from debag import debag

cap = cv2.VideoCapture(0)
def click_mouse():
     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
     #time.sleep(float(1.0))

# def move_mosue():
#     win32api.mouse_event(0x01,int(100),int(0))

def make_mask(img):
    RED_MIN = np.array([0, 170, 170])
    RED_MAX = np.array([10, 255, 255])
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, RED_MIN, RED_MAX)
    return mask

def info(img):
    mask= make_mask(img)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)
    binary_img = cv2.bitwise_and(img, img, mask=mask)
    hight,width= img.shape[0],img.shape[1]

    return num_labels, labels, stats, centroids, binary_img,hight,width

# def rotate_img_180(binary_img):
#     binary_img_180 = cv2.rotate(binary_img,cv2.ROTATE_180)
#     return binary_img_180

def judge(center_X,cetner_Y,width,hight,define_value):
        if center_X > int((width/2)+define_value) and int((hight/2)-define_value) < cetner_Y < int((hight/2)+define_value):
            win32api.mouse_event(0x01,int(70),int(0))
            time.sleep(float(0.02))
        
        if center_X < int((width/2)+define_value) and int((hight/2)-define_value) < cetner_Y < int((hight/2)+define_value):
             win32api.mouse_event(0x01,int(-70),int(0))
             time.sleep(float(0.02))

        if int((width/2)-define_value) < center_X < int((width/2)+define_value) and cetner_Y < int((width/2)-define_value):
             win32api.mouse_event(0x01,int(0),int(-70))
             time.sleep(float(0.02))
             
        if int((width/2)-define_value) < center_X < int((width/2)+define_value) and cetner_Y > int((width/2)+define_value):
             win32api.mouse_event(0x01,int(0),int(70))
             time.sleep(float(0.02))
        
        if center_X >=int(width/2-define_value) and center_X <=int(width/2+define_value):
            if cetner_Y >=int(hight/2-define_value) and cetner_Y <=int(width/2+define_value):
                pass

    #変更
    #print(f'center_X:{center_X},center_Y{cetner_Y}')
    # if center_X <=int((width//2)-define_value):
    #     if cetner_Y <=int((hight/2)-define_value): 
            # print("moving LEFT")
            # keyboard.release("w")
            # keyboard.release("s")
            # keyboard.release("d")
            # keyboard.press("a")
    
    # if cetner_Y >=int((hight/2)+define_value) and center_X<=int((hight//2)-define_value): 
    #     win32api.mouse_event(0x01,int(0),int(-70))
    #     print("1")
    #     time.sleep(float(0.02))

            # print("moving stright")
            # keyboard.release("a")
            # keyboard.release("s")
            # keyboard.release("d")
            # keyboard.press("w")
            
    # if center_X >=int((width//2)+define_value):
    #     if cetner_Y <=int((hight/2)-define_value): 
    #         win32api.mouse_event(0x01,int(70),int(0))
    #         time.sleep(float(0.02))
            # print("moving RIGHT")
            # keyboard.release("w")
            # keyboard.release("a")
            # keyboard.release("s")
            # keyboard.press("d")

    # if cetner_Y >=int((hight/2)+define_value) and center_X >=int((hight//2)+define_value): 
    #     win32api.mouse_event(0x01,int(0),int(70))
    #     print("2")
        # time.sleep(float(0.02))
        # print("moving down")
        # keyboard.release("w")
        # keyboard.release("a")
        # keyboard.release("d")
        # keyboard.press("s")

            
    # if center_X >=int(width/2-define_value) and center_X <=int(width/2+define_value):
    #     if cetner_Y <=int((hight/2)-define_value-30): 
    #         click_mouse()    
        
def main(define_value):
    while True:
        ret, img = cap.read()
        img = cv2.flip(img,1)
        num_labels, labels, stats, centroids, binary_img,hight,width = info(img)   
        if stats.shape[0] > 1:
            max_index = np.argmax(stats[1:,4])+1
            center_X,center_Y = centroids[max_index]   
            X1,Y1,X2,Y2,area_size = stats[max_index]
            cv2.circle(binary_img, (int(center_X), int(center_Y)), 10, (0, 255, 0), -1) 
            cv2.circle(binary_img,(int(width/2),int(hight/2)),4,(255,255,0),-1)
            cv2.rectangle(binary_img,(X1,Y1),(X2+X1,Y2+Y1),(255,0,0),thickness=3,lineType=cv2.LINE_4)
            judge(center_X,center_Y,width,hight,define_value)
            debag(X1,Y1,X2,Y2,area_size)    
        cv2.rectangle(binary_img,(int(width/2-define_value),int(hight/2-define_value)),(int(width/2+define_value),int(hight/2+define_value)),(0,255,0),thickness=3,lineType=cv2.LINE_4)
        
        #marge_img = np.hstack((binary_img,gray_img)) # 二つの画像をつなげる
        cv2.imshow("Test", binary_img)
        key = cv2.waitKey(1)
        if key == 27: 
            break

   
    cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
