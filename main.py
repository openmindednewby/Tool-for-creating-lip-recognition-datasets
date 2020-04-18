''' Every type you encounter ##EDIT_ME## you will need to adjust these settings '''
''' Here we download and process youtube videos in a format in which ML algorithms can be trained.'''
''' Tested on Ubuntu 19.4 and python 3.7.7'''
import pandas as pd
import numpy as np
import module_youtube_extract
#import module_compare_subtitles
import module_convert_audio_to_wav
import module_process_subtitles
import module_save_variables
import module_video_processing
import module_sample_name
import module_face_detection



##EDIT_ME##
#---
# tested and it works
#INPUT_URL='https://www.youtube.com/watch?v=6cXdS_qVfUc'

# tested and it works
#INPUT_URL= 'https://www.youtube.com/watch?v=v2Q3eoUldcE'

# tested and it works
INPUT_URL= 'https://www.youtube.com/watch?v=kayOhGRcNt4'


#---
#FILE_NAME
# download everithing into a new folder just add folder_name/file_name
# to avioid errors and extra work make sure that the variables created do not contain special characters or spaces

#-2
# It is recomaneded that the folder in which all the information for each video is created first as some functions produce errors if it does not presxists. 
# This generates a random string which will be assigned to the the function which creates a file
random_string_INPUT = str(module_sample_name.passw_gen(MODE=0, LENGTH=3))

# Optional 
# You can spcify the exact folder path or name that you would like everithing to be downloaded and storded in simply assing the directory name to random_string_INPUT
# Example
#random_string_INPUT = '/media/username/name_of_storage_device/Folder-name'

#-1
#FOLDER_PATH = str('a')
FOLDER_PATH = module_sample_name.folder_gen(RANDOM_STRING = random_string_INPUT, FILE_PERMISION = '777')

##EDIT_ME##
# avoid special characters appart from _ and remember to add / before the name
#NNAME = '/Donald Trump suspends US travel from 26 European countries but not the UK to fight coronavirus'
#NNAME = '/Moving to the UK to study Finnish Girls Experience'
NNAME = '/Tell Me About Yourself - A Good Answer to This Interview Question'

#  remove any spaces if they exists in the path as that may introduce errors. Note_if there are space0 or in the absolute directory path, this might introduce errors.
NNAME = NNAME.replace(' ', '_')

INPUT_FILE_NAME=str(FOLDER_PATH) + NNAME



#0
# get a video meta data
meta_data = module_youtube_extract.meta_data(URL = INPUT_URL, FILE_NAME = INPUT_FILE_NAME , TXT_CLEAN=True, TXT=True, JSON=True, DOWNLOAD=False)

#1
# get all available downloadble formats
available_formats = module_youtube_extract.list_available_AV_formats(URL = INPUT_URL, CLEAN=True, LIST=True, SAVE=True, FILE_NAME = INPUT_FILE_NAME+'_down_formats')



#2
# download audio visual content. Note it has been observed that when some of codes are used even thought they are specified as pure video codes they also contain embeded audio such as code 22. There for an additional function is needed to remove the audio.
module_youtube_extract.down_audio_video(URL = INPUT_URL, VIDEO_QUALITY_CODE=22, AUDIO_QUALITY_CODE=140 , MERGE=False, FILE_NAME = INPUT_FILE_NAME)

#7
# Convert m4a into wav file, it is required in order to apply allingment of audio and text
module_convert_audio_to_wav.file_conversion_to_wav(FORMAT_FROM='.m4a', FILE_NAME=INPUT_FILE_NAME, BIT_RATE='192k')


whole_pure_audio_file_name_dir = INPUT_FILE_NAME + '.wav'

#8
#Convert mp4 to mkv format as this elliminates errors in the segmentatio of the videos later on
video_converted_to_mkv = module_video_processing.convert_from_mp4_to_mkv(FILE_NAME=INPUT_FILE_NAME, INPUT_EXTENSION='.mp4', OUTPUT_EXTENSION = '.mkv')

#9
# remove the audio from the mp4 file 

module_video_processing.remove_audio_from_file_mp4(FILE_NAME=INPUT_FILE_NAME, EXTENSION = '.mp4')


#10 
#Convert mp4 to mkv format as this elliminates errors in the segmentatio of the videos later on for the none_audio_ video
video_converted_to_mkv_none_audio = module_video_processing.convert_from_mp4_to_mkv(FILE_NAME=INPUT_FILE_NAME+'_none_audio', INPUT_EXTENSION='.mp4', OUTPUT_EXTENSION = '.mkv')

#3
# Checks to see what subtitles are available and in what format (ex. timings are for every word or)
string_subtitle_formats, manual_subtitles_exist, automatic_subtitles_exist = module_youtube_extract.list_available_subtitles(URL = INPUT_URL, FILE_NAME = INPUT_FILE_NAME, TXT_CLEAN=False, TXT=False, JSON=False)


#4
# downlaods the subtitles
man_sub_var, auto_sub_var = module_youtube_extract.down_sub(URL = INPUT_URL, FILE_NAME=INPUT_FILE_NAME+'SUBTITLES', TYPE='vtt', LANGUAGE='en', MAN_SUB = manual_subtitles_exist, AUTO_SUB = automatic_subtitles_exist, SAVE=True)

#5
# Identify what type of subtitles they are, if they contain contain timings per word or per sentence
man_sub_easy_type, auto_sub_easy_type = module_youtube_extract.sub_type(MAN_SUB = man_sub_var, AUTO_SUB = auto_sub_var, MAN_SUB_EXIST = manual_subtitles_exist, AUTO_SUB_EXIST = automatic_subtitles_exist)


#6
# process the subtitles into an easy to read and process lists which will contain the subtitles and the other the timeings they are presented in the video. Note: if timings are alocated per word which is due to the auto sub gen of Youtube, we will not allign our subtitles to the text as that has been already done. This function takes care of all 3 cases as inputs (no subtitles, sub aligned per sentence, sub aligned per word) for auto and man sub()
'''
acpwe #auto_content_per_word_easy
atpwe #auto_time_per_word_easy

mcpwe #man_content_per_word_easy
mtpwe #man_time_per_word_easy

acpse #auto_content_per_sentence_easy
atpse #auto_time_per_sentence_easy

acpsh #auto_content_per_sentence_hard
atpsh #auto_time_per_sentence_hard

mcpse #man_content_per_sentence_easy
mtpse #man_time_per_sentence_easy

mcpsh #man_content_per_sentence_hard
mtpsh #man_time_per_sentence_hard

'''
# takes input values from #5 #4 #3
acpwe, atpwe, acpse, atpse, acpsh, atpsh, mcpwe, mtpwe, mcpse, mtpse, mcpsh, mtpsh = module_process_subtitles.format_sub(MAN_SUB_EXIST = manual_subtitles_exist, AUTO_SUB_EXIST = automatic_subtitles_exist, MAN_SUB_EASY_TYPE = man_sub_easy_type, AUTO_SUB_EASY_TYPE = auto_sub_easy_type, MAN_SUB = man_sub_var, AUTO_SUB = auto_sub_var)


