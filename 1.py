yt = YouTube(url)
        yt.streams.first().download(os.getcwd())

        cap = cv2.VideoCapture(yt.title)

        try:
            if not os.path.exists('./youtube/frame'):
                os.makedirs('./youtube/frame')
        except OSError:
            print ('Error: Creating directory of frame')

        vidcap = cv2.VideoCapture(yt.title + ".mp4")
        currentFrame = 0
        currentSavedFrame = 0
        while(True):
            success,image = vidcap.read()
            if not success:
                break
            ret, frame = cap.read()

            if(currentFrame % (second*30) == 0):
                name = './youtube/frame/frame' + str(currentSavedFrame) + '.jpg'
                currentSavedFrame += 1
                print ('Creating...' + name)
                cv2.imwrite(name, frame)

            currentFrame += 1
        cap.release()
        os.remove(os.getcwd() + "\\" + yt.title + ".mp4")