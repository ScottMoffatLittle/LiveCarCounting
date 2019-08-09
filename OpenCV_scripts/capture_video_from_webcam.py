# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('video capture', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture("rtmp://s12.us-east-1.skyvdn.com:1935/rtplive/SalemI81MM140")

while True:
    ret, frame = cap.read()
    cv2.imshow('video capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()