video_converted_to_mkv_none_audio_no_extension = video_converted_to_mkv_none_audio.replace('.mkv','')


video_converted_to_mkv_none_audio_no_extension = list(video_converted_to_mkv_none_audio_no_extension)



##EDIT_ME##
# adjust the following variables
# Controll chopping properties on acpwe, atpwe, acpse, atpse, acpsh, atpsh, mcpwe, mtpwe, mcpse, mtpse, mcpsh, mtpsh for all chopped samples.
# This values are feed into module_video_processing.chop_video_per_word_or_sentence

# in milliseconds
shift_right_or_left_acpwe = 0
shift_right_or_left_mcpwe = 0
shift_right_or_left_acpse = 0
shift_right_or_left_acpsh = 0
shift_right_or_left_mcpse = 0
shift_right_or_left_mcpsh = 0

# in milliseconds extend left
extend_left_acpwe = -150
extend_left_mcpwe = -150
extend_left_acpse = -150
extend_left_acpsh = -150
extend_left_mcpse = -150
extend_left_mcpsh = -150

# in milliseconds extend right
extend_right_acpwe = 150
extend_right_mcpwe = 150
extend_right_acpse = 150
extend_right_acpsh = 150
extend_right_mcpse = 150
extend_right_mcpsh = 150

# start word or sentence index from  acpwe, atpwe, acpse, atpse, acpsh, atpsh, mcpwe, mtpwe, mcpse, mtpse, mcpsh, mtpsh 
start_index_acpwe = 0
start_index_mcpwe = 0
start_index_acpse = 0
start_index_acpsh = 0
start_index_mcpse = 0
start_index_mcpsh = 0

# stop word or sentence index from  acpwe, atpwe, acpse, atpse, acpsh, atpsh, mcpwe, mtpwe, mcpse, mtpse, mcpsh, mtpsh 
stop_index_acpwe = 5 # 'END' # Does the whole video
stop_index_mcpwe = 5
stop_index_acpse = 5
stop_index_acpsh = 5
stop_index_mcpse = 5
stop_index_mcpsh = 5


#12
# Fixed and necessary step
# get the maximum time of the video
max_time = module_video_processing.maximum_time_of_vid(ATPSE=atpse, MTPSE=mtpse, AUTO=True, MAN=False)
if max_time == None:
    max_time = module_video_processing.maximum_time_of_vid(ATPSE=atpsh, MTPSE=mtpsh, AUTO=True, MAN=False)
else:
    pass


if (acpwe == None or acpwe == [] or atpwe == None or atpwe == []):
    word_chunk_samples_info_acpwe = None
    chopped_sample_per_word_folder_dir_acpwe = None
    chopped_sample_per_word_folder_dir_pure_audio_acpwe = None
    chopped_sample_per_word_folder_dir_pure_video_acpwe = None
else:
    #7 OPTIONAL
    # REMOVE OR ELIMINATE SPECIAL CHARACTERS. CARE MUST BE TAKEN NOT TO INPUT THE TIME VALUES 
    acpwe = module_process_subtitles.remove_or_replace_special_char(INPUT_SUB_LIST = acpwe, CHAR_TO_REPLACE = 'all', CHAR_TO_REPLACE_WITH = '')
    #9
    # function to save subtitles in easy to read format
    #acpwe
    module_save_variables.save_sub(VAR_INPUT=acpwe, FILE_NAME=INPUT_FILE_NAME+'_acpwe', TXT=False, JSON=True, TXT_SEPARATOR = '\n')    

    #11
    # create a folders to store all chopped samples #chopped_sample_per_word_folder_dir
    chopped_sample_per_word_folder_dir_acpwe = module_sample_name.folder_gen(RANDOM_STRING = FOLDER_PATH + '/chopped_samples_per_word_acpwe', FILE_PERMISION = '777')
  
    #13
    # acpwe and atpwe 
    # split the video into chunks of each word per video and save them in the chopped_samples_per_word folder #word_chunk_samples_info
    word_chunk_samples_info_acpwe = module_video_processing.chop_video_per_word_or_sentence(LIST_PER_WORD = acpwe, TIMES_PER_WORD = atpwe, MAX_TIME = max_time, FILE_NAME = INPUT_FILE_NAME,  CHOPPED_SAMPLE_FOLDER_DIR = chopped_sample_per_word_folder_dir_acpwe, SAVE_FILE_NAME = chopped_sample_per_word_folder_dir_acpwe + '/word_chunk_samples_info_acpwe.csv', SHIFT_RIGHT_OR_LEFT = shift_right_or_left_acpwe, EXTEND_LEFT = extend_left_acpwe, EXTEND_RIGHT = extend_right_acpwe, EXTENSION = '.mkv', START_INDEX = start_index_acpwe, STOP_INDEX = stop_index_acpwe, SAVE = True)
   
    
    #15
    # create new folders which will contain only the audio segments, the none-audio video segments and combined audio and video cropped result
    # create a folders to store all chopped samples
    # chopped_sample_per_word_folder_dir_pure_audio
    chopped_sample_per_word_folder_dir_pure_audio_acpwe = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_word_folder_dir_acpwe + '/pure_audio', FILE_PERMISION = '777')
    
    chopped_sample_per_word_folder_dir_pure_video_acpwe = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_word_folder_dir_acpwe + '/pure_video', FILE_PERMISION = '777')
    

    
if (mcpwe == None or mcpwe == [] or mtpwe == None or mtpwe == []):
    word_chunk_samples_info_mcpwe = None
    chopped_sample_per_word_folder_dir_mcpwe = None
    chopped_sample_per_word_folder_dir_pure_audio_mcpwe = None
    chopped_sample_per_word_folder_dir_pure_video_mcpwe = None
