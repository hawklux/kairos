# 노이즈 필터링(salt & pepper에는 medianBlur가 좋다)
import cv2
import numpy as np

# 카메라 객체생성: 소스 + 해상도 설정
capt = cv2.VideoCapture(0)
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 648)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 동영상 = 무한루프
while True:
    # frame: 카메라 캡쳐 영상 저장
    # ret: 잘 받았으면 True, 아니면 False
    ret, frame = capt.read()

    if not ret:
        print("Fail to capture image.")
        break

    # frame에 적용할 salt & papper 노이즈 생성
    noise = np.uint8(np.random.normal(loc=0, scale=0.4, size=frame.shape)) #size=[480, 640, 3])) 높,폭,색도 됨.
    noised_img = cv2.add(frame, noise) # 노이즈 적용

    # Blur 필터 적용 영상
    blur = cv2.blur(noised_img, (5,5))

    # 가우시안 Blur: 그냥 blur보다는 외곽선 살아남
    gaussian = cv2.GaussianBlur(noised_img,(5,5),0)

    # bilateral 필터: 가우시안보다 외곽선 더 살림
    bilateral = cv2.bilateralFilter(noised_img,9,75,75)

    # Median blur: salt & pepper 노이즈 제거 탁월, 외곽선 굿.
    median = cv2.medianBlur(noised_img,5)

    # 원본 영상(비교용)
    cv2.imshow("Original", frame)

    # 노이즈 적용 영상
    cv2.imshow("Noised", noised_img)

    # blur 필터 적용 영상
    # cv2.imshow("Blurred", blur)

    # gaussian blur 필터 적용 영상
    # cv2.imshow("Gaussian blurred", gaussian)

    # bilateral 필터 적용 영상
    # cv2.imshow("Bilaterally", bilateral)

    # Median blur 필터 적용 영상
    # cv2.imshow("Median Blurred", median)

    # 여러 영상을 하나로 합침
    row1 = cv2.hconcat([frame, noised_img, blur])
    row2 = cv2.hconcat([gaussian, bilateral, median])

    total = cv2.vconcat([row1, row2])
    cv2.imshow("All in one", total)

    if cv2.waitKey(1) == ord('q'):
        break
capt.release()
cv2.destroyAllWindows()