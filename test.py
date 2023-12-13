import cv2 #cv2 불러오기

src = cv2.imread('wonyoung.JPG', cv2.IMREAD_COLOR) #imread 이미지 읽기, cv.2IMREAD_~~는 이미지 파일을 Color로 읽어들입니다. 투명한 부분은 무시되며, Default값입니다.

cv2.imshow('src', src) #imshow 함수는 이미지를 사이즈에 맞게 보여줍니다.

for sigma in range(1, 10): #시그마 1부터 3까지 반복문
    dst = cv2.GaussianBlur(src, (0, 0), sigma) #ksize: 가우시안 커널 크기. (0, 0)을 지정하면 sigma 값에 의해 자동 결정됨
    
    desc = 'sigma = {}'.format(sigma) # 시그마 숫자대로 문자열 처리
    cv2.putText(dst, desc,(150,300), cv2.FONT_HERSHEY_COMPLEX, 5.0, (0,0,0),cv2.LINE_AA)
    #cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    
    cv2.imshow('dst', dst)
    cv2.waitKey()
    
cv2.destroyAllWindows