else:
    #7 OPTIONAL
    # REMOVE OR ELIMINATE SPECIAL CHARACTERS. CARE MUST BE TAKEN NOT TO INPUT THE TIME VALUES 
    mcpwe = module_process_subtitles.remove_or_replace_special_char(INPUT_SUB_LIST = mcpwe, CHAR_TO_REPLACE = 'all', CHAR_TO_REPLACE_WITH = '')
    #9
    # function to save subtitles in easy to read format
    #mcpwe
    module_save_variables.save_sub(VAR_INPUT=mcpwe, FILE_NAME=INPUT_FILE_NAME+'_mcpwe', TXT=False, JSON=True, TXT_SEPARATOR = '\n')    

    #11
    # create a folders to store all chopped samples #chopped_sample_per_word_folder_dir
    chopped_sample_per_word_folder_dir_mcpwe = module_sample_name.folder_gen(RANDOM_STRING = FOLDER_PATH + '/chopped_samples_per_word_mcpwe', FILE_PERMISION = '777')
    
    
    #13
    # mcpwe and mtpwe 
    # split the video into chunks of each word per video and save them in the chopped_samples_per_word folder #word_chunk_samples_info
    word_chunk_samples_info_mcpwe = module_video_processing.chop_video_per_word_or_sentence(LIST_PER_WORD = mcpwe, TIMES_PER_WORD = mtpwe, MAX_TIME = max_time, FILE_NAME = INPUT_FILE_NAME,  CHOPPED_SAMPLE_FOLDER_DIR = chopped_sample_per_word_folder_dir_mcpwe, SAVE_FILE_NAME = chopped_sample_per_word_folder_dir_mcpwe + '/word_chunk_samples_info_mcpwe.csv', SHIFT_RIGHT_OR_LEFT = shift_right_or_left_mcpwe, EXTEND_LEFT = extend_left_mcpwe, EXTEND_RIGHT = extend_right_mcpwe, EXTENSION = '.mkv', START_INDEX = start_index_mcpwe, STOP_INDEX = stop_index_mcpwe, SAVE = True)
   
    #15
    # create new folders which will contain only the audio segments and the none-audio video segments
    # create a folders to store all chopped samples
    # chopped_sample_per_word_folder_dir_pure_audio
    chopped_sample_per_word_folder_dir_pure_audio_mcpwe = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_word_folder_dir_mcpwe + '/pure_audio', FILE_PERMISION = '777')
    
    chopped_sample_per_word_folder_dir_pure_video_mcpwe = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_word_folder_dir_mcpwe + '/pure_video', FILE_PERMISION = '777') 


if (acpse == None or acpse == [] or atpse == None or atpse == []):
    sentence_chunk_samples_info_acpse = None
    chopped_sample_per_sentence_folder_dir_acpse = None
    chopped_sample_per_sentence_folder_dir_pure_audio_acpse = None
    chopped_sample_per_sentence_folder_dir_pure_video_acpse = None
else:
    #7 OPTIONAL
    # REMOVE OR ELIMINATE SPECIAL CHARACTERS. CARE MUST BE TAKEN NOT TO INPUT THE TIME VALUES 
    acpse = module_process_subtitles.remove_or_replace_special_char(INPUT_SUB_LIST = acpse, CHAR_TO_REPLACE = 'all', CHAR_TO_REPLACE_WITH = '')
    #9
    # function to save subtitles in easy to read format
    #acpse
    module_save_variables.save_sub(VAR_INPUT=acpse, FILE_NAME=INPUT_FILE_NAME+'_acpse', TXT=False, JSON=True, TXT_SEPARATOR = '\n')    

    #11
    # create a folders to store all chopped samples #chopped_sample_per_sentence_folder_dir
    chopped_sample_per_sentence_folder_dir_acpse = module_sample_name.folder_gen(RANDOM_STRING = FOLDER_PATH + '/chopped_samples_per_sentence_acpse', FILE_PERMISION = '777')
    
    #13
    # acpse and atpse 
    # split the video into chunks of each word per video and save them in the chopped_samples_per_word folder #sentence_chunk_samples_info 
    sentence_chunk_samples_info_acpse = module_video_processing.chop_video_per_word_or_sentence(LIST_PER_WORD = acpse, TIMES_PER_WORD = atpse, MAX_TIME = max_time, FILE_NAME = INPUT_FILE_NAME,  CHOPPED_SAMPLE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpse, SAVE_FILE_NAME = chopped_sample_per_sentence_folder_dir_acpse + '/sentence_chunk_samples_info_acpse.csv', SHIFT_RIGHT_OR_LEFT = shift_right_or_left_acpse, EXTEND_LEFT = extend_left_acpse, EXTEND_RIGHT = extend_right_acpse, EXTENSION = '.mkv', START_INDEX = start_index_acpse, STOP_INDEX = stop_index_acpse, SAVE = True)
    
    #15
    # create new folders which will contain only the audio segments and the none-audio video segments
    # create a folders to store all chopped samples
    # chopped_sample_per_sentence_folder_dir_pure_audio
    
    chopped_sample_per_sentence_folder_dir_pure_audio_acpse = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_sentence_folder_dir_acpse + '/pure_audio', FILE_PERMISION = '777')
    chopped_sample_per_sentence_folder_dir_pure_video_acpse = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_sentence_folder_dir_acpse + '/pure_video', FILE_PERMISION = '777')



if (acpsh == None or acpsh == [] or atpsh == None or atpsh == []):
    sentence_chunk_samples_info_acpsh = None
    chopped_sample_per_sentence_folder_dir_acpsh = None
    chopped_sample_per_sentence_folder_dir_pure_audio_acpsh = None
    chopped_sample_per_sentence_folder_dir_pure_video_acpsh = None
