# Tool-for-creating-lip-recognition-datasets

This program is an open source tool which will culd be used to create datasets suitable train lip recognition machine learning algorithms. All of the results are saved locally. No subtitle to audio or audio to video alignment is applied at the moment. The video is chopped at the times in which subtitles are presented in the video. There are alot of improvements that could be made.


## Requirements

Make sure you are connected to the internet.
You will need ffmpeg and youtube-dl installed.
The code was tested on Ubuntu 19.04 and python 3.7.7 in the anaconda environment.
Note: In order for the code to run download the shape_predictor_68_face_landmarks.dat file from here https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/ and place it in the same folder with main.py and the rest of the scripts. Make sure the name is exactly 'shape_predictor_68_face_landmarks.dat'.
 An IDE such as spyder is recommended as it displays the variables values.
 
 
## Instructions 

Simply open main.py and run it to for an example result.
Just specify the URL and a name.

For a realtime demo of face detection and cropping open DEMO_face_detect.py, uncomment some example code in the file and run it.


## For more information and list of Options

Please read the pdf file 'Demetrios Loizides Final Year Project.pdf' or see the video demonstration I have made from here https://drive.google.com/file/d/1pw_bmya_RYbQ8jZJynZV7JgTkbRnmK-O/view?usp=sharing.

Thank you.
