##CSCI442, Program 2 by Nayte Chandler and Logan Shy, 2/13/2019
##Runs Part one, press 'q' to exit, then Part 2 runs and when you press 'q' again the program is done


import cv2 as cv
import numpy as np



#hsvValues = np.zeros(3); 
scalarMin = np.zeros(3); #holds 3 min values
scalarMax = np.zeros(3); #holds 3 max values
#xValue = 0;

def hueMax(value): #all these functions set the min max array alues to the slider values
    scalarMax[0] = value;
def hueMin(value):
    scalarMin[0] = value;
def satMax(value):
    scalarMax[1] = value;
def satMin(value):
    scalarMin[1] = value;
def valueMax(value):
    scalarMax[2] = value;
def valueMin(value):
    scalarMin[2] = value;
    #print(scalarMax);
    #print(scalarMin);
    
p = 'true'; #while true loop
capture = cv.VideoCapture(0); 
cv.namedWindow("frame1"); #make frame before loop so i can add sliders
cv.createTrackbar("hueMax", "frame1", 179, 179, hueMax); #making 6 track bars (the first can only goto 179) 
cv.createTrackbar("hueMin", "frame1", 0, 179, hueMin);
cv.createTrackbar("SatMax", "frame1", 255, 255, satMax);
cv.createTrackbar("SatMin", "frame1", 0, 255, satMin);
cv.createTrackbar("ValueMax", "frame1", 255, 255, valueMax);
cv.createTrackbar("ValueMin", "frame1", 0, 255, valueMin);


def getLoc(event, x, y, flags, parameter): #prints location of click and hsv values af the clicked pixel
    if event == cv.EVENT_LBUTTONDBLCLK:
        print("Location X: ", x, "Y: ", y);
        print(imgHSV[y, x]);
    if event == cv.EVENT_LBUTTONUP: #for some reason you have to program it so it works for clicked and unclicked
        print("Location X: ", x, "Y: ", y);
        print(imgHSV[y, x]);

while(p == 'true'):
    imgHSV, original = capture.read(); #captures webcam
    maskedFrame = capture.read(); #captures webcam
    imgHSV = cv.cvtColor(original, cv.COLOR_BGR2HSV); #converts to hsv
    cv.imshow('frame1',imgHSV); #displays frames
    cv.imshow('frame2', original);
    maskedFrame = cv.inRange(imgHSV, scalarMin, scalarMax); #applies mask to hsv image
    maskedFrame = cv.dilate(maskedFrame, np.ones((3, 3))); #dilates hsv image
    maskedFrame = cv.erode(maskedFrame, np.ones((5, 5))); #erodes hsv image

    
    cv.imshow('frame3', maskedFrame);
    cv.setMouseCallback('frame1', getLoc);
    if cv.waitKey(1) & 0xFF == ord('q'): #if q is pressed exit
        p = 'false';
        break;
    
capture.release();
cv.destroyAllWindows();


cap = cv.VideoCapture(0);
#cv2.namedWindow("Video");
#cv2.namedWindow("Test");

compare = None; 
thresh = None;

while True:
    status, img = cap.read();
    cv.imshow("Video", img);

    grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY); #change to grayscale
    blurimg = cv.GaussianBlur(grayimg, (21,21), 0); #gaussian blur with 21x21 matrix
    thresh = blurimg;
    if compare is None: #for first iteration
        compare = blurimg; 
    difference = cv.absdiff(compare, blurimg); #compute absdif
    thres, thresh = cv.threshold(difference, 25, 255, cv.THRESH_BINARY); #take threshold
    cv.imshow('frame2: Difference', difference); 
    difference = blurimg;
    mask = np.ones((5,5), np.uint8); # mask for dilating and eroding
    thresh = cv.dilate(thresh, mask, iterations = 2); #dilates the whites
    thresh = cv.erode(thresh, mask, iterations = 2); #erodes the whites

    cv.imshow('frame3: Threshold', thresh);
    if cv.waitKey(1) & 0xFF == ord('q'): #if q is pressed exit (my computer wasnt running this part super well so i pass wait key 100 to slow down the capture rate
        p = 'false';
        break;
    compare = blurimg;
    
cap.release();
cv.destroyAllWindows();































    