else:
    #7 OPTIONAL
    # REMOVE OR ELIMINATE SPECIAL CHARACTERS. CARE MUST BE TAKEN NOT TO INPUT THE TIME VALUES 
    acpsh = module_process_subtitles.remove_or_replace_special_char(INPUT_SUB_LIST = acpsh, CHAR_TO_REPLACE = 'all', CHAR_TO_REPLACE_WITH = '')
    #9
    # function to save subtitles in easy to read format
    #acpsh
    module_save_variables.save_sub(VAR_INPUT=acpsh, FILE_NAME=INPUT_FILE_NAME+'_acpsh', TXT=False, JSON=True, TXT_SEPARATOR = '\n')    

    #11
    # create a folders to store all chopped samples #chopped_sample_per_sentence_folder_dir
    chopped_sample_per_sentence_folder_dir_acpsh = module_sample_name.folder_gen(RANDOM_STRING = FOLDER_PATH + '/chopped_samples_per_sentence_acpsh', FILE_PERMISION = '777')
    
    #13
    # acpsh and atpsh 
    # split the video into chunks of each word per video and save them in the chopped_samples_per_word folder #sentence_chunk_samples_info 
    sentence_chunk_samples_info_acpsh = module_video_processing.chop_video_per_word_or_sentence(LIST_PER_WORD = acpsh, TIMES_PER_WORD = atpsh, MAX_TIME = max_time, FILE_NAME = INPUT_FILE_NAME,  CHOPPED_SAMPLE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpsh, SAVE_FILE_NAME = chopped_sample_per_sentence_folder_dir_acpsh + '/sentence_chunk_samples_info_acpsh.csv', SHIFT_RIGHT_OR_LEFT = shift_right_or_left_acpsh, EXTEND_LEFT = extend_left_acpsh, EXTEND_RIGHT = extend_right_acpsh, EXTENSION = '.mkv', START_INDEX = start_index_acpsh, STOP_INDEX = stop_index_acpsh, SAVE = True)
    
    #15
    # create new folders which will contain only the audio segments and the none-audio video segments
    # create a folders to store all chopped samples
    # chopped_sample_per_sentence_folder_dir_pure_audio
    
    chopped_sample_per_sentence_folder_dir_pure_audio_acpsh = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_sentence_folder_dir_acpsh + '/pure_audio', FILE_PERMISION = '777')
    chopped_sample_per_sentence_folder_dir_pure_video_acpsh = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_sentence_folder_dir_acpsh + '/pure_video', FILE_PERMISION = '777')



if (mcpse == None or mcpse == [] or mtpse == None or mtpse == []):
    sentence_chunk_samples_info_mcpse = None
    chopped_sample_per_sentence_folder_dir_mcpse = None
    chopped_sample_per_sentence_folder_dir_pure_audio_mcpse = None
    chopped_sample_per_sentence_folder_dir_pure_video_mcpse = None
else:
    #7 OPTIONAL
    # REMOVE OR ELIMINATE SPECIAL CHARACTERS. CARE MUST BE TAKEN NOT TO INPUT THE TIME VALUES 
    mcpse = module_process_subtitles.remove_or_replace_special_char(INPUT_SUB_LIST = mcpse, CHAR_TO_REPLACE = 'all', CHAR_TO_REPLACE_WITH = '')
    #9
    # function to save subtitles in easy to read format
    #mcpse
    module_save_variables.save_sub(VAR_INPUT=mcpse, FILE_NAME=INPUT_FILE_NAME+'_mcpse', TXT=False, JSON=True, TXT_SEPARATOR = '\n')    

    #11
    # create a folders to store all chopped samples #chopped_sample_per_sentence_folder_dir
    chopped_sample_per_sentence_folder_dir_mcpse = module_sample_name.folder_gen(RANDOM_STRING = FOLDER_PATH + '/chopped_samples_per_sentence_mcpse', FILE_PERMISION = '777')
    
    #13
    # mcpse and mtpse 
    # split the video into chunks of each word per video and save them in the chopped_samples_per_word folder #sentence_chunk_samples_info 
    sentence_chunk_samples_info_mcpse = module_video_processing.chop_video_per_word_or_sentence(LIST_PER_WORD = mcpse, TIMES_PER_WORD = mtpse, MAX_TIME = max_time, FILE_NAME = INPUT_FILE_NAME,  CHOPPED_SAMPLE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpse, SAVE_FILE_NAME = chopped_sample_per_sentence_folder_dir_mcpse + '/sentence_chunk_samples_info_mcpse.csv', SHIFT_RIGHT_OR_LEFT = shift_right_or_left_mcpse, EXTEND_LEFT = extend_left_mcpse, EXTEND_RIGHT = extend_right_mcpse, EXTENSION = '.mkv', START_INDEX = start_index_mcpse, STOP_INDEX = stop_index_mcpse, SAVE = True)
    
    #15
    # create new folders which will contain only the audio segments and the none-audio video segments
    # create a folders to store all chopped samples
    # chopped_sample_per_sentence_folder_dir_pure_audio
    
    chopped_sample_per_sentence_folder_dir_pure_audio_mcpse = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_sentence_folder_dir_mcpse + '/pure_audio', FILE_PERMISION = '777')
    chopped_sample_per_sentence_folder_dir_pure_video_mcpse = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_sentence_folder_dir_mcpse + '/pure_video', FILE_PERMISION = '777')



if (mcpsh == None or mcpsh == [] or mtpsh == None or mtpsh == []):
    sentence_chunk_samples_info_mcpsh = None
    chopped_sample_per_sentence_folder_dir_mcpsh = None
    chopped_sample_per_sentence_folder_dir_pure_audio_mcpsh = None
    chopped_sample_per_sentence_folder_dir_pure_video_mcpsh = None

else:
    #7 OPTIONAL
    # REMOVE OR ELIMINATE SPECIAL CHARACTERS. CARE MUST BE TAKEN NOT TO INPUT THE TIME VALUES 
    mcpsh = module_process_subtitles.remove_or_replace_special_char(INPUT_SUB_LIST = mcpsh, CHAR_TO_REPLACE = 'all', CHAR_TO_REPLACE_WITH = '')
    #9
    #mcpsh
    module_save_variables.save_sub(VAR_INPUT=mcpsh, FILE_NAME=INPUT_FILE_NAME+'_mcpsh', TXT=False, JSON=True, TXT_SEPARATOR = '\n')    

    #11
    # create a folders to store all chopped samples #chopped_sample_per_sentence_folder_dir
    chopped_sample_per_sentence_folder_dir_mcpsh = module_sample_name.folder_gen(RANDOM_STRING = FOLDER_PATH + '/chopped_samples_per_sentence_mcpsh', FILE_PERMISION = '777')
    
    #13
    # mcpsh and mtpsh 
    # split the video into chunks of each word per video and save them in the chopped_samples_per_word folder #sentence_chunk_samples_info 
    sentence_chunk_samples_info_mcpsh = module_video_processing.chop_video_per_word_or_sentence(LIST_PER_WORD = mcpsh, TIMES_PER_WORD = mtpsh, MAX_TIME = max_time, FILE_NAME = INPUT_FILE_NAME,  CHOPPED_SAMPLE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpsh, SAVE_FILE_NAME = chopped_sample_per_sentence_folder_dir_mcpsh + '/sentence_chunk_samples_info_mcpsh.csv', SHIFT_RIGHT_OR_LEFT = shift_right_or_left_mcpsh, EXTEND_LEFT = extend_left_mcpsh, EXTEND_RIGHT = extend_right_mcpsh, EXTENSION = '.mkv', START_INDEX = start_index_mcpsh, STOP_INDEX = stop_index_mcpsh, SAVE = True)
    
    #15
    # create new folders which will contain only the audio segments, the none-audio video segments and combined audio and video cropped result
    # create a folders to store all chopped samples
    # chopped_sample_per_sentence_folder_dir_pure_audio
    
    chopped_sample_per_sentence_folder_dir_pure_audio_mcpsh = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_sentence_folder_dir_mcpsh + '/pure_audio', FILE_PERMISION = '777')
    chopped_sample_per_sentence_folder_dir_pure_video_mcpsh = module_sample_name.folder_gen(RANDOM_STRING = chopped_sample_per_sentence_folder_dir_mcpsh + '/pure_video', FILE_PERMISION = '777')


