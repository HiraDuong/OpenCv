import cv2 as cv
from pyzbar import pyzbar as qr

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cant use the camera!")
        break

    qrcodes = qr.decode(frame)
    for qrcode in qrcodes:
        x, y, w, h = qrcode.rect
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

        data = qrcode.data.decode("utf-8")
        codetype = qrcode.type
        text = '{} - {}'.format(data, codetype)
        cv.putText(frame, text, (x - 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv.imshow("Read QR code", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
