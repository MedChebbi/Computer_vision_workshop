import cv2


vid_path = '../resources/videos/video_1.mp4'
save_path = '../resources/videos/video_test.mp4'
save_vid = False #A variable to tell when we want to save video

#Create video capture instance
vid_cap = cv2.VideoCapture(vid_path)

#Get needed video info if we are going to record video
if save_vid:
    #Extracting useful info from the video
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #w,  h = 1280, 720

    #Create video writer instance
    vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

while(vid_cap.isOpened()):
    # Capture frame-by-frame using the .read() method on the video capture instance
    ####[CODE HERE]####
    ret, frame = vid_cap.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(gray_img.shape)
    #frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_AREA)
    frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_AREA)
    # Display video 
    if ret:
        #Showing video, frame per frames
        cv2.imshow("frame",frame)
        cv2.imshow("Gray",gray_img)

        # Close window when you press q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Record if save_vid == True
    if save_vid:
        #Saving video frames
        vid_writer.write(frame)

if save_vid: vid_writer.release()
# When everything done, release the video capture object
vid_cap.release()
# Closes all the frames
cv2.destroyAllWindows()