#16
# make lists which will contain only the file names of each sample. Process file names 


# new var EXAMPLE
LLIST_INPUT_WORD_CHUNK_SAMPLES_ACPWE_FILE_NAMES = module_video_processing.generate_list_input_word_chunk_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_acpwe)

LLIST_INPUT_WORD_CHUNK_SAMPLES_MCPWE_FILE_NAMES = module_video_processing.generate_list_input_word_chunk_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_mcpwe)



# new var EXAMPLE
LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSH_FILE_NAMES = module_video_processing.generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpsh)

LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSE_FILE_NAMES = module_video_processing.generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpse)

LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSH_FILE_NAMES = module_video_processing.generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpsh)

LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSE_FILE_NAMES = module_video_processing.generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpse)


# new var EXAMPLE
LIST_OUTPUT_AUDIO_WORD_CHOPPED_ACPWE_NAMES = module_video_processing.generate_list_output_audio_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_acpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir_acpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_word_folder_dir_pure_audio_acpwe, AUDIO_EXTENSION = '.wav')

LIST_OUTPUT_AUDIO_WORD_CHOPPED_MCPWE_NAMES = module_video_processing.generate_list_output_audio_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_mcpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir_mcpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_word_folder_dir_pure_audio_mcpwe, AUDIO_EXTENSION = '.wav')


# new var EXAMPLE
LIST_OUTPUT_VIDEO_WORD_CHOPPED_ACPWE_NAMES = module_video_processing.generate_list_output_video_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_acpwe , CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir_acpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_word_folder_dir_pure_video_acpwe, VIDEO_EXTENSION = '.mkv')

LIST_OUTPUT_VIDEO_WORD_CHOPPED_MCPWE_NAMES = module_video_processing.generate_list_output_video_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_mcpwe , CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir_mcpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_word_folder_dir_pure_video_mcpwe, VIDEO_EXTENSION = '.mkv')



# new var EXAMPLE
LIST_OUTPUT_AUDIO_SENTENCE_MCPSH_CHOPPED_NAMES = module_video_processing.generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio_mcpsh, AUDIO_EXTENSION = '.wav')

LIST_OUTPUT_AUDIO_SENTENCE_MCPSE_CHOPPED_NAMES = module_video_processing.generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio_mcpse, AUDIO_EXTENSION = '.wav')

LIST_OUTPUT_AUDIO_SENTENCE_ACPSH_CHOPPED_NAMES = module_video_processing.generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio_acpsh, AUDIO_EXTENSION = '.wav')

LIST_OUTPUT_AUDIO_SENTENCE_ACPSE_CHOPPED_NAMES = module_video_processing.generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio_acpse, AUDIO_EXTENSION = '.wav')


# new var EXAMPLE
LIST_OUTPUT_VIDEO_SENTENCE_MCPSH_CHOPPED_NAMES = module_video_processing.generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video_mcpsh, VIDEO_EXTENSION = '.mkv')


LIST_OUTPUT_VIDEO_SENTENCE_ACPSE_CHOPPED_NAMES = module_video_processing.generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video_acpse, VIDEO_EXTENSION = '.mkv')
 
LIST_OUTPUT_VIDEO_SENTENCE_ACPSH_CHOPPED_NAMES = module_video_processing.generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video_acpsh, VIDEO_EXTENSION = '.mkv')


LIST_OUTPUT_VIDEO_SENTENCE_MCPSE_CHOPPED_NAMES = module_video_processing.generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video_mcpse, VIDEO_EXTENSION = '.mkv')

    

#17
# extract the audio from the chopped samples and recreate new files which will contain only the audio and save them in the folders pure_audio
# for multiple files per word
module_video_processing.extract_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_WORD_CHUNK_SAMPLES_ACPWE_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_AUDIO_WORD_CHOPPED_ACPWE_NAMES, BIT_RATE = '192000')
module_video_processing.extract_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_WORD_CHUNK_SAMPLES_MCPWE_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_AUDIO_WORD_CHOPPED_MCPWE_NAMES, BIT_RATE = '192000')
# for multiple files per sentence
module_video_processing.extract_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSH_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_AUDIO_SENTENCE_MCPSH_CHOPPED_NAMES, BIT_RATE = '192000')
module_video_processing.extract_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSE_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_AUDIO_SENTENCE_MCPSE_CHOPPED_NAMES, BIT_RATE = '192000')
module_video_processing.extract_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSH_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_AUDIO_SENTENCE_ACPSH_CHOPPED_NAMES, BIT_RATE = '192000')
module_video_processing.extract_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSE_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_AUDIO_SENTENCE_ACPSE_CHOPPED_NAMES, BIT_RATE = '192000')






#18
# remove copy the chopped samples but withought the audio and save them pure_video folders

module_video_processing.remove_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_WORD_CHUNK_SAMPLES_ACPWE_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_WORD_CHOPPED_ACPWE_NAMES)
module_video_processing.remove_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_WORD_CHUNK_SAMPLES_MCPWE_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_WORD_CHOPPED_MCPWE_NAMES)
# for multiple files per sentence

module_video_processing.remove_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSH_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_MCPSH_CHOPPED_NAMES)

module_video_processing.remove_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSE_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_MCPSE_CHOPPED_NAMES)

module_video_processing.remove_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSH_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_ACPSH_CHOPPED_NAMES)

module_video_processing.remove_audio_from_list_mkv_files(INPUT_FILE_NAME = LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSE_FILE_NAMES, OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_ACPSE_CHOPPED_NAMES)



#19
# Apply face recognition and chopping for both. Fourcc M J P G is (FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G') one form of compression. An uncompressed video so that it saves each frame is RGBA, FOURCC1='R', FOURCC2='G', FOURCC3='B',FOURCC4 ='A' which is a loss less codec however that creates massive files

#0, for flipping the image around the x-axis (vertical flipping);
#> 0 for flipping around the y-axis (horizontal flipping);
#< 0 for flipping around both axe FLIP == True, FLIP_ARGUMENT =1

