import cv2

if __name__ == '__main__':
    vid_path ='/home/mohamed/data/test_conf_5.mp4'
    save_path = '/home/mohamed/data/demo_test_conf_5.mp4'
    save_vid = True
    vid_cap = cv2.VideoCapture(vid_path)
    if save_vid:
        fps = vid_cap.get(cv2.CAP_PROP_FPS)
        w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #w,  h = 1280, 720
        vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

    while(vid_cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = vid_cap.read()
        frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_AREA)
        if ret:
            
            cv2.imshow("frame",frame)
          
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if save_vid:
            vid_writer.write(frame)

    if save_vid: vid_writer.release()
    # When everything done, release the video capture object
    vid_cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()
    