import cv2 as cv
import numpy as np

if (__name__ == '__main__'):
    src = cv.imread('banner.jpeg')
    dsize = np.array([len(src[0]), len(src)])
    point = 0
    pts1 = np.float32([[0, 0], [dsize[0], 0],
        [0, dsize[1]], [dsize[0], dsize[1]]])
    pts2 = np.float32([[0, 0], [dsize[0], 0],
        [0, dsize[1]], [dsize[0], dsize[1]]])
    while(True):

        matrix = cv.getPerspectiveTransform(pts1, pts2)
        result = cv.warpPerspective(src, matrix, (2500,1600))
        cv.imshow('banner', src)
        cv.imshow('result', result)
        val = cv.waitKey(24)
        if(val == ord(' ')):
            break
        elif(val >= ord('1') and val <= ord('4')):
            point = val - ord('1')
        elif(val == ord('w')):
            pts2[point][1] -= 1
        elif(val == ord('s')):
            pts2[point][1] += 1
        elif(val == ord('d')):
            pts2[point][0] += 1
        elif(val == ord('a')):
            pts2[point][0] -= 1
        elif(val >= ord('1') and val <= ord('4')):
            point = val - ord('1')
        elif(val == ord('i')):
            pts2[point][1] -= 10
        elif(val == ord('k')):
            pts2[point][1] += 10
        elif(val == ord('l')):
            pts2[point][0] += 10
        elif(val == ord('j')):
            pts2[point][0] -= 10  
    cv.destroyAllWindows()