#example
#pure_video_cropped_word_chunk_samples_info = module_face_detection.multiple_file_camera_face_rec_and_cropping(LIST_OUTPUT_FILE_NAME = list_output_video_word_chopped_names, LIST_OF_INPUT_FILE_NAME = list_output_video_word_chopped_names, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', ADD_STR_CROPPED_FILE_NAME = '_cropped', INPUT_FILE_NAME_EXTENSION = '.mkv', OUPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 110, CROPPED_HEIGHT = 105, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 24,  ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = False, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = False, DISPLAY_CROPPED = False, FUTURE_KILL_SWITCH = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT = 1, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINTS = 68) 


pure_video_cropped_word_chunk_samples_info_acpwe = module_face_detection.multiple_file_camera_face_rec_and_cropping(LIST_OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_WORD_CHOPPED_ACPWE_NAMES, LIST_OF_INPUT_FILE_NAME = LIST_OUTPUT_VIDEO_WORD_CHOPPED_ACPWE_NAMES, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', ADD_STR_CROPPED_FILE_NAME = '_cropped', INPUT_FILE_NAME_EXTENSION = '.mkv', OUPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 110, CROPPED_HEIGHT = 105, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 24,  ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = False, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = False, DISPLAY_CROPPED = False, FUTURE_KILL_SWITCH = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT = 1, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINTS = 68) 


pure_video_cropped_word_chunk_samples_info_mcpwe = module_face_detection.multiple_file_camera_face_rec_and_cropping(LIST_OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_WORD_CHOPPED_MCPWE_NAMES, LIST_OF_INPUT_FILE_NAME = LIST_OUTPUT_VIDEO_WORD_CHOPPED_MCPWE_NAMES, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', ADD_STR_CROPPED_FILE_NAME = '_cropped', INPUT_FILE_NAME_EXTENSION = '.mkv', OUPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 110, CROPPED_HEIGHT = 105, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 24,  ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = False, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = False, DISPLAY_CROPPED = False, FUTURE_KILL_SWITCH = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT = 1, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINTS = 68) 


pure_video_cropped_sentence_chunk_samples_info_mcpsh = module_face_detection.multiple_file_camera_face_rec_and_cropping(LIST_OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_MCPSH_CHOPPED_NAMES, LIST_OF_INPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_MCPSH_CHOPPED_NAMES, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', ADD_STR_CROPPED_FILE_NAME = '_cropped', INPUT_FILE_NAME_EXTENSION = '.mkv', OUPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 110, CROPPED_HEIGHT = 105, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 24,  ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = False, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = False, DISPLAY_CROPPED = False, FUTURE_KILL_SWITCH = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT = 1, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINTS = 68) 

pure_video_cropped_sentence_chunk_samples_info_acpse = module_face_detection.multiple_file_camera_face_rec_and_cropping(LIST_OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_ACPSE_CHOPPED_NAMES, LIST_OF_INPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_ACPSE_CHOPPED_NAMES, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', ADD_STR_CROPPED_FILE_NAME = '_cropped', INPUT_FILE_NAME_EXTENSION = '.mkv', OUPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 110, CROPPED_HEIGHT = 105, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 24,  ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = False, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = False, DISPLAY_CROPPED = False, FUTURE_KILL_SWITCH = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT = 1, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINTS = 68) 


pure_video_cropped_sentence_chunk_samples_info_acpsh = module_face_detection.multiple_file_camera_face_rec_and_cropping(LIST_OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_ACPSH_CHOPPED_NAMES, LIST_OF_INPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_ACPSH_CHOPPED_NAMES, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', ADD_STR_CROPPED_FILE_NAME = '_cropped', INPUT_FILE_NAME_EXTENSION = '.mkv', OUPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 110, CROPPED_HEIGHT = 105, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 24,  ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = False, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = False, DISPLAY_CROPPED = False, FUTURE_KILL_SWITCH = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT = 1, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINTS = 68) 

pure_video_cropped_sentence_chunk_samples_info_mcpse = module_face_detection.multiple_file_camera_face_rec_and_cropping(LIST_OUTPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_MCPSE_CHOPPED_NAMES, LIST_OF_INPUT_FILE_NAME = LIST_OUTPUT_VIDEO_SENTENCE_MCPSE_CHOPPED_NAMES, FOURCC1='M', FOURCC2='J', FOURCC3='P',FOURCC4 ='G', ADD_STR_CROPPED_FILE_NAME = '_cropped', INPUT_FILE_NAME_EXTENSION = '.mkv', OUPUT_FILE_NAME_EXTENSION = '.avi', CROPPED_WIDTH = 110, CROPPED_HEIGHT = 105, SHIFT_RIGHT = -50, SHIFT_DOWN = 0, OUTPUT_FPS = 24,  ENABLE_FACE_RECOGNITION_TRACKING_CROPING = True, WHOLE_FACE_PROFILE = False, LIPS_PROFILE = False, LOAD_FACE_LANDMARKS = True, POINT_LAND_MARK_TRACKING = False, LAND_MARK_TRACKING_NUMBER = 1, LAND_MARK_LIP_TRACKING = True, CAPTURE_FACE_LANDMARKS = True, DISPLAY_FACE_LANDMARKS = False, SAVE_LANDMARK_TRACKING_RESULTS = False, SAVE_LANDMARK_TRACKING_RESULTS_NAME = 'Record', SAVE_WHOLE = False, SAVE_CROPPED = True, DISPLAY_WHOLE = False, DISPLAY_CROPPED = False, FUTURE_KILL_SWITCH = False, ENABLE_CUBIC_LAND_MARK_TRACKING = False, CUBIC_LAND_MARK_POINT_TOP = 34,CUBIC_LAND_MARK_POINT_LEFT = 49, CUBIC_LAND_MARK_POINT_BOTTOM = 9, CUBIC_LAND_MARK_POINT_RIGHT = 55, FLIP = True, FLIP_ARGUMENT = 1, SHAPE_PREDICTOR_NUMBER_OF_LANDMARK_POINTS = 68) 

# # other settings
# #sentence_chunk_samples_info = module_video_processing.chop_video_per_word_or_sentence(LIST_PER_WORD = acpsh, TIMES_PER_WORD = atpsh, MAX_TIME = max_time, FILE_NAME = INPUT_FILE_NAME,  CHOPPED_SAMPLE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir, SAVE_FILE_NAME = chopped_sample_per_sentence_folder_dir + '/sentence_chunk_samples_info.csv', SHIFT_RIGHT_OR_LEFT = 0, EXTEND_LEFT = -0, EXTEND_RIGHT = 0, EXTENSION = '.mkv', START_INDEX = 0, STOP_INDEX = 'END', SAVE = True)



'''
# example of how to load a json file
# import json
# # load jason file example
# filename = '/media/god/9c72f9bb-20f1-4b7b-8a9e-01f045898c0e/god/LEARNING/UniSheff/Mech/4/FYP/fyp-code/useful_bit/important_files/W/Moving_to_the_UK_to_study_Finnish_Girls_Experience_atpse.json'
# with open(filename, 'r') as f:
#         atpse = json.load(f)
'''


# pure video chunked and cropped
pure_video_cropped_word_chunk_samples_file_dir_acpwe = pure_video_cropped_word_chunk_samples_info_acpwe['LIST_CROPPED_VIDEO_FILENAME']
pure_video_cropped_word_chunk_samples_file_dir_mcpwe = pure_video_cropped_word_chunk_samples_info_mcpwe['LIST_CROPPED_VIDEO_FILENAME']
pure_video_cropped_sentence_chunk_samples_file_dir_acpse = pure_video_cropped_sentence_chunk_samples_info_acpse['LIST_CROPPED_VIDEO_FILENAME']
pure_video_cropped_sentence_chunk_samples_file_dir_acpsh = pure_video_cropped_sentence_chunk_samples_info_acpsh['LIST_CROPPED_VIDEO_FILENAME']
pure_video_cropped_sentence_chunk_samples_file_dir_mcpse = pure_video_cropped_sentence_chunk_samples_info_mcpse['LIST_CROPPED_VIDEO_FILENAME']
pure_video_cropped_sentence_chunk_samples_file_dir_mcpsh = pure_video_cropped_sentence_chunk_samples_info_mcpsh['LIST_CROPPED_VIDEO_FILENAME']



whole_files_name_dir = {'video_converted_to_mkv' : video_converted_to_mkv, 'video_converted_to_mkv_none_audio' : video_converted_to_mkv_none_audio, 'whole_pure_audio_file_name_dir' : whole_pure_audio_file_name_dir}

chopped_files_name_dir = {'LLIST_INPUT_WORD_CHUNK_SAMPLES_ACPWE_FILE_NAMES' : LLIST_INPUT_WORD_CHUNK_SAMPLES_ACPWE_FILE_NAMES
, 'LLIST_INPUT_WORD_CHUNK_SAMPLES_MCPWE_FILE_NAMES' : LLIST_INPUT_WORD_CHUNK_SAMPLES_MCPWE_FILE_NAMES, 'LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSH_FILE_NAMES' : LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSH_FILE_NAMES, 'LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSE_FILE_NAMES' : LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSE_FILE_NAMES, 'LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSH_FILE_NAMES' : LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSH_FILE_NAMES, 'LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSE_FILE_NAMES' : LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSE_FILE_NAMES}

chopped_pure_audio_files_name_dir = {'LIST_OUTPUT_AUDIO_WORD_CHOPPED_ACPWE_NAMES' : LIST_OUTPUT_AUDIO_WORD_CHOPPED_ACPWE_NAMES, 'LIST_OUTPUT_AUDIO_WORD_CHOPPED_MCPWE_NAMES' : LIST_OUTPUT_AUDIO_WORD_CHOPPED_MCPWE_NAMES, 'LIST_OUTPUT_AUDIO_SENTENCE_MCPSH_CHOPPED_NAMES' : LIST_OUTPUT_AUDIO_SENTENCE_MCPSH_CHOPPED_NAMES, 'LIST_OUTPUT_AUDIO_SENTENCE_MCPSE_CHOPPED_NAMES' : LIST_OUTPUT_AUDIO_SENTENCE_MCPSE_CHOPPED_NAMES, 'LIST_OUTPUT_AUDIO_SENTENCE_ACPSH_CHOPPED_NAMES' : LIST_OUTPUT_AUDIO_SENTENCE_ACPSH_CHOPPED_NAMES, 'LIST_OUTPUT_AUDIO_SENTENCE_ACPSE_CHOPPED_NAMES' : LIST_OUTPUT_AUDIO_SENTENCE_ACPSE_CHOPPED_NAMES}


chopped_pure_video_files_name_dir = {'LIST_OUTPUT_VIDEO_WORD_CHOPPED_ACPWE_NAMES' : LIST_OUTPUT_VIDEO_WORD_CHOPPED_ACPWE_NAMES
, 'LIST_OUTPUT_VIDEO_WORD_CHOPPED_MCPWE_NAMES' : LIST_OUTPUT_VIDEO_WORD_CHOPPED_MCPWE_NAMES, 'LIST_OUTPUT_VIDEO_SENTENCE_MCPSH_CHOPPED_NAMES' : LIST_OUTPUT_VIDEO_SENTENCE_MCPSH_CHOPPED_NAMES, 'LIST_OUTPUT_VIDEO_SENTENCE_MCPSE_CHOPPED_NAMES' : LIST_OUTPUT_VIDEO_SENTENCE_MCPSE_CHOPPED_NAMES, 'LIST_OUTPUT_VIDEO_SENTENCE_ACPSH_CHOPPED_NAMES' : LIST_OUTPUT_VIDEO_SENTENCE_ACPSH_CHOPPED_NAMES, 'LIST_OUTPUT_VIDEO_SENTENCE_ACPSE_CHOPPED_NAMES' : LIST_OUTPUT_VIDEO_SENTENCE_ACPSE_CHOPPED_NAMES}

chopped_cropped_pure_video_files_name_dir = {'pure_video_cropped_word_chunk_samples_file_dir_acpwe' : pure_video_cropped_word_chunk_samples_file_dir_acpwe
, 'pure_video_cropped_word_chunk_samples_file_dir_mcpwe' : pure_video_cropped_word_chunk_samples_file_dir_mcpwe, 'pure_video_cropped_sentence_chunk_samples_file_dir_mcpsh' : pure_video_cropped_sentence_chunk_samples_file_dir_mcpsh, 'pure_video_cropped_sentence_chunk_samples_file_dir_mcpse' : pure_video_cropped_sentence_chunk_samples_file_dir_mcpse, 'pure_video_cropped_sentence_chunk_samples_file_dir_acpsh' : pure_video_cropped_sentence_chunk_samples_file_dir_acpsh, 'pure_video_cropped_sentence_chunk_samples_file_dir_acpse' : pure_video_cropped_sentence_chunk_samples_file_dir_acpse}


dir_name_dictionary = {'whole_files_name_dir' : whole_files_name_dir, 'chopped_files_name_dir' : chopped_files_name_dir, 'chopped_pure_audio_files_name_dir' : chopped_pure_audio_files_name_dir, 'chopped_pure_video_files_name_dir' : chopped_pure_video_files_name_dir, 'chopped_cropped_pure_video_files_name_dir' : chopped_cropped_pure_video_files_name_dir}

variable_names_dataframe = pd.DataFrame(dir_name_dictionary) 


# list input video file names
list_chopped_cropped_pure_video_files_name =list(chopped_cropped_pure_video_files_name_dir.values())

# list input audio file names
list_chopped_pure_audio_files_name = list(chopped_pure_audio_files_name_dir.values())


#13
# use the fps value and the land mark points to map and hence create time signals for the change of each point in the x and y axis from 
cropped_chunk_info_list = [pure_video_cropped_word_chunk_samples_info_acpwe, pure_video_cropped_word_chunk_samples_info_mcpwe, pure_video_cropped_sentence_chunk_samples_info_acpse, pure_video_cropped_sentence_chunk_samples_info_acpsh, pure_video_cropped_sentence_chunk_samples_info_mcpse, pure_video_cropped_sentence_chunk_samples_info_mcpsh]


# add the time between frames in seconds. Thuse be able to create a time signal 
for i in range(len(cropped_chunk_info_list)):
    OUR_SAMPLE = cropped_chunk_info_list[i]
    FPS_LIST = OUR_SAMPLE.get('LIST_OF_INPUT_VIDEO_FPS')
    TIME_BETWEEN_FRAMES = []
    for k in range(len(FPS_LIST)):
        FPS_PER_SAMPLE = FPS_LIST[k]
        TIME_BETWEEN_FRAMES_PER_SAMPLE = float(1/FPS_PER_SAMPLE)
        TIME_BETWEEN_FRAMES.append(TIME_BETWEEN_FRAMES_PER_SAMPLE)
    OUR_SAMPLE['TIME_BETWEEN_FRAMES_IN_SECONDS'] = TIME_BETWEEN_FRAMES

cropped_chunk_info_dict = {'acpwe' : cropped_chunk_info_list[0], 'mcpwe': cropped_chunk_info_list[1], 'acpse':cropped_chunk_info_list[2], 'acpsh':cropped_chunk_info_list[3], 'mcpse':cropped_chunk_info_list[4], 'mcpsh':cropped_chunk_info_list[5]}


cropped_chunk_info_list = list(cropped_chunk_info_dict.values())

# if we would like to perform this on downloaded videos. Then 
FPS = 'TIME_BETWEEN_FRAMES_IN_SECONDS'
# if we would like to perform this on recorded videos. Then
#FPS = 'LIST_OF_MEASURED_FPS'

for i in range(len(cropped_chunk_info_list)):
    cropped_chunk_info_list_value = cropped_chunk_info_list[i]
    GET_LIST_OF_TIME_BETWEEN_FRAMES_IN_SECONDS = cropped_chunk_info_list_value.get(FPS)
    GET_LIST_OF_LAND_MARK_RESULTS = cropped_chunk_info_list_value.get('LIST_OF_LAND_MARK_RESULTS')
    for k in range(len(GET_LIST_OF_LAND_MARK_RESULTS)):
        TIME_BETWEEN_FRAMES_IN_SECONDS_VALUE = GET_LIST_OF_TIME_BETWEEN_FRAMES_IN_SECONDS[k]
        LANDMARK_DATAFRAME_VALUE = GET_LIST_OF_LAND_MARK_RESULTS[k]
        
        LANDMARK_DATAFRAME_array = LANDMARK_DATAFRAME_VALUE.get('X-Y Land Mark Coordinates')
        LENGTH_OF_LANDMARK_DATAFRAME_array = len(LANDMARK_DATAFRAME_array)
        LAND_MARK_TIME_LENGTH_ARRAY = [None]*LENGTH_OF_LANDMARK_DATAFRAME_array
        TIME_VALUE_IN_SECONDS = 0
        for z in range(LENGTH_OF_LANDMARK_DATAFRAME_array):
            LAND_MARK_TIME_LENGTH_ARRAY[z] = float(TIME_VALUE_IN_SECONDS)
            TIME_VALUE_IN_SECONDS = TIME_VALUE_IN_SECONDS + TIME_BETWEEN_FRAMES_IN_SECONDS_VALUE
        # Add the length values
        LANDMARK_DATAFRAME_VALUE['LAND_MARK_TIME_LENGTH_ARRAY'] = LAND_MARK_TIME_LENGTH_ARRAY
    
    
#pure_video_cropped_word_chunk_samples_info_acpwe.get('LIST_OF_INPUT_VIDEO_FPS')
    #cropped_chunk_info_list_value['Start Times'] = 
cropped_chunk_info_dict = {'acpwe' : cropped_chunk_info_list[0], 'mcpwe': cropped_chunk_info_list[1], 'acpse':cropped_chunk_info_list[2], 'acpsh':cropped_chunk_info_list[3], 'mcpse':cropped_chunk_info_list[4], 'mcpsh':cropped_chunk_info_list[5]}


# save results
# Note at the moment there is some information lost in the saved file as we a saving a dict variable which consists of multiple other lists and dataframes
module_save_variables.save_pandas_dict_results(VAR_INPUT = cropped_chunk_info_dict, FILE_NAME = FOLDER_PATH + '/cropped_chunks_info_dict', CSV=True, TXT=True)

# Future work Potentialy the user may descide to chop the whole video and delete all samples which fall bellow the stated threashold of LIST_RATIO_OF_DETECTED_FACES_PER_FRAME 

# Future work 12 add the functionality which automaticaly deletes any video which there isn't a face detected in less than 90% of the frames




# delet unecessary variables
del extend_left_acpse
del extend_left_acpsh
del extend_left_acpwe
del extend_left_mcpse
del extend_left_mcpsh
del extend_left_mcpwe
del extend_right_acpse
del extend_right_acpsh
del extend_right_acpwe
del extend_right_mcpse
del extend_right_mcpsh
del extend_right_mcpwe
del i
del k
del z
del shift_right_or_left_acpse
del shift_right_or_left_acpsh
del shift_right_or_left_acpwe
del shift_right_or_left_mcpse
del shift_right_or_left_mcpsh
del shift_right_or_left_mcpwe
del start_index_acpse
del start_index_acpsh
del start_index_acpwe
del start_index_mcpse
del start_index_mcpsh
del start_index_mcpwe
del stop_index_acpse
del stop_index_acpsh
del stop_index_acpwe
del stop_index_mcpse
del stop_index_mcpsh
del stop_index_mcpwe


### END ###

# In the future the it will be desired to clean a bit the code and apply allignment of between subtitles - audio and audio - video. 