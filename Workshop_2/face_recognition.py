import cv2
import numpy as np
import face_recognition
import os

def main():
    KNOWN_FACES_DIR = 'resources/known_faces'
    TOLERANCE = 0.6
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 3
    MODEL = 'cnn' # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model

    print('Loading known faces...')
    known_faces = []
    known_names = []

    # We oranize known faces as subfolders of KNOWN_FACES_DIR
    # Each subfolder's name becomes our label (name)
    for name in os.listdir(KNOWN_FACES_DIR):

        # Next we load every file of faces of known person
        for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):

            # Load an image
            image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')
            r,c,ch = image.shape
            print ('row',r)
            print ('col',c)
            print ('channel',ch)
            # Get 128-dimension face encoding
            # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
            encoding = face_recognition.face_encodings(image)[0]
            # Append encodings and name
            known_faces.append(encoding)
            known_names.append(name)

    image = cv2.imread('resources/Trump.jpg')
    locations = face_recognition.face_locations(image, model=MODEL)
    # Now since we know loctions, we can pass them to face_encodings as second argument
    # Without that it will search for faces once again slowing down whole process
    encodings = face_recognition.face_encodings(image, locations)

    for face_encoding, face_location in zip(encodings, locations):
 
        # We use compare_faces (but might use face_distance as well)
        # Returns array of True/False values in order of passed known_faces
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        
        # Since order is being preserved, we check if any face was found then grab index
        # then label (name) of first matching known face withing a tolerance
        match = None
        if True in results:  # If at least one is true, get a name of first of found labels
            match = known_names[results.index(True)]
            #print(f' - {match} from {results}')
            # Each location contains positions in order: top, right, bottom, left
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            # Paint frame
            cv2.rectangle(image, top_left, bottom_right, (255,255,255), FRAME_THICKNESS)
    
            #cv2.rectangle(image, top_left, bottom_right, (255,0,0), cv2.FILLED)
            # Wite a name
            print(match)
            cv2.putText(image, match, (face_location[3]+15, face_location[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), FONT_THICKNESS)


if __name__ == '__main__':
    main()