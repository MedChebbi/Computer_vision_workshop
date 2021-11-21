import cv2


vid_path ='../resources/videos/video_1.mp4'
save_path = '../resources/videos/video_test.mp4'
save_vid = True #A variable to tell when we want to save video

#Initialize where to get video from: cv2.VideoCapture()
####[CODE HERE]####

if save_vid:
    #Extracting useful info from the video
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #w,  h = 1280, 720
    #Initializing the video recorder
    vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

while(vid_cap.isOpened()):
    # Capture frame-by-frame using the .read() method on the video capture instance
    ####[CODE HERE]####
    
    #frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_AREA)
    if ret:
        #Showing video, frame per frames
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if save_vid:
        #Saving video frames
        vid_writer.write(frame)

if save_vid: vid_writer.release()
# When everything done, release the video capture object
vid_cap.release()
# Closes all the frames
cv2.destroyAllWindows()
    