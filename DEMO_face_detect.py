# This function is used to record a video, apply face detection onto it, extract the usefull bit and save it
def file_face_rec_and_cropping(SAVE_WHOLE = False, SAVE_CROPPED = False, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', DISPLAY_WHOLE = True, DISPLAY_CHROPPED = True, OUTPUT_FILE_NAME = 'camera_recording', ADD_STR_CROPPED_FILE_NAME = '_cropped', OUTPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 105, CROPPED_HEIGHT = 105, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 10, NUMBER_OF_CAMERA_OR_VIDEO_DIR = 0, ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, FUTURE_KILL_SWITCH = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = False, ENABLE_CUBIC_LAND_MARK_TRACKING = True, CUBIC_LAND_MARK_POINT_TOP = 34,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT = 1,  SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START = 48, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP = 68):
    import cv2
    import numpy as np
    import dlib
    import time
    import pandas as pd
    
    '''
    # if the program crashes and doesn't work again you need to restart the kernel
    # Note to stop the recording simply click onto the diplayed image and press the 'q' button or from the terminal pres CTRL+C
    # fourcc codecs list https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html 
    #In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
    #In Windows: DIVX (More to be tested and added)
    #In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).

    # This function is used to record a video, apply face detection onto it, extract the usefull bit and save it 

    SAVE_WHOLE # saves whole recording
    SAVE_CROPPED # saves cropped recording    
    DISPLAY_WHOLE # displays whole captured input
    DISPLAY_CHROPPED # displayes cropped captured input
    OUTPUT_FILE_NAME # file name
    OUTPUT_FILE_NAME_EXTENSION # extensions
    CROPPED_WIDTH # integer value greater than 0 
    CROPPED_HEIGHT #  integer value greater than 0
    SHIFT_RIGHT = -50 # inger value, shifts cropeed region
    SHIFT_DOWN = 0 # inger value, shifts cropeed region
    OUTPUT_FPS = 15 # save fps 
    NUMBER_OF_CAMERA_OR_VIDEO_DIR = 0 # camera index number, 0 unless more than one camera connected
    
    ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True # This function is used to enable automatic face tracking of wither based on landmarks or face recogntition. If this is set to False a fixed croped region is placed in the middle of the screen

    WHOLE_FACE_PROFILE = False # predefined face profiles which tracks the whole face. Based on face recognition coordinates and not on land mark position tracking
    LIPS_PROFILE = False # predefined face profiles which tracks the whole face. Based on face recognition coordinates and not on land mark position tracking
    
    FUTURE_KILL_SWITCH = False    # potential future stop switch

    
    # tracking from landmark positions insted. 
    LOAD_FACE_LANDMARKS = True # load land marks, needed for any landmark use
    POINT_LAND_MARK_TRACKING = False # Insted of tracking with face recognition coordinates track using land mark positions of the 68 points shown in figure facial_landmarks_68markup.
    LAND_MARK_TRACKING_NUMBER = 1 # Specifies the tracking point, see image facial_landmarks_68markup-768x619 for details about the numbers
    LAND_MARK_LIP_TRACKING = True # alias to tracking point 38
    DISPLAY_FACE_LANDMARKS = False #show land marks
    CAPTURE_FACE_LANDMARKS = True # captur 68 landmark positions 
    
    # PROFILES Note: if LAND_MARK_LIP_TRACKING is enabled this profiles are ingnored. Also if these profiles are enabled the previously set CROPPED_WIDTH = 210 CROPPED_HEIGHT = 210 SHIFT_RIGHT = 0 SHIFT_DOWN = 100 are overwritten.





    # NOTES

    ###    
    if WHOLE_FACE_PROFILE = True then LIPS_PROFILE, POINT_LAND_MARK_TRACKING, LAND_MARK_LIP_TRACKING must be False and ofcourse ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True 
    

    '''
    
    
    
    import cv2
    import numpy as np
    import dlib
    import time

   
    

    
    # only applicable for auto-tracking and cropping but point land marking must be disabled
    if WHOLE_FACE_PROFILE == True:
        # properties wich will enable a full face profile
        CROPPED_WIDTH = 210
        CROPPED_HEIGHT = 300
        SHIFT_RIGHT = -15
        SHIFT_DOWN = -100
    elif WHOLE_FACE_PROFILE == False:
        pass
    else:
        pass
    
    if LIPS_PROFILE == True:
        # properties wich will enable a full face profile
        CROPPED_WIDTH = 105
        CROPPED_HEIGHT = 105
        SHIFT_RIGHT = 55
        SHIFT_DOWN = 120
    elif LIPS_PROFILE == False:
        pass
    else:
        pass
    
    if ( WHOLE_FACE_PROFILE == True and POINT_LAND_MARK_TRACKING == True):
        # properties wich will enable a full face profile
        CROPPED_WIDTH = 230
        CROPPED_HEIGHT = 360
        SHIFT_RIGHT = -15
        SHIFT_DOWN = -170
    elif WHOLE_FACE_PROFILE == False:
        pass
    else:
        pass
    
    detector = dlib.get_frontal_face_detector()
    
    # a pre set variable that it is required by the programm, do not change
    #FACE_DETECTED = False
    LIST_FACE_DETECTION_RESULT_PER_FRAME = []
    global LIST_SINGLE_FRAME_LANDMARK_RESULT
    global LIST_LANDMARK_RESULT_PER_INPUT
    LIST_LANDMARK_RESULT_PER_INPUT = []

    FRAME_INDEX = 0
    LIST_FRAME_INDEX = []
    
    if LOAD_FACE_LANDMARKS == True:
        try:
            # load land mark preditor
            predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat') # the follwoing file was downloaded from here https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat
            # x and y will be the lists which will contain the coordinates of the land mark points             
            #print('shape_predictor_68_face_landmarks.dat loaded')
        except:
            print('could unable to load shape_predictor_68_face_landmarks.dat')
    
    XLAND_MARK = [None]*(int(SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP) -int(SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START))
    YLAND_MARK = [None]*(int(SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP) -int(SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START))
    
    cap = cv2.VideoCapture(NUMBER_OF_CAMERA_OR_VIDEO_DIR) # select camera to capture frames
    
    
    if (cap.isOpened() == False): 
      print("Unable to read camera feed")
    
    # dimensions of output whole video
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    # supposed to get the fps however as we add more features the fps drops and it is thuse inacurate. For some reason the actial value extracted from the camera is 30 however in practice we get just 15
    INPUT_VID_FPS = cap.get(5)
    
    if OUTPUT_FPS == 'same':
        OUTPUT_FPS = cap.get(5)
    else:
        pass
    
    '''
    # more info at https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html
    NUMBER_OF_FRAMES_IN_VIDEO = cap.get(7)
    # cap = cv2.VideoCapture("video.mp4")
    #total_frames = cap.get(7)
    #
    get the time
    time = cap.get(0)# in miliseconds
    
    
    '''
    
    # dimensions of croped region
    cropped_width = CROPPED_WIDTH # edit as you like it is in pixels
    cropped_height = CROPPED_HEIGHT # edit as you like
    
    center_x_coordinate= int(frame_width/2)
    center_y_coordinate= int(frame_height/2)
    
    top_left_corner_x_coordinate = int(center_x_coordinate - int(cropped_width/2))
    top_left_corner_y_coordinate = int(center_y_coordinate + int(cropped_height/2))
    
    bottom_right_corner_x_coordinate = int(center_x_coordinate + int(cropped_width/2))
    bottom_right_corner_y_coordinate = int(center_y_coordinate - int(cropped_height/2))
    
    
    if ENABLE_CUBIC_LAND_MARK_TRACKING == True:
        cropped_width = frame_width
        cropped_height = frame_height
    else:
        pass
    
    # Option to save whole video
    if SAVE_WHOLE == True:
        out_normal = cv2.VideoWriter(OUTPUT_FILE_NAME + OUTPUT_FILE_NAME_EXTENSION,cv2.VideoWriter_fourcc(FOURCC1,FOURCC2,FOURCC3,FOURCC4), OUTPUT_FPS, (frame_width,frame_height)) # format to save normal recorded video
    elif SAVE_WHOLE == False:
        pass
    else:
        pass
    
    # Option to save cropped video
    CROPPED_VIDEO_FILENAME =  OUTPUT_FILE_NAME + ADD_STR_CROPPED_FILE_NAME + OUTPUT_FILE_NAME_EXTENSION

    if SAVE_CROPPED == True:
        out_croped = cv2.VideoWriter(CROPPED_VIDEO_FILENAME,cv2.VideoWriter_fourcc(FOURCC1,FOURCC2,FOURCC3,FOURCC4), OUTPUT_FPS, (cropped_width,cropped_height)) # format to save croped recorded video
    elif SAVE_CROPPED == False:
        pass
    else:
        pass

    start_timer = time.time()
    while(True):
      ret, frame = cap.read()
      if ret == True:
          LIST_FRAME_INDEX.append(FRAME_INDEX)
          #0, for flipping the image around the x-axis (vertical flipping);
          #> 0 for flipping around the y-axis (horizontal flipping);
          #< 0 for flipping around both axe FLIP == True, FLIP_ARGUMENT =1
          if FLIP == True:
              frame = cv2.flip(frame, FLIP_ARGUMENT)
          else:
              pass
          
          gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          faces = detector(gray)
          if int(len(faces)) == 1:
              LIST_FACE_DETECTION_RESULT_PER_FRAME.append(True)
          elif int(len(faces)) == 0:
              LIST_FACE_DETECTION_RESULT_PER_FRAME.append(False)
          elif int(len(faces)) > 1:
              LIST_FACE_DETECTION_RESULT_PER_FRAME.append(str(len(faces)) + ' faces_found')
          else:
              LIST_FACE_DETECTION_RESULT_PER_FRAME.append(['Error'])
              print('something has gone wrong len(faces) is neither 0 or greater')
          for face in faces:
                
              #extract the points
              #x1 = face.left()
              #y1 = face.top()
              #x2 = face.right()
              #y2 = face.bottom()          
              
              # this block of code is used in the determination of the autmatic tracking settings, if it is based on land marks or from face recognition
              if LOAD_FACE_LANDMARKS == True:
                  
                  landmarks = predictor(gray,face)
                  
                  
                  if ENABLE_CUBIC_LAND_MARK_TRACKING == True:
                      x1 = landmarks.part(CUBIC_LAND_MARK_POINT_LEFT).x
                      y1 = landmarks.part(CUBIC_LAND_MARK_POINT_TOP).y
                      x2 = landmarks.part(CUBIC_LAND_MARK_POINT_RIGHT).x
                      y2 = landmarks.part(CUBIC_LAND_MARK_POINT_BOTTOM).y                    
                      #apply shifting
                      x1 = x1 + SHIFT_RIGHT 
                      y1 = y1 + SHIFT_DOWN
                      x2 = x2 + SHIFT_RIGHT
                      y2 = y2 + SHIFT_DOWN
                      # apply extensions
                      x1 = int(x1 - CROPPED_WIDTH/2)
                      y1 = int(y1 - CROPPED_HEIGHT/2)
                      x2 = int(x2 + CROPPED_WIDTH/2)
                      y2 = int(y2 + CROPPED_HEIGHT/2)
                  else: 
                      if POINT_LAND_MARK_TRACKING == True:
                         
                          y1 = landmarks.part(LAND_MARK_TRACKING_NUMBER).y
                          x1 = landmarks.part(LAND_MARK_TRACKING_NUMBER).x
                          # apply shifting
                          x1 = x1 + SHIFT_RIGHT
                          y1 = y1 + SHIFT_DOWN
                          
                      elif POINT_LAND_MARK_TRACKING == False:
                          
                          if LAND_MARK_LIP_TRACKING == True:
                              x1 = landmarks.part(33).x
                              y1 = landmarks.part(33).y
                              # apply shifting
                              x1 = x1 + SHIFT_RIGHT
                              y1 = y1 + SHIFT_DOWN
                              
                          elif LAND_MARK_LIP_TRACKING == False:
                              # uses face recognition coordinates insted
                              x1 = face.left()
                              y1 = face.top()
                              # x2 = face.right()
                              # y2 = face.bottom()
                              x1 = x1 + SHIFT_RIGHT
                              y1 = y1 + SHIFT_DOWN
                              
                          else:
                              
                              x1 = face.left()
                              y1 = face.top()
                              # x2 = face.right()
                              # y2 = face.bottom()
                              x1 = x1 + SHIFT_RIGHT
                              y1 = y1 + SHIFT_DOWN
                      
                              
                      else:
                          
                          x1 = face.left()
                          y1 = face.top()
                          # x2 = face.right()
                          # y2 = face.bottom()
                          x1 = x1 + SHIFT_RIGHT
                          y1 = y1 + SHIFT_DOWN
    
    
    
                      
                  if (DISPLAY_FACE_LANDMARKS ==True and CAPTURE_FACE_LANDMARKS == True):
                      # extract the landmark coordinates for the points
                      for i in range(SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP):
                          XLAND_MARK[i-SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START] = landmarks.part(i).x
                          YLAND_MARK[i-SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START] = landmarks.part(i).y        
                          cv2.circle(frame, (XLAND_MARK[i-SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START],YLAND_MARK[i-SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START]), 1, (255, 255, 0), -1)
                      # list of landmark points for x and y
                      LIST_SINGLE_FRAME_LANDMARK_RESULT = [XLAND_MARK[:],YLAND_MARK[:]]
                      LIST_LANDMARK_RESULT_PER_INPUT.append(LIST_SINGLE_FRAME_LANDMARK_RESULT)     
                     
                      #print(str(LIST_LANDMARK_RESULT_PER_INPUT))
                  elif (DISPLAY_FACE_LANDMARKS ==False and CAPTURE_FACE_LANDMARKS == True):
                      # extract the landmark coordinates for the points
                      for i in range(SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP):
                          XLAND_MARK[i-SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START] = landmarks.part(i).x
                          YLAND_MARK[i-SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START] = landmarks.part(i).y    
                      # list of landmark points for x and y
                      LIST_SINGLE_FRAME_LANDMARK_RESULT = [XLAND_MARK[:],YLAND_MARK[:]]
                      LIST_LANDMARK_RESULT_PER_INPUT.append(LIST_SINGLE_FRAME_LANDMARK_RESULT)
                  elif (DISPLAY_FACE_LANDMARKS ==True and CAPTURE_FACE_LANDMARKS == False):
                      print('Landmarks need to be captured in order to be displaied, Set CAPTURE_FACE_LANDMARKS to True')  
                      XLAND_MARK = []
                      YLAND_MARK = []
                  elif (DISPLAY_FACE_LANDMARKS ==False and CAPTURE_FACE_LANDMARKS == False):
                      XLAND_MARK = []
                      YLAND_MARK = []
                  else:
                      XLAND_MARK = []
                      YLAND_MARK = []
                  
              elif LOAD_FACE_LANDMARKS ==False:
                      
                  x1 = face.left()
                  y1 = face.top()
                  # x2 = face.right()
                  # y2 = face.bottom()
                  x1 = x1 + SHIFT_RIGHT
                  y1 = y1 + SHIFT_DOWN
                      
              else:
                      
                  x1 = face.left()
                  y1 = face.top()
                  # x2 = face.right()
                  # y2 = face.bottom()
                  x1 = x1 + SHIFT_RIGHT
                  y1 = y1 + SHIFT_DOWN        
              
              if ENABLE_CUBIC_LAND_MARK_TRACKING == False:
                  x1 = int(x1) 
                  y1 = int(y1) 
                  x2 = int( x1 + cropped_width)
                  y2 = int( y1 + cropped_height)
              else:
                  pass
              
              if int(x2) > frame_width:
                  x2 = frame_width
                  print('Warning parts of the face are not in the camera, check x-axis')
              else:
                  pass
              
              if int(y2) > frame_height:
                  y2 = frame_height
                  print('Warning parts of the face are not in the camera, check y-axis')
              else:
                  pass
              
              
                    
          if ENABLE_FACE_RECOGNITION_TRACKING_CROPING == True:
              try:
                  if ENABLE_CUBIC_LAND_MARK_TRACKING == True:
                      cv2.rectangle(frame,(x1 -1, y1 - 1), (x2 + 1, y2 + 1),(0,225,0),1)
                      
                      #global mask
                      #global mask2
                      #mask2 = frame
                      #global mask3
                      #mask3 = frame[y1:y2,x1:x2]
                      mask = np.zeros_like(frame)
                      mask = cv2.rectangle(mask,(x1, y1), (x2 , y2),(225,225,225),-1) # Show region of  cropeed blue always in the middle
                      result3 = np.bitwise_and(frame,mask)
                      result3[y1:y2,x1:x2] = frame[y1:y2,x1:x2]
#                      result3 = frame[y1:y2,x1:x2]
                      #result3 = np.multiply(frame,mask)
#                      cv2.bitwise_and(result3,mask)
#                      result3 = np.bitwise_and(frame,mask)
#                      result3 = np.bitwise_and(frame,mask)

#                      dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

                      #result3 = frame          
                      #result3[:,:] = 0
                      #result3 = result3 + frame[y1:y2,x1:x2]

                  else:
                      cv2.rectangle(frame,(x1 -1, y1 - 1), (x2 + 1, y2 + 1),(0,225,0),1) 
                      result3 = frame[y1:y2,x1:x2]


                  #A = result3
                  
                  
                  # save whole video
                  if SAVE_WHOLE == True:
                      out_normal.write(frame)
                  elif SAVE_WHOLE == False:
                      pass
                  else:
                      pass
                  
                  #  save cropped video
                  if SAVE_CROPPED == True:
                      out_croped.write(result3)
                  elif SAVE_CROPPED == False:
                      pass
                  else:
                      pass
                  
                  
                  if DISPLAY_WHOLE == True:
                      cv2.imshow('Whole capture',frame)
                  elif DISPLAY_WHOLE == False:
                      pass
                  else:
                      pass
                  
                  if DISPLAY_CHROPPED == True:         
                      cv2.imshow('Cropped capture',result3)
                  elif DISPLAY_CHROPPED == False:
                      pass
                  else:
                      pass
                  
                  
                  #print('4')
                  xx1 = x1
                  xx2 = x2 
                  yy1 = y1
                  yy2 = y2   
                  #FACE_DETECTED = True
                  #print('detected')
        #EDIT
              except:
                  try:
                      # this causes the the captured ouput to remain at the same position if the face is not detected
                      if ENABLE_CUBIC_LAND_MARK_TRACKING == True:
                          
                          cv2.rectangle(frame,(xx1 -1, yy1 - 1), (xx2 + 1, yy2 + 1),(0,0,225),1) 
                          mask = np.zeros_like(frame)
                          mask = cv2.rectangle(mask,(xx1, yy1), (xx2, yy2),(225,225,225),-1) # Show region of  cropeed blue always in the middle
                          result3 = np.bitwise_and(frame,mask)
                          result3[yy1:yy2,xx1:xx2] = frame[yy1:yy2,xx1:xx2]
                      
                      else:
                          cv2.rectangle(frame,(xx1 -1, yy1 + 20), (xx2 + 1, yy2 -20),(0,0,225),1) 
                          result3 = frame[yy1:yy2,xx1:xx2]
                         
                     # save whole video
                      if SAVE_WHOLE == True:
                          out_normal.write(frame)
                      elif SAVE_WHOLE == False:
                          pass
                      else:
                          pass
                      
                      #  save cropped video
                      if SAVE_CROPPED == True:
                          out_croped.write(result3)
                      elif SAVE_CROPPED == False:
                          pass
                      else:
                          pass
    
                      if DISPLAY_WHOLE == True:
                          cv2.imshow('Whole capture',frame)
                      elif DISPLAY_WHOLE == False:
                          pass
                      else:
                          pass
    
    
                      if DISPLAY_CHROPPED == True:         
                          cv2.imshow('Cropped capture',result3)
                      elif DISPLAY_CHROPPED == False:
                          pass
                      else:
                          pass
                      
                      #FACE_DETECTED = False
                      #print('FACE_DETECTED = ' +str(FACE_DETECTED) +' please position your face in the center of the camera.')
                      #print('2')
        
                  except:
                      # use to take into consideration the very first frame which it probably won't be in the 
                      if ENABLE_CUBIC_LAND_MARK_TRACKING == True:
                          cv2.rectangle(frame,(top_left_corner_x_coordinate - 1, top_left_corner_y_coordinate + 1), (bottom_right_corner_x_coordinate + 1, bottom_right_corner_y_coordinate -1),(255,0,0),1) # Show region of  cropeed blue always in the middle
                          mask = np.zeros_like(frame)
                          mask = cv2.rectangle(mask,(top_left_corner_x_coordinate - 1, top_left_corner_y_coordinate + 1), (bottom_right_corner_x_coordinate + 1, bottom_right_corner_y_coordinate -1),(225,225,225),-1) # Show region of  cropeed blue always in the middle
                          result3 = np.bitwise_and(frame,mask)
                          result3[bottom_right_corner_y_coordinate:top_left_corner_y_coordinate,top_left_corner_x_coordinate:bottom_right_corner_x_coordinate] = frame[y1:y2,x1:x2]
                      
                          
                          
                      else:
                          cv2.rectangle(frame,(top_left_corner_x_coordinate - 1, top_left_corner_y_coordinate + 1), (bottom_right_corner_x_coordinate + 1, bottom_right_corner_y_coordinate -1),(255,0,0),1) # Show region of  cropeed blue always in the middle
                          result3 = frame[bottom_right_corner_y_coordinate:top_left_corner_y_coordinate,top_left_corner_x_coordinate:bottom_right_corner_x_coordinate]
    
                      
    
                      #  save cropped video
                      if SAVE_CROPPED == True:
                          out_croped.write(result3)
                      elif SAVE_CROPPED == False:
                          pass
                      else:
                          pass
                      
                      # save whole video
                      if SAVE_WHOLE == True:
                          out_normal.write(frame)
                      elif SAVE_WHOLE == False:
                          pass
                      else:
                          pass
    
                      if DISPLAY_WHOLE == True:
                          cv2.imshow('Whole capture',frame)
                      elif DISPLAY_WHOLE == False:
                          pass
                      else:
                          pass
        
                      if DISPLAY_CHROPPED == True:         
                          cv2.imshow('Cropped capture',result3)
                      elif DISPLAY_CHROPPED == False:
                          pass
                      else:
                          pass
                      #FACE_DETECTED = False
                      #print('FACE_DETECTED = ' +str(FACE_DETECTED) +' please position your face in the center of the camera.')
                      
          
          elif ENABLE_FACE_RECOGNITION_TRACKING_CROPING == False:
            # use to take into consideration the very first frame which it probably won't be in the 
              cv2.rectangle(frame,(top_left_corner_x_coordinate - 1, top_left_corner_y_coordinate + 1), (bottom_right_corner_x_coordinate + 1, bottom_right_corner_y_coordinate -1),(255,0,0),1) # Show region of  cropeed blue always in the middle
              result3 = frame[bottom_right_corner_y_coordinate:top_left_corner_y_coordinate,top_left_corner_x_coordinate:bottom_right_corner_x_coordinate]
              #C = result3
    
              
    
              #  save cropped video
              if SAVE_CROPPED == True:
                  out_croped.write(result3)
              elif SAVE_CROPPED == False:
                  pass
              else:
                  pass          
              
              # save whole video
                  if SAVE_WHOLE == True:
                      out_normal.write(frame)
                  elif SAVE_WHOLE == False:
                      pass
                  else:
                      pass
              
              
              if DISPLAY_WHOLE == True:
                  cv2.imshow('Whole capture',frame)
              elif DISPLAY_WHOLE == False:
                  pass
              else:
                  pass
    
    
              if DISPLAY_CHROPPED == True:         
                  cv2.imshow('Cropped capture',result3)
              elif DISPLAY_CHROPPED == False:
                  pass
              else:
                  pass      
              
              #print('FACE_DETECTED = ' +str(FACE_DETECTED) +' please position your face in the center of the camera.')
              FACE_DETECTED = False
          FRAME_INDEX = FRAME_INDEX + 1
              
          if len(LIST_FRAME_INDEX) == len(LIST_LANDMARK_RESULT_PER_INPUT):
              pass
          elif len(LIST_FRAME_INDEX) == (len(LIST_LANDMARK_RESULT_PER_INPUT) + 1):
                LIST_LANDMARK_RESULT_PER_INPUT.append(None)
          else:
              print('something has gone wrong, LIST_LANDMARK_RESULT_PER_INPUT is neither equal or smaller by 1 ')
              pass

          if cv2.waitKey(1) & 0xFF == ord('q') or FUTURE_KILL_SWITCH == True or cap.isOpened() == False:
              break
          
      else:
        break
    
    cap.release()
    stop_timer = time.time()

   # save whole video
    if SAVE_WHOLE == True:
        out_normal.release()
    elif SAVE_WHOLE == False:
        pass
    else:
        pass
    
    # terminate cropped video 
    if SAVE_CROPPED == True:
        print('Saved ' + str(CROPPED_VIDEO_FILENAME))
        out_croped.release()
    elif SAVE_CROPPED == False:
        pass
    else:
        pass

    cv2.destroyAllWindows()# Closes all the frames

    MEASURED_RECORDING_PROCESSING_TIME = stop_timer - start_timer
    NUMBER_OF_FRAMES = len(LIST_FACE_DETECTION_RESULT_PER_FRAME)

    
    if NUMBER_OF_FRAMES == 0:
        MEASURED_FPS = NUMBER_OF_FRAMES/MEASURED_RECORDING_PROCESSING_TIME     
        NUMBER_OF_FRAMES_FACE_IS_DETECTED = 0   
        RATIO_OF_DETECTED_FACES_PER_FRAME = 0
        print('Warning video: ' + str(CROPPED_VIDEO_FILENAME) + ' does not contain any frames')
    else:
        MEASURED_FPS = NUMBER_OF_FRAMES/MEASURED_RECORDING_PROCESSING_TIME     
        NUMBER_OF_FRAMES_FACE_IS_DETECTED = LIST_FACE_DETECTION_RESULT_PER_FRAME.count(True)    
        RATIO_OF_DETECTED_FACES_PER_FRAME = float(NUMBER_OF_FRAMES_FACE_IS_DETECTED/NUMBER_OF_FRAMES)
    
    #FACE_DETECTION_RESULT = pd.DataFrame(dict) 
    dict = {'Frame Index': LIST_FRAME_INDEX, 'LIST_FACE_DETECTION_RESULT_PER_FRAME': LIST_FACE_DETECTION_RESULT_PER_FRAME, 'X-Y Land Mark Coordinates': LIST_LANDMARK_RESULT_PER_INPUT}
    LANDMARK_TRACKING_RESULT = pd.DataFrame(dict) 
    
    #CSV_RESULT_RECORD = FACE_DETECTION_RESULT
    CSV_LANDMARK_TRACKING_RESULT = LANDMARK_TRACKING_RESULT
    #save option to be added for both sentence and word samples. Remember to add the SAVE = True OPTION and the SAVE_FILE_NAME OPTION (sentence_chunk_samples_info and word_chunk_samples_info)
    
    if SAVE_LANDMARK_TRACKING_RESULTS == True:
        #CSV_RESULT_RECORD.to_csv(SAVE_LANDMARK_TRACKING_RESULTS_NAME, index = True, header=True)
        CSV_LANDMARK_TRACKING_RESULT.csv(SAVE_LANDMARK_TRACKING_RESULTS_NAME+'_landmarks', index = True, header=True)
    else:
        pass
    
    return CROPPED_VIDEO_FILENAME, RATIO_OF_DETECTED_FACES_PER_FRAME, NUMBER_OF_FRAMES, LANDMARK_TRACKING_RESULT, MEASURED_RECORDING_PROCESSING_TIME, MEASURED_FPS, INPUT_VID_FPS






''' SIMPLY UNCOMMENT EACH ONE OF THE SETTINGS AND EXPERIMENT'''

# setting -2 No face recognition, just  keep your face in the middle
cropped_video_filename, ratio_of_detected_faces_per_frame, number_of_frames, landmark_tracking_result, measured_recording_processing_time, measured_fps, input_vid_fps = file_face_rec_and_cropping(SAVE_WHOLE = False, SAVE_CROPPED = True, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', DISPLAY_WHOLE = True, DISPLAY_CHROPPED = True, OUTPUT_FILE_NAME = 'camera_recording_no_face_recognition', ADD_STR_CROPPED_FILE_NAME = '_cropped', OUTPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 105, CROPPED_HEIGHT = 90, SHIFT_RIGHT = -10, SHIFT_DOWN = 600, OUTPUT_FPS = 10, NUMBER_OF_CAMERA_OR_VIDEO_DIR = 0, ENABLE_FACE_RECOGNITION_TRACKING_CROPING = False, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, FUTURE_KILL_SWITCH = False, LOAD_FACE_LANDMARKS = False, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = False, CAPTURE_FACE_LANDMARKS = False, DISPLAY_FACE_LANDMARKS = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34, CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT =1, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START = 48, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP = 68)

# setting -1 Face tracking lips #Note shifting and cropping settings are ingored as the LIPS_PROFILE = True overides input settings
#cropped_video_filename, ratio_of_detected_faces_per_frame, number_of_frames, landmark_tracking_result, measured_recording_processing_time, measured_fps, input_vid_fps = file_face_rec_and_cropping(SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = True, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', DISPLAY_CHROPPED = True, OUTPUT_FILE_NAME = 'camera_recording_lip_tracking1', ADD_STR_CROPPED_FILE_NAME = '_cropped', OUTPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 105, CROPPED_HEIGHT = 90, SHIFT_RIGHT = -10, SHIFT_DOWN = 600, OUTPUT_FPS = 10, NUMBER_OF_CAMERA_OR_VIDEO_DIR = 0, ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = True, FUTURE_KILL_SWITCH = False, LOAD_FACE_LANDMARKS = False, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = False, CAPTURE_FACE_LANDMARKS = False, DISPLAY_FACE_LANDMARKS = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34, CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT =1, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START = 48, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP = 68)


# setting 0 Face tracking Face
#cropped_video_filename, ratio_of_detected_faces_per_frame, number_of_frames, landmark_tracking_result, measured_recording_processing_time, measured_fps, input_vid_fps = file_face_rec_and_cropping(SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = True, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', DISPLAY_CHROPPED = True, OUTPUT_FILE_NAME = 'camera_recording_face_tracking1', ADD_STR_CROPPED_FILE_NAME = '_cropped', OUTPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 105, CROPPED_HEIGHT = 90, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 10, NUMBER_OF_CAMERA_OR_VIDEO_DIR = 0, ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = True, LIPS_PROFILE = False, FUTURE_KILL_SWITCH = False, LOAD_FACE_LANDMARKS = False, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = False, CAPTURE_FACE_LANDMARKS = False, DISPLAY_FACE_LANDMARKS = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34, CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT =1, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START = 48, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP = 68)

# setting 1 Point landmark fixed cropped region of the lips
#cropped_video_filename, ratio_of_detected_faces_per_frame, number_of_frames, landmark_tracking_result, measured_recording_processing_time, measured_fps, input_vid_fps = file_face_rec_and_cropping(SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = True, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', DISPLAY_CHROPPED = True, OUTPUT_FILE_NAME = 'camera_recording_fixed_cropped_reggion_of_lips', ADD_STR_CROPPED_FILE_NAME = '_cropped', OUTPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 105, CROPPED_HEIGHT = 90, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 10, NUMBER_OF_CAMERA_OR_VIDEO_DIR = 0, ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, FUTURE_KILL_SWITCH = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = True, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34, CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT =1, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START = 48, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP = 68)


# setting 2 Point landmark fixed cropped region of the head do not display landmarks. It should be mentioned that the option not to output the video is also available however we will need some form to stop the recording which is currently accomplished by pressing on the displayed windown and then the 'q' key stroke
#cropped_video_filename, ratio_of_detected_faces_per_frame, number_of_frames, landmark_tracking_result, measured_recording_processing_time, measured_fps, input_vid_fps = file_face_rec_and_cropping(SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = True, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', DISPLAY_CHROPPED = True, OUTPUT_FILE_NAME = 'camera_recording_fixed_cropped_reggion_of_face', ADD_STR_CROPPED_FILE_NAME = '_cropped', OUTPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 110, CROPPED_HEIGHT = 100, SHIFT_RIGHT = -40, SHIFT_DOWN = -700, OUTPUT_FPS = 10, NUMBER_OF_CAMERA_OR_VIDEO_DIR = 0, ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = True, LIPS_PROFILE = False, FUTURE_KILL_SWITCH = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = True, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = False, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = True, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34, CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT =1, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START = 48, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP = 68)

# setting 3
#cropped_video_filename, ratio_of_detected_faces_per_frame, number_of_frames, landmark_tracking_result, measured_recording_processing_time, measured_fps, input_vid_fps = file_face_rec_and_cropping(SAVE_WHOLE = True, SAVE_CROPPED = True, DISPLAY_WHOLE = True, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', DISPLAY_CHROPPED = True, OUTPUT_FILE_NAME = 'camera_recording_flexible_cropped_reggion_of_lips2', ADD_STR_CROPPED_FILE_NAME = '_cropped', OUTPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 35, CROPPED_HEIGHT = 10, SHIFT_RIGHT = -2, SHIFT_DOWN = 0, OUTPUT_FPS = 10, NUMBER_OF_CAMERA_OR_VIDEO_DIR = 0, ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, FUTURE_KILL_SWITCH = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = True, ENABLE_CUBIC_LAND_MARK_TRACKING = True, CUBIC_LAND_MARK_POINT_TOP = 52,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 58, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT =1, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START = 48, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP = 68)

#
# on youtube video in dir girl setting 4
#cropped_video_filename, ratio_of_detected_faces_per_frame, number_of_frames, landmark_tracking_result, measured_recording_processing_time, measured_fps, input_vid_fps = file_face_rec_and_cropping(SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = True, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', DISPLAY_CHROPPED = True, OUTPUT_FILE_NAME = 'camera_recording_on_moving_to_the_uk', ADD_STR_CROPPED_FILE_NAME = '_cropped', OUTPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 160, CROPPED_HEIGHT = 105, SHIFT_RIGHT = -70, SHIFT_DOWN = 0, OUTPUT_FPS = 24, NUMBER_OF_CAMERA_OR_VIDEO_DIR = '/media/god/9c72f9bb-20f1-4b7b-8a9e-01f045898c0e/god/LEARNING/UniSheff/Mech/4/FYP/fyp-code/useful_bit/important_files/Moving_to_the_UK_to_study_Finnish_Girls_Experience.mkv', ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, FUTURE_KILL_SWITCH = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = True, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 52,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 58, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT =1, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START = 48, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP = 68)

# on youtube video in dir trump setting 5
#cropped_video_filename, ratio_of_detected_faces_per_frame, number_of_frames, landmark_tracking_result, measured_recording_processing_time, measured_fps, input_vid_fps = file_face_rec_and_cropping(SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = True, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', DISPLAY_CHROPPED = True, OUTPUT_FILE_NAME = 'camera_recording_trump', ADD_STR_CROPPED_FILE_NAME = '_cropped', OUTPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 35, CROPPED_HEIGHT = 10, SHIFT_RIGHT = -2, SHIFT_DOWN = 0, OUTPUT_FPS = 10, NUMBER_OF_CAMERA_OR_VIDEO_DIR = '/media/god/9c72f9bb-20f1-4b7b-8a9e-01f045898c0e/god/LEARNING/UniSheff/Mech/4/FYP/fyp-code/useful_bit/important_files/Donald_Trump_suspends_US_travel_from_26_European_countries_but_not_the_UK_to_fight_coronavirus.mkv', ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, FUTURE_KILL_SWITCH = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = True, ENABLE_CUBIC_LAND_MARK_TRACKING = True, CUBIC_LAND_MARK_POINT_TOP = 52,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 58, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT =1, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_START = 0, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINT_STOP = 2)