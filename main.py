import cv2


cap = cv2.VideoCapture('video.MP4')
fps = int(cap.get(cv2.CAP_PROP_FPS))
save_interval = 10

frame_count = 0
i=0

if cap.isOpened():
    ret, frame = cap.read()
    if ret:
        im2 = frame


while cap.isOpened():
    ret, frame = cap.read()


    if ret:
        frame_count += 1
        if frame_count % (fps * save_interval) == 0:
            im1 = im2
            im2 = frame
            im3 = cv2.subtract(im1, im2)

            cv2.imwrite('im' + str(i) + '.jpg', im3)
            i += 1
            print(str(i)+'th image')
            # optional
            frame_count = 0

    # Break the loop
    else:
        break

cap.release()
