#  write a function which can read video file and play for you .
def videoshow(path):
    import cv2
    cap = cv2.VideoCapture(path)
    if (cap.isOpened() == False):
        print("Error opening video file")

    # Read until video is completed
    while (cap.isOpened()):

        ret, frame = cap.read()
        if ret == True:

            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    videoshow(input("Enter the path of file\n"))