
def maximum_time_of_vid(ATPSE, MTPSE, AUTO = True, MAN = False):
    '''
    ATPSE=atpse, MTPSE=mtpse, AUTO = True, MAN = False
    Parameters
    ----------
    ATPSE : List, optional
        DESCRIPTION. The default is atpse.
        atpse #auto_time_per_sentence_easy
    MTPSE : List, optional
        DESCRIPTION. The default is mtpse.
        mtpse #man_time_per_sentence_easy
    AUTO : List, optional
        DESCRIPTION. The default is True.
    MAN : List, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    max_time : Integer
        max legth of movie.

    '''
    
    # get the maximum time/length of the video
    if (AUTO == True and MAN == True):
        try:
            temp_var = ATPSE[len(ATPSE) - 1]
            max_time = temp_var[-12:]
            max_time = max_time.replace(':', '')#remove ':'
            max_time = max_time.replace('.', '')#remove ':'
            return max_time
        except:
            print('Please specify either ATUO or MAN as True and the other as False')
            return None
    elif (type(ATPSE) == type(None) and type(MTPSE) == type(None)):
        print('Either ATPSE/ATPSH or MTPSE/MTPSH must be != to Nonetype')
        return None
    elif (type(ATPSE) != type(None) and AUTO == True):
            temp_var = ATPSE[len(ATPSE) - 1]
            max_time = temp_var[-12:]
            max_time = max_time.replace(':', '')#remove ':'
            max_time = max_time.replace('.', '')#remove ':'
            return max_time
    elif (type(MTPSE) != type(None) and MAN == True):
            temp_var = MTPSE[len(MTPSE) - 1]
            max_time = temp_var[-12:]
            max_time = max_time.replace(':', '')#remove ':'
            max_time = max_time.replace('.', '')#remove ':'
            return max_time
    elif (AUTO != True and MAN != True):
        print('Please specify either AUTO or MAN as true')
        return None
        

    
    
def chop_video_per_word_or_sentence(LIST_PER_WORD, TIMES_PER_WORD, MAX_TIME, FILE_NAME, CHOPPED_SAMPLE_FOLDER_DIR, SAVE_FILE_NAME, SHIFT_RIGHT_OR_LEFT = 0, EXTEND_LEFT = -1000, EXTEND_RIGHT = 1000, EXTENSION = '.mkv', START_INDEX = 0, STOP_INDEX = 'END', SAVE = True):
    '''
    , CONCANTENATE = 2
    chop_video_per_word(LIST_PER_WORD = acpwe, TIMES_PER_WORD = atpwe, MAX_TIME = max_time, FILE_NAME = INPUT_FILE_NAME, CHOPPED_SAMPLE_FOLDER_DIR = chopped_sample_folder_dir, SHIFT_RIGHT_OR_LEFT = 0, EXTEND_LEFT = -1000, EXTEND_RIGHT = 1000, EXTENSION = '.mkv')
        
    # LIST_PER_WORD = acpwe or LIST_PER_WORD = mcpwe
    # TIMES_PER_WORD = atpwe or TIMES_PER_WORD = mtpwe 
    # MAX_TIME = max_time
    # apply shifting
    #SHIFT_RIGHT_OR_LEFT = 1000 # IN milliseconds accepts possitive and negative integers including 0 
    # apply extensions in the pre defined duration of each clip
    # EXTEND_LEFT = -1000, EXTEND_RIGHT = 1000 accept integer values
    # NOTE extension is in miliseconds and must be an integer, 500=0.5second
    # EXTENSION = '.mkv' # the extension of the input file name
    # FILE_NAME # string with the name of the file withought the extension
    #COMPLETE_FILE_NAME = '/media/god/9c72f9bb-20f1-4b7b-8a9e-01f045898c0e/god/LEARNING/UniSheff/Mech/4/FYP/fyp-code/useful_bit/important_files/k/Moving_to_the_UK_to_study_Finnish_Girls_Experience.mkv'    
    #CHOPPED_SAMPLE_FOLDER_DIR = '/media/god/9c72f9bb-20f1-4b7b-8a9e-01f045898c0e/god/LEARNING/UniSheff/Mech/4/FYP/fyp-code/useful_bit/important_files/choped_samples/'
    #CHOPPED_SAMPLE_FOLDER_DIR = #directory of the folder to store all the choppe samples
    #START_INDEX = 0# is the starting word to initialise cropping from the list LIST_PER_WORD
    #STOP_INDEX = 'END' # Sets the ending index, if the key word END is used the function continues until the end of the list. STOP_INDEX accepts an integer variable
    # concatenate # merges words and there for can produce more than a single word or sentence sample. IF CONCANTENATE =0 OR 1 NOTHING HAPPENS
    
    Parameters
    ----------
    LIST_PER_WORD : TYPE, optional
        DESCRIPTION. The default is acpwe.
    TIMES_PER_WORD : TYPE, optional
        DESCRIPTION. The default is atpwe.
    MAX_TIME : TYPE, optional
        DESCRIPTION. The default is max_time.
    SHIFT_RIGHT_OR_LEFT : TYPE, optional
        DESCRIPTION. The default is 0.
    EXTEND_LEFT : TYPE, optional
        DESCRIPTION. The default is -1000.
    EXTEND_RIGHT : TYPE, optional
        DESCRIPTION. The default is 1000.
    EXTENSION : TYPE, optional
        DESCRIPTION. The default is '.mkv'.
    FILE_NAME : TYPE, optional
        DESCRIPTION. The default is INPUT_FILE_NAME.
    CHOPPED_SAMPLE_FOLDER_DIR : TYPE, optional
        DESCRIPTION. The default is chopped_sample_folder_dir.

    Returns
    -------
    None.

    '''
    import pandas as pd
    import subprocess

    OVERALL_EXTEND_LEFT = EXTEND_LEFT + SHIFT_RIGHT_OR_LEFT
    OVERALL_EXTEND_RIGHT = EXTEND_RIGHT + SHIFT_RIGHT_OR_LEFT
    COMPLETE_FILE_NAME = FILE_NAME + EXTENSION    
    
    if STOP_INDEX == 'END':
        STOP_INDEX = len(TIMES_PER_WORD)
    else:
        pass
    
    if str(type(LIST_PER_WORD)) == 'Nonetype':
        print('Input list is empty')
        return None
    elif str(type(LIST_PER_WORD)) == 'Nonetype':
        print('Input list is empty')
        return None
    
    
   
    
    if type(LIST_PER_WORD) != type([]):
        print('Please assign a list to LIST_PER_WORD')
        return
    
    # identify the format of the subtitles.Per sentence they contain '-->' and both start and stop of the times in a single cell while other don't
    str_TIMES_PER_WORD = str(TIMES_PER_WORD[0])
    SKIP = False
    if str_TIMES_PER_WORD.find('-->') != -1:
        SKIP = True
    elif str_TIMES_PER_WORD.find('-->') == -1:
        SKIP = False
    else:
        print('something has gone wrong in function chop_video_per_word')
        return
    #for INDEX in range(len(TIMES_PER_WORD)):
        
    L_FILE_NAME = []
    L_START_TIME = []
    L_END_TIME = []
    L_WORD_CONT = []
    L_INDEX = []
    L_DURATION = []
    DURATION1 = 0
    DURATION2 = 0    
    for INDEX in range(START_INDEX,STOP_INDEX):
        
        
        if SKIP == False:
            INPUT_TIME = TIMES_PER_WORD[INDEX]
            FORMATED_INPUT_TIME = INPUT_TIME.replace('<','')
            FORMATED_INPUT_TIME = FORMATED_INPUT_TIME.replace('>','')        
            if INDEX == len(TIMES_PER_WORD)-1:
                break
            OUTPUT_TIME = TIMES_PER_WORD[INDEX+1]
            FORMATED_OUTPUT_TIME = OUTPUT_TIME.replace('<','')
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME.replace('>','')
        elif SKIP == True:
            INPUT_TIME = TIMES_PER_WORD[INDEX]
            FORMATED_INPUT_TIME = INPUT_TIME[0:12]
            OUTPUT_TIME = TIMES_PER_WORD[INDEX]
            FORMATED_OUTPUT_TIME = OUTPUT_TIME[17:]
            #if INDEX == len(TIMES_PER_WORD)-1:
            #    break
        else:
            print('something has gone wrong in function chop_video_per_word')
            return
            
        
        '''    
        # future option to add summ strings together acpwe[0] + ' ' + acpwe[1] Out[3]: 'hi guys'
        if CONCANTENATE <= 1:
            pass
        elif CONCANTENATE == 2:
            pass
        elif CONCANTENATE == 3:
            pass
        elif CONCANTENATE == 4:
            pass
        '''

        if INDEX == 0:# Avoid shifting on the first index
            # Extend only to the left    
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME.replace(':', '')#remove ':'
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME.replace('.', '')#remove '.'
            FORMATED_OUTPUT_TIME = int(FORMATED_OUTPUT_TIME)# CONVERT to intneger
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME + OVERALL_EXTEND_RIGHT
            DURATION2 = FORMATED_OUTPUT_TIME
            if FORMATED_OUTPUT_TIME >= int(MAX_TIME):
                FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME - OVERALL_EXTEND_RIGHT
                print('Start time of segment of index ' + str(INDEX) + ' resulted to a greater value due to shifting than the . For index' + str(INDEX) + ' shifting to the right was not applied')
            else:
                pass
            FORMATED_OUTPUT_TIME = str(FORMATED_OUTPUT_TIME)# CONVERT back to string
            while len(FORMATED_OUTPUT_TIME) != 9:
                FORMATED_OUTPUT_TIME = '0' + FORMATED_OUTPUT_TIME
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME[0:2] + ':' + FORMATED_OUTPUT_TIME[2:4] + ':' + FORMATED_OUTPUT_TIME[4:6] + '.' + FORMATED_OUTPUT_TIME[6::]# re assemble the string into the correct format by add the missing ':' and '.'        
        elif INDEX+1 == len(TIMES_PER_WORD)-1: # avoid shifting on the last index to the right
        
        # extend only to the right    
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME.replace(':', '')#remove ':'
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME.replace('.', '')#remove '.'
            FORMATED_OUTPUT_TIME = int(FORMATED_OUTPUT_TIME)# CONVERT to intneger
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME + OVERALL_EXTEND_RIGHT
            DURATION2 = FORMATED_OUTPUT_TIME
            if FORMATED_OUTPUT_TIME >= int(MAX_TIME):
                FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME - OVERALL_EXTEND_RIGHT
                print('Start time of segment of index ' + str(INDEX) + ' resulted to a greater value due to shifting than the . For index' + str(INDEX) + ' shifting to the right was not applied')
            else:
                pass
            FORMATED_OUTPUT_TIME = str(FORMATED_OUTPUT_TIME)# CONVERT back to string
            while len(FORMATED_OUTPUT_TIME) != 9:
                FORMATED_OUTPUT_TIME = '0' + FORMATED_OUTPUT_TIME
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME[0:2] + ':' + FORMATED_OUTPUT_TIME[2:4] + ':' + FORMATED_OUTPUT_TIME[4:6] + '.' + FORMATED_OUTPUT_TIME[6::]# re assemble the string into the correct format by add the missing ':' and '.'

        else:
            # apply extensions on both left and right
            # EXTEND TO THE LEFT
            FORMATED_INPUT_TIME = FORMATED_INPUT_TIME.replace(':', '')#remove ':'
            FORMATED_INPUT_TIME = FORMATED_INPUT_TIME.replace('.', '')#remove '.'
            FORMATED_INPUT_TIME = int(FORMATED_INPUT_TIME)# CONVERT to intneger
            FORMATED_INPUT_TIME = FORMATED_INPUT_TIME + OVERALL_EXTEND_LEFT
            DURATION1 = FORMATED_INPUT_TIME
            if FORMATED_INPUT_TIME < 0:
                FORMATED_INPUT_TIME = FORMATED_INPUT_TIME - OVERALL_EXTEND_LEFT
                print('Start time of segment of index ' + str(INDEX) + ' resulted to a negative value due to extension. For index' + str(INDEX) + ' shifting to the left was not applied')
            else:
                pass
            FORMATED_INPUT_TIME = str(FORMATED_INPUT_TIME)# CONVERT back to string
            while len(FORMATED_INPUT_TIME) != 9:
                FORMATED_INPUT_TIME = '0' + FORMATED_INPUT_TIME
            FORMATED_INPUT_TIME = FORMATED_INPUT_TIME[0:2] + ':' + FORMATED_INPUT_TIME[2:4] + ':' + FORMATED_INPUT_TIME[4:6] + '.' + FORMATED_INPUT_TIME[6::]# re assemble the string into the correct format by add the missing ':' and '.' 
            
            # EXTEND TO THE RIGHT
            
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME.replace(':', '')#remove ':'
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME.replace('.', '')#remove '.'
            FORMATED_OUTPUT_TIME = int(FORMATED_OUTPUT_TIME)# CONVERT to intneger
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME + OVERALL_EXTEND_RIGHT
            DURATION2 = FORMATED_OUTPUT_TIME
            if FORMATED_OUTPUT_TIME >= int(MAX_TIME):
                FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME - OVERALL_EXTEND_RIGHT
                print('Start time of segment of index ' + str(INDEX) + ' resulted to a greater value due to shifting than the . For index' + str(INDEX) + ' shifting to the right was not applied')
            else:
                pass
            FORMATED_OUTPUT_TIME = str(FORMATED_OUTPUT_TIME)# CONVERT back to string
            while len(FORMATED_OUTPUT_TIME) != 9:
                FORMATED_OUTPUT_TIME = '0' + FORMATED_OUTPUT_TIME
            FORMATED_OUTPUT_TIME = FORMATED_OUTPUT_TIME[0:2] + ':' + FORMATED_OUTPUT_TIME[2:4] + ':' + FORMATED_OUTPUT_TIME[4:6] + '.' + FORMATED_OUTPUT_TIME[6::]# re assemble the string into the correct format by add the missing ':' and '.'
            
        DURATION = DURATION2 - DURATION1
        DURATION =str(DURATION)
        
        while len(DURATION) != 9:
                DURATION = '0' + DURATION
        DURATION = DURATION[0:2] + ':' + DURATION[2:4] + ':' + DURATION[4:6] + '.' + DURATION[6::]# re assemble the string into the correct format by add the missing ':' and '.'
            
        WORD_OR_SENTENCE_IN_SEGMENT = LIST_PER_WORD[INDEX]
        #REPLACE SPACES WITH '-'
        WORD_OR_SENTENCE_IN_SEGMENT = WORD_OR_SENTENCE_IN_SEGMENT.replace(' ','-')   
        WORD_OR_SENTENCE_IN_SEGMENT = WORD_OR_SENTENCE_IN_SEGMENT.replace('\'','\\\'')
        FORMATED_INPUT_FILE_NAME = COMPLETE_FILE_NAME.replace(' ', '\ ')
        FORMATED_INPUT_FILE_NAME = COMPLETE_FILE_NAME.replace('\'','\\\'')
        FORMATED_OUTPUT_FILE_NAME = CHOPPED_SAMPLE_FOLDER_DIR + '/AUTO_SEGMNET_'+ str(WORD_OR_SENTENCE_IN_SEGMENT) + '_' + str(INDEX) + str(EXTENSION)
        #command = 'ffmpeg ' + '-hide_banner -loglevel panic' + ' -ss ' + str(FORMATED_INPUT_TIME) + ' -i ' + COMPLETE_FILE_NAME + ' -to ' + str(FORMATED_OUTPUT_TIME) + ' -c copy ' + FORMATED_OUTPUT_FILE_NAME
        #command = 'ffmpeg ' + '-hide_banner -loglevel panic'  ' -i ' + COMPLETE_FILE_NAME + ' -ss ' + str(FORMATED_INPUT_TIME) + ' -to ' + str(FORMATED_OUTPUT_TIME) + ' -c copy ' + FORMATED_OUTPUT_FILE_NAME
        command = 'ffmpeg ' + '-hide_banner -loglevel panic' + ' -i ' + FORMATED_INPUT_FILE_NAME + ' -ss ' + str(FORMATED_INPUT_TIME) + ' -to ' + str(FORMATED_OUTPUT_TIME) + ' -c:v ffv1 ' + FORMATED_OUTPUT_FILE_NAME  
        subprocess.call(command, shell=True)
        L_FILE_NAME.append(FORMATED_OUTPUT_FILE_NAME)
        L_START_TIME.append(str(FORMATED_INPUT_TIME))
        L_END_TIME.append(str(FORMATED_OUTPUT_TIME))
        L_WORD_CONT.append(str(WORD_OR_SENTENCE_IN_SEGMENT))
        L_INDEX.append(INDEX)
        L_DURATION.append(str(DURATION))
        print('Completed segment ' + str(INDEX) + ' out of ' + str(len(TIMES_PER_WORD)))
    
    # dictionary made out of lists 
    dict = {'File Name': L_FILE_NAME, 'Start Time (with extension)': L_START_TIME, 'End Time (with extension)': L_END_TIME, 'Duration (with extension)': L_DURATION ,'Word Content' : L_WORD_CONT, 'INDEX': L_INDEX} 
    	
    RESULT_RECORD = pd.DataFrame(dict)
    CSV_RESULT_RECORD = RESULT_RECORD
    #save option to be added for both sentence and word samples. Remember to add the SAVE = True OPTION and the SAVE_FILE_NAME OPTION (sentence_chunk_samples_info and word_chunk_samples_info)
    if SAVE == True:
        CSV_RESULT_RECORD.to_csv(SAVE_FILE_NAME, index = True, header=True)
    else:
        pass
    return RESULT_RECORD





def chopped_samples_file_names(CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO, SENTENCE_CHUNK_SAMPLES_FILE_NAMES, WORD_CHUNK_SAMPLES_FILE_NAMES, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR, AUDIO_EXTENSION = '.wav',VIDEO_EXTENSION = '.mkv'):
    '''
    This function is broken down into many other sub functions below and used

    Parameters
    ----------
    CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO : str
        DESCRIPTION.
    CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO : str
        DESCRIPTION.
    CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO : str
        DESCRIPTION.
    CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO : str
        DESCRIPTION.
    SENTENCE_CHUNK_SAMPLES_FILE_NAMES : dataframe
        DESCRIPTION.
    WORD_CHUNK_SAMPLES_FILE_NAMES : dataframe
        DESCRIPTION.
    CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR : str
        DESCRIPTION.
    CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR : str
        DESCRIPTION.
    AUDIO_EXTENSION : str, optional
        DESCRIPTION. The default is '.wav'.
    VIDEO_EXTENSION : str, optional
        DESCRIPTION. The default is '.mkv'.

    Returns
    -------
    LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES : list
        DESCRIPTION.
    LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES : list
        DESCRIPTION.
    LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES : list
        DESCRIPTION.
    LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES : list
        DESCRIPTION.
    LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES : list
        DESCRIPTION.
    LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES : list
        DESCRIPTION.

    


    '''
    import pandas as pd

    LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = []
    LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = []
    
    LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES = []
    LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES = []
    
    LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES = []
    LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES = [] 
    
    
    
    # input names lists .values.tolist()
    if WORD_CHUNK_SAMPLES_FILE_NAMES == None or WORD_CHUNK_SAMPLES_FILE_NAMES == []:
        LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = []
        LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES = []
        LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES = []
        pass
    else:
        LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = WORD_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
        LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
        for i in range(0, len(LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES)):
            # create the LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES
            temp_audio = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i] # get a sample file name from the list
            temp_audio = str(temp_audio)
            temp_audio = temp_audio.replace('[\'', '')
            temp_audio = temp_audio.replace('\']', '')
            temp_audio = temp_audio.replace('[\"', '')
            temp_audio = temp_audio.replace('\"]', '')
            temp_audio = temp_audio.replace('\\\\\'', '\\\'')
            temp_audio = temp_audio.replace(CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO)
            temp_audio = temp_audio.replace('.mkv', AUDIO_EXTENSION)
            LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES.append(temp_audio)
            # create the LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES
            temp_video = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i]
            temp_video = str(temp_video)
            temp_video = temp_video.replace('[\'', '')
            temp_video = temp_video.replace('\']', '')
            temp_video = temp_video.replace('[\"', '')
            temp_video = temp_video.replace('\"]', '')
            temp_video = temp_video.replace('\\\\\'', '\\\'')
            temp_video = temp_video.replace(CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO)
            temp_video = temp_video.replace('.mkv', VIDEO_EXTENSION)
            LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES.append(temp_video)
            #take care of the LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES
            temp_input_word = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i]
            temp_input_word = str(temp_input_word)
            temp_input_word = temp_input_word.replace('[\'', '')
            temp_input_word = temp_input_word.replace('\']', '')
            temp_input_word = temp_input_word.replace('[\"', '')
            temp_input_word = temp_input_word.replace('\"]', '')
            temp_input_word = temp_input_word.replace('\\\\\'', '\\\'')
            LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.append(temp_input_word)
    
    if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None or SENTENCE_CHUNK_SAMPLES_FILE_NAMES == []:
        LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = []
        LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES = []
        LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES = []
        pass
    else:
        LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = SENTENCE_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
        LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
        for i in range(0, len(LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES)):
            # create the LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES
            temp_audio = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i] # get a sample file name from the list
            temp_audio = str(temp_audio)
            temp_audio = temp_audio.replace('[\'', '')
            temp_audio = temp_audio.replace('\']', '')
            temp_audio = temp_audio.replace('[\"', '')
            temp_audio = temp_audio.replace('\"]', '')
            temp_audio = temp_audio.replace('\\\\\'', '\\\'')
            temp_audio = temp_audio.replace(CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO)
            temp_audio = temp_audio.replace('.mkv', AUDIO_EXTENSION)
            LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES.append(temp_audio)
            # create the LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES
            temp_video = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i]
            temp_video = str(temp_video)
            temp_video = temp_video.replace('[\'', '')
            temp_video = temp_video.replace('\']', '')
            temp_video = temp_video.replace('[\"', '')
            temp_video = temp_video.replace('\"]', '')
            temp_video = temp_video.replace('\\\\\'', '\\\'')
            temp_video = temp_video.replace(CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO)
            temp_video = temp_video.replace('.mkv', VIDEO_EXTENSION)
            LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES.append(temp_video)
            #take care of the LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES
            temp_input_sent = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i]
            temp_input_sent = str(temp_input_sent)
            temp_input_sent = temp_input_sent.replace('[\'', '')
            temp_input_sent = temp_input_sent.replace('\']', '')
            temp_input_sent = temp_input_sent.replace('[\"', '')
            temp_input_sent = temp_input_sent.replace('\"]', '')
            temp_input_sent = temp_input_sent.replace('\\\\\'', '\\\'')
            LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.append(temp_input_sent)
                
    
    return LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES, LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES, LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES, LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES, LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES, LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES









    # WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info
                # WORD_CHUNK_SAMPLES_INFO_ACPWE = word_chunk_samples_info_acpwe    
                # WORD_CHUNK_SAMPLES_INFO_MCPWE = word_chunk_samples_info_mcpwe

   # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir,
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_ACPWE = chopped_sample_per_word_folder_dir_acpwe
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_MCPWE = chopped_sample_per_word_folder_dir_mcpwe
    
    # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_word_folder_dir_pure_audio_acpwe
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO_ACPWE = chopped_sample_per_word_folder_dir_pure_audio_acpwe
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO_MCPWE = chopped_sample_per_word_folder_dir_pure_audio_mcpwe

    # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_word_folder_dir_pure_video_acpwe
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO_ACPWE = chopped_sample_per_word_folder_dir_pure_video_acpwe
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO_MCPWE = chopped_sample_per_word_folder_dir_pure_video_mcpwe
    
    # SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info,
                # SENTENCE_CHUNK_SAMPLES_INFO_MCPSH = sentence_chunk_samples_info_mcpsh
                # SENTENCE_CHUNK_SAMPLES_INFO_MCPSE = sentence_chunk_samples_info_mcpse
                # SENTENCE_CHUNK_SAMPLES_INFO_ACPSH = sentence_chunk_samples_info_acpsh
                # SENTENCE_CHUNK_SAMPLES_INFO_ACPSE = sentence_chunk_samples_info_acpse
    
    # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_MCPSH = chopped_sample_per_sentence_folder_dir_mcpsh
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_MCPSE = chopped_sample_per_sentence_folder_dir_mcpse
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_ACPSH = chopped_sample_per_sentence_folder_dir_acpsh
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_ACPSE = chopped_sample_per_sentence_folder_dir_acpse
    
    # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_MCPSH = chopped_sample_per_sentence_folder_dir_pure_audio_mcpsh
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_MCPSE = chopped_sample_per_sentence_folder_dir_pure_audio_mcpse
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_ACPSH = chopped_sample_per_sentence_folder_dir_pure_audio_acpsh
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_ACPSE = chopped_sample_per_sentence_folder_dir_pure_audio_mcpse 
                
    # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_MCPSH = chopped_sample_per_sentence_folder_dir_pure_video_mcpsh
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_MCPSE = chopped_sample_per_sentence_folder_dir_pure_video_mcpse
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_ACPSH = chopped_sample_per_sentence_folder_dir_pure_video_acpsh
                # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_ACPSE = chopped_sample_per_sentence_folder_dir_pure_video_acpse








# # INPUT DEPENDENCIES
# WORD_CHUNK_SAMPLES_FILE_NAMES
# # ouput 1
# LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES

# # INPUT DEPENDENCIES
# SENTENCE_CHUNK_SAMPLES_FILE_NAMES
# # ouput 2
# LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES

# # INPUT DEPENDENCIES
# WORD_CHUNK_SAMPLES_FILE_NAMES
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO
# AUDIO_EXTENSION
# # output 3
# LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES

# # INPUT DEPENDENCIES
# WORD_CHUNK_SAMPLES_FILE_NAMES
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO
# VIDEO_EXTENSION
# # output 4
# LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES

# # INPUT DEPENDENCIES
# SENTENCE_CHUNK_SAMPLES_FILE_NAMES
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO
# AUDIO_EXTENSION
# # output 5
# LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES

# # INPUT DEPENDENCIES
# SENTENCE_CHUNK_SAMPLES_FILE_NAMES
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO
# VIDEO_EXTENSION
# # output 6
# LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES





#######
# WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info
                # WORD_CHUNK_SAMPLES_INFO_ACPWE = word_chunk_samples_info_acpwe    
                # WORD_CHUNK_SAMPLES_INFO_MCPWE = word_chunk_samples_info_mcpwe
# old var EXAMPLE
# LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = generate_list_input_word_chunk_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info)

# # new var EXAMPLE
# LLIST_INPUT_WORD_CHUNK_SAMPLES_ACPWE_FILE_NAMES = generate_list_input_word_chunk_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_acpwe)

# LLIST_INPUT_WORD_CHUNK_SAMPLES_MCPWE_FILE_NAMES = generate_list_input_word_chunk_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_mcpwe)

def generate_list_input_word_chunk_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES):
    
    LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = []
  
#     if WORD_CHUNK_SAMPLES_FILE_NAMES == None:
# #    if WORD_CHUNK_SAMPLES_FILE_NAMES == None | WORD_CHUNK_SAMPLES_FILE_NAMES == []:
# #    if WORD_CHUNK_SAMPLES_FILE_NAMES == None or WORD_CHUNK_SAMPLES_FILE_NAMES == []:

#         LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = []
#     else:
#         LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = WORD_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
#         LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
#         for i in range(0, len(LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES)):
#             temp_input_word = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i]
#             temp_input_word = str(temp_input_word)
#             temp_input_word = temp_input_word.replace('[\'', '')
#             temp_input_word = temp_input_word.replace('\']', '')
#             temp_input_word = temp_input_word.replace('[\"', '')
#             temp_input_word = temp_input_word.replace('\"]', '')
#             temp_input_word = temp_input_word.replace('\\\\\'', '\\\'')
#             LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.append(temp_input_word)
          
    if str(type(WORD_CHUNK_SAMPLES_FILE_NAMES)) == "<class 'pandas.core.frame.DataFrame'>":
        LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = WORD_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
        LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
        for i in range(0, len(LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES)):
            temp_input_word = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i]
            temp_input_word = str(temp_input_word)
            temp_input_word = temp_input_word.replace('[\'', '')
            temp_input_word = temp_input_word.replace('\']', '')
            temp_input_word = temp_input_word.replace('[\"', '')
            temp_input_word = temp_input_word.replace('\"]', '')
            temp_input_word = temp_input_word.replace('\\\\\'', '\\\'')
            LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.append(temp_input_word)
    else:
        LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = []

            
    return LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES



# # INPUT DEPENDENCIES
# #WORD_CHUNK_SAMPLES_FILE_NAMES
# # ouput 1
# #LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES

#     LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = []

#     if WORD_CHUNK_SAMPLES_FILE_NAMES == None or WORD_CHUNK_SAMPLES_FILE_NAMES == []:
#         LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = []
#     else:
#         LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = WORD_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
#         LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
#         for i in range(0, len(LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES)):
#             temp_input_word = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i]
#             temp_input_word = str(temp_input_word)
#             temp_input_word = temp_input_word.replace('[\'', '')
#             temp_input_word = temp_input_word.replace('\']', '')
#             temp_input_word = temp_input_word.replace('[\"', '')
#             temp_input_word = temp_input_word.replace('\"]', '')
#             temp_input_word = temp_input_word.replace('\\\\\'', '\\\'')
#             LLIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.append(temp_input_word)


#######






##############

# SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info,
                # SENTENCE_CHUNK_SAMPLES_INFO_MCPSH = sentence_chunk_samples_info_mcpsh
                # SENTENCE_CHUNK_SAMPLES_INFO_MCPSE = sentence_chunk_samples_info_mcpse
                # SENTENCE_CHUNK_SAMPLES_INFO_ACPSH = sentence_chunk_samples_info_acpsh
                # SENTENCE_CHUNK_SAMPLES_INFO_ACPSE = sentence_chunk_samples_info_acpse


# # old var EXAMPLE
# LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info)

# # new var EXAMPLE
# LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSH_FILE_NAMES = generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpsh)

# LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_MCPSE_FILE_NAMES = generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpse)

# LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSH_FILE_NAMES = generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpsh)

# LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_ACPSE_FILE_NAMES = generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpse)




def generate_list_input_sentence_chunk_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES):
    LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = []
    
# #    if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None or SENTENCE_CHUNK_SAMPLES_FILE_NAMES == []:
# #    if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None | SENTENCE_CHUNK_SAMPLES_FILE_NAMES == []:
#     if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None:
#         LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = []

#         pass
#     else:
#         LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = SENTENCE_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
#         LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
#         for i in range(0, len(LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES)):
#             temp_input_sent = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i]
#             temp_input_sent = str(temp_input_sent)
#             temp_input_sent = temp_input_sent.replace('[\'', '')
#             temp_input_sent = temp_input_sent.replace('\']', '')
#             temp_input_sent = temp_input_sent.replace('[\"', '')
#             temp_input_sent = temp_input_sent.replace('\"]', '')
#             temp_input_sent = temp_input_sent.replace('\\\\\'', '\\\'')
#             LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.append(temp_input_sent)  
    
    if str(type(SENTENCE_CHUNK_SAMPLES_FILE_NAMES)) == "<class 'pandas.core.frame.DataFrame'>":
        
        LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = SENTENCE_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
        LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
        for i in range(0, len(LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES)):
            temp_input_sent = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i]
            temp_input_sent = str(temp_input_sent)
            temp_input_sent = temp_input_sent.replace('[\'', '')
            temp_input_sent = temp_input_sent.replace('\']', '')
            temp_input_sent = temp_input_sent.replace('[\"', '')
            temp_input_sent = temp_input_sent.replace('\"]', '')
            temp_input_sent = temp_input_sent.replace('\\\\\'', '\\\'')
            LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.append(temp_input_sent)  
    else:
        LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = []

    
    return LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES
        
        
        
# # INPUT DEPENDENCIES
# SENTENCE_CHUNK_SAMPLES_FILE_NAMES
# # ouput 2
# LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES

#     LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = []

#     if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None or SENTENCE_CHUNK_SAMPLES_FILE_NAMES == []:
#         LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = []

#         pass
#     else:
#         LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = SENTENCE_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
#         LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
#         for i in range(0, len(LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES)):
#             temp_input_sent = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i]
#             temp_input_sent = str(temp_input_sent)
#             temp_input_sent = temp_input_sent.replace('[\'', '')
#             temp_input_sent = temp_input_sent.replace('\']', '')
#             temp_input_sent = temp_input_sent.replace('[\"', '')
#             temp_input_sent = temp_input_sent.replace('\"]', '')
#             temp_input_sent = temp_input_sent.replace('\\\\\'', '\\\'')
#             LLIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.append(temp_input_sent)


####################





#####################

    # WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info
                # WORD_CHUNK_SAMPLES_INFO_ACPWE = word_chunk_samples_info_acpwe    
                # WORD_CHUNK_SAMPLES_INFO_MCPWE = word_chunk_samples_info_mcpwe


    # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir,
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_ACPWE = chopped_sample_per_word_folder_dir_acpwe
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_MCPWE = chopped_sample_per_word_folder_dir_mcpwe
      
    # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_word_folder_dir_pure_audio_acpwe
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO_ACPWE = chopped_sample_per_word_folder_dir_pure_audio_acpwe
                # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO_MCPWE = chopped_sample_per_word_folder_dir_pure_audio_mcpwe

# # INPUT DEPENDENCIES
# WORD_CHUNK_SAMPLES_FILE_NAMES
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO
# AUDIO_EXTENSION = '.wav'
# # output 3
# LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES



# # old var EXAMPLE
# LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES = generate_list_output_audio_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir_acpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_word_folder_dir_pure_audio_acpwe, AUDIO_EXTENSION = '.wav')

# # new var EXAMPLE
# LIST_OUTPUT_AUDIO_WORD_CHOPPED_ACPWE_NAMES = generate_list_output_audio_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_acpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir_acpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_word_folder_dir_pure_audio_acpwe, AUDIO_EXTENSION = '.wav')

# LIST_OUTPUT_AUDIO_WORD_CHOPPED_MCPWE_NAMES = generate_list_output_audio_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_mcpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir_mcpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_word_folder_dir_pure_audio_mcpwe, AUDIO_EXTENSION = '.wav')




def generate_list_output_audio_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO, AUDIO_EXTENSION = '.wav'):
    LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES = []
    
    # input names lists .values.tolist()
    # if WORD_CHUNK_SAMPLES_FILE_NAMES == None or WORD_CHUNK_SAMPLES_FILE_NAMES == []:
    # if WORD_CHUNK_SAMPLES_FILE_NAMES == None | WORD_CHUNK_SAMPLES_FILE_NAMES == []:
    # if WORD_CHUNK_SAMPLES_FILE_NAMES == None:
    #     LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES = []
    #     pass
    # else:
    #     LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = WORD_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
    #     LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
    #     for i in range(0, len(LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES)):
    #         # create the LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES
    #         temp_audio = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i] # get a sample file name from the list
    #         temp_audio = str(temp_audio)
    #         temp_audio = temp_audio.replace('[\'', '')
    #         temp_audio = temp_audio.replace('\']', '')
    #         temp_audio = temp_audio.replace('[\"', '')
    #         temp_audio = temp_audio.replace('\"]', '')
    #         temp_audio = temp_audio.replace('\\\\\'', '\\\'')
    #         temp_audio = temp_audio.replace(CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO)
    #         temp_audio = temp_audio.replace('.mkv', AUDIO_EXTENSION)
    #         LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES.append(temp_audio)
    
    if str(type(WORD_CHUNK_SAMPLES_FILE_NAMES)) == "<class 'pandas.core.frame.DataFrame'>":
        LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = WORD_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
        LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
        for i in range(0, len(LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES)):
            # create the LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES
            temp_audio = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i] # get a sample file name from the list
            temp_audio = str(temp_audio)
            temp_audio = temp_audio.replace('[\'', '')
            temp_audio = temp_audio.replace('\']', '')
            temp_audio = temp_audio.replace('[\"', '')
            temp_audio = temp_audio.replace('\"]', '')
            temp_audio = temp_audio.replace('\\\\\'', '\\\'')
            temp_audio = temp_audio.replace(CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO)
            temp_audio = temp_audio.replace('.mkv', AUDIO_EXTENSION)
            LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES.append(temp_audio)
    else:
        LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES = []

            
            
    
    return LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES



#     LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES = []

#     # input names lists .values.tolist()
#     if WORD_CHUNK_SAMPLES_FILE_NAMES == None or WORD_CHUNK_SAMPLES_FILE_NAMES == []:
#         LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES = []
#         pass
#     else:
#         LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = WORD_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
#         LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
#         for i in range(0, len(LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES)):
#             # create the LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES
#             temp_audio = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i] # get a sample file name from the list
#             temp_audio = str(temp_audio)
#             temp_audio = temp_audio.replace('[\'', '')
#             temp_audio = temp_audio.replace('\']', '')
#             temp_audio = temp_audio.replace('[\"', '')
#             temp_audio = temp_audio.replace('\"]', '')
#             temp_audio = temp_audio.replace('\\\\\'', '\\\'')
#             temp_audio = temp_audio.replace(CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO)
#             temp_audio = temp_audio.replace('.mkv', AUDIO_EXTENSION)
#             LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES.append(temp_audio)

####################




##################






# # INPUT DEPENDENCIES
# WORD_CHUNK_SAMPLES_FILE_NAMES
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO
# VIDEO_EXTENSION = '.mkv'
# # output 4
# LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES

# # WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info
                  # WORD_CHUNK_SAMPLES_INFO_ACPWE = word_chunk_samples_info_acpwe    
                  # WORD_CHUNK_SAMPLES_INFO_MCPWE = word_chunk_samples_info_mcpwe
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir,
                  # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_ACPWE = chopped_sample_per_word_folder_dir_acpwe
                  # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_MCPWE = chopped_sample_per_word_folder_dir_mcpwe
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_word_folder_dir_pure_video
                  # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO_ACPWE = chopped_sample_per_word_folder_dir_pure_video_acpwe
                  # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO_MCPWE = chopped_sample_per_word_folder_dir_pure_video_mcpwe


# # old var EXAMPLE
# LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES = generate_list_output_video_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info , CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_word_folder_dir_pure_video, VIDEO_EXTENSION = '.mkv')

# # new var EXAMPLE
# LIST_OUTPUT_VIDEO_WORD_CHOPPED_ACPWE_NAMES = generate_list_output_video_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_acpwe , CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir_acpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_word_folder_dir_pure_video_acpwe, VIDEO_EXTENSION = '.mkv')

# LIST_OUTPUT_VIDEO_WORD_CHOPPED_MCPWE_NAMES = generate_list_output_video_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info_acpwe , CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir_acpwe, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_word_folder_dir_pure_video_acpwe, VIDEO_EXTENSION = '.mkv')



def generate_list_output_video_word_chopped_samples_file_names(WORD_CHUNK_SAMPLES_FILE_NAMES, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO, VIDEO_EXTENSION = '.mkv'):

    LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES = []
    # if WORD_CHUNK_SAMPLES_FILE_NAMES == None or WORD_CHUNK_SAMPLES_FILE_NAMES == []:
    # if WORD_CHUNK_SAMPLES_FILE_NAMES == None | WORD_CHUNK_SAMPLES_FILE_NAMES == []:
    # if WORD_CHUNK_SAMPLES_FILE_NAMES == None:
    #     LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES = []
    #     pass
    # else:
    #     LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = WORD_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
    #     LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
    #     for i in range(0, len(LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES)):
    #         temp_video = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i]
    #         temp_video = str(temp_video)
    #         temp_video = temp_video.replace('[\'', '')
    #         temp_video = temp_video.replace('\']', '')
    #         temp_video = temp_video.replace('[\"', '')
    #         temp_video = temp_video.replace('\"]', '')
    #         temp_video = temp_video.replace('\\\\\'', '\\\'')
    #         temp_video = temp_video.replace(CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO)
    #         temp_video = temp_video.replace('.mkv', VIDEO_EXTENSION)
    #         LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES.append(temp_video)
  
    
    if str(type(WORD_CHUNK_SAMPLES_FILE_NAMES)) == "<class 'pandas.core.frame.DataFrame'>":
        LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = WORD_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
        LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
        for i in range(0, len(LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES)):
            temp_video = LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES[i]
            temp_video = str(temp_video)
            temp_video = temp_video.replace('[\'', '')
            temp_video = temp_video.replace('\']', '')
            temp_video = temp_video.replace('[\"', '')
            temp_video = temp_video.replace('\"]', '')
            temp_video = temp_video.replace('\\\\\'', '\\\'')
            temp_video = temp_video.replace(CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO)
            temp_video = temp_video.replace('.mkv', VIDEO_EXTENSION)
            LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES.append(temp_video)
    else:
        LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES = []
 
    return LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES

##################

###################

#     # SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info,
#                 # SENTENCE_CHUNK_SAMPLES_INFO_MCPSH = sentence_chunk_samples_info_mcpsh
#                 # SENTENCE_CHUNK_SAMPLES_INFO_MCPSE = sentence_chunk_samples_info_mcpse
#                 # SENTENCE_CHUNK_SAMPLES_INFO_ACPSH = sentence_chunk_samples_info_acpsh
#                 # SENTENCE_CHUNK_SAMPLES_INFO_ACPSE = sentence_chunk_samples_info_acpse
    

#     # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_MCPSH = chopped_sample_per_sentence_folder_dir_mcpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_MCPSE = chopped_sample_per_sentence_folder_dir_mcpse
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_ACPSH = chopped_sample_per_sentence_folder_dir_acpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_ACPSE = chopped_sample_per_sentence_folder_dir_acpse

#     # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_MCPSH = chopped_sample_per_sentence_folder_dir_pure_audio_mcpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_MCPSE = chopped_sample_per_sentence_folder_dir_pure_audio_mcpse
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_ACPSH = chopped_sample_per_sentence_folder_dir_pure_audio_acpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_ACPSE = chopped_sample_per_sentence_folder_dir_pure_audio_acpse 
                
# # INPUT DEPENDENCIES
# SENTENCE_CHUNK_SAMPLES_FILE_NAMES
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO
# AUDIO_EXTENSION
# # output 5

# # old var EXAMPLE
# LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES = generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio, AUDIO_EXTENSION = '.wav')

# # new var EXAMPLE
# LIST_OUTPUT_AUDIO_SENTENCE_MCPSH_CHOPPED_NAMES = generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio_mcpsh, AUDIO_EXTENSION = '.wav')

# LIST_OUTPUT_AUDIO_SENTENCE_MCPSE_CHOPPED_NAMES = generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio_mcpse, AUDIO_EXTENSION = '.wav')

# LIST_OUTPUT_AUDIO_SENTENCE_ACPSH_CHOPPED_NAMES = generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio_acpsh, AUDIO_EXTENSION = '.wav')

# LIST_OUTPUT_AUDIO_SENTENCE_ACPSE_CHOPPED_NAMES = generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio_acpse, AUDIO_EXTENSION = '.wav')



def generate_list_output_audio_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO, AUDIO_EXTENSION = '.wav'):


    LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES = []

    # # if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None or SENTENCE_CHUNK_SAMPLES_FILE_NAMES == []:
    # # if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None | SENTENCE_CHUNK_SAMPLES_FILE_NAMES == []:
    # if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None:
    #     LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES = []
    #     pass
    # else:
    #     LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = SENTENCE_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
    #     LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
    #     for i in range(0, len(LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES)):
    #         # create the LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES
    #         temp_audio = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i] # get a sample file name from the list
    #         temp_audio = str(temp_audio)
    #         temp_audio = temp_audio.replace('[\'', '')
    #         temp_audio = temp_audio.replace('\']', '')
    #         temp_audio = temp_audio.replace('[\"', '')
    #         temp_audio = temp_audio.replace('\"]', '')
    #         temp_audio = temp_audio.replace('\\\\\'', '\\\'')
    #         temp_audio = temp_audio.replace(CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO)
    #         temp_audio = temp_audio.replace('.mkv', AUDIO_EXTENSION)
    #         LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES.append(temp_audio)
            
            
    if str(type(SENTENCE_CHUNK_SAMPLES_FILE_NAMES)) == "<class 'pandas.core.frame.DataFrame'>":
        LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = SENTENCE_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
        LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
        for i in range(0, len(LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES)):
            # create the LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES
            temp_audio = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i] # get a sample file name from the list
            temp_audio = str(temp_audio)
            temp_audio = temp_audio.replace('[\'', '')
            temp_audio = temp_audio.replace('\']', '')
            temp_audio = temp_audio.replace('[\"', '')
            temp_audio = temp_audio.replace('\"]', '')
            temp_audio = temp_audio.replace('\\\\\'', '\\\'')
            temp_audio = temp_audio.replace(CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO)
            temp_audio = temp_audio.replace('.mkv', AUDIO_EXTENSION)
            LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES.append(temp_audio)
    else:
        LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES = []

    return LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES

######################

######################


# # INPUT DEPENDENCIES
# SENTENCE_CHUNK_SAMPLES_FILE_NAMES
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO
# VIDEO_EXTENSION
# # output 6
# LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES
   


# #     # SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info,
#                 # SENTENCE_CHUNK_SAMPLES_INFO_MCPSH = sentence_chunk_samples_info_mcpsh
#                 # SENTENCE_CHUNK_SAMPLES_INFO_MCPSE = sentence_chunk_samples_info_mcpse
#                 # SENTENCE_CHUNK_SAMPLES_INFO_ACPSH = sentence_chunk_samples_info_acpsh
#                 # SENTENCE_CHUNK_SAMPLES_INFO_ACPSE = sentence_chunk_samples_info_acpse
    

#     # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_MCPSH = chopped_sample_per_sentence_folder_dir_mcpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_MCPSE = chopped_sample_per_sentence_folder_dir_mcpse
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_ACPSH = chopped_sample_per_sentence_folder_dir_acpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_ACPSE = chopped_sample_per_sentence_folder_dir_acpse
    
#     # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_MCPSH = chopped_sample_per_sentence_folder_dir_pure_video_mcpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_MCPSE = chopped_sample_per_sentence_folder_dir_pure_video_mcpse
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_ACPSH = chopped_sample_per_sentence_folder_dir_pure_video_acpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_ACPSE = chopped_sample_per_sentence_folder_dir_pure_video_acpse
      
# old var EXAMPLE

# LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES = generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video, VIDEO_EXTENSION = '.mkv')

# # new var EXAMPLE
# LIST_OUTPUT_VIDEO_SENTENCE_MCPSH_CHOPPED_NAMES = generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video_mcpsh, VIDEO_EXTENSION = '.mkv')


# LIST_OUTPUT_VIDEO_SENTENCE_ACPSE_CHOPPED_NAMES = generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video_acpse, VIDEO_EXTENSION = '.mkv')
 
# LIST_OUTPUT_VIDEO_SENTENCE_ACPSH_CHOPPED_NAMES = generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_acpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_acpsh, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video_acpsh, VIDEO_EXTENSION = '.mkv')


# LIST_OUTPUT_VIDEO_SENTENCE_MCPSE_CHOPPED_NAMES = generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info_mcpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir_mcpse, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video_mcpse, VIDEO_EXTENSION = '.mkv')


def generate_list_output_video_sentence_chopped_samples_file_names(SENTENCE_CHUNK_SAMPLES_FILE_NAMES, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO, VIDEO_EXTENSION = '.mkv'):

    LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES = [] 
    
    # # if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None or SENTENCE_CHUNK_SAMPLES_FILE_NAMES == []:
    # # if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None | SENTENCE_CHUNK_SAMPLES_FILE_NAMES == []:
    # if SENTENCE_CHUNK_SAMPLES_FILE_NAMES == None:
    #     LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES = []
    #     pass
    # else:
    #     LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = SENTENCE_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
    #     LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
    #     for i in range(0, len(LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES)):
    #         temp_video = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i]
    #         temp_video = str(temp_video)
    #         temp_video = temp_video.replace('[\'', '')
    #         temp_video = temp_video.replace('\']', '')
    #         temp_video = temp_video.replace('[\"', '')
    #         temp_video = temp_video.replace('\"]', '')
    #         temp_video = temp_video.replace('\\\\\'', '\\\'')
    #         temp_video = temp_video.replace(CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO)
    #         temp_video = temp_video.replace('.mkv', VIDEO_EXTENSION)
    #         LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES.append(temp_video)
    
    if str(type(SENTENCE_CHUNK_SAMPLES_FILE_NAMES)) == "<class 'pandas.core.frame.DataFrame'>":
        LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = SENTENCE_CHUNK_SAMPLES_FILE_NAMES[['File Name']]
        LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES.values.tolist()
        for i in range(0, len(LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES)):
            temp_video = LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES[i]
            temp_video = str(temp_video)
            temp_video = temp_video.replace('[\'', '')
            temp_video = temp_video.replace('\']', '')
            temp_video = temp_video.replace('[\"', '')
            temp_video = temp_video.replace('\"]', '')
            temp_video = temp_video.replace('\\\\\'', '\\\'')
            temp_video = temp_video.replace(CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR, CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO)
            temp_video = temp_video.replace('.mkv', VIDEO_EXTENSION)
            LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES.append(temp_video)
    else:
        LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES = []

    
    
    return LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES





####################################










































   
    
#    # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR = chopped_sample_per_word_folder_dir,
#                 # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_ACPWE = chopped_sample_per_word_folder_dir_acpwe
#                 # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_MCPWE = chopped_sample_per_word_folder_dir_mcpwe
    
#     # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_word_folder_dir_pure_audio
#                 # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO_ACPWE = chopped_sample_per_word_folder_dir_pure_audio_acpwe
#                 # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO_MCPWE = chopped_sample_per_word_folder_dir_pure_audio_mcpwe

#     # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_word_folder_dir_pure_video_acpwe
#                 # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO_ACPWE = chopped_sample_per_word_folder_dir_pure_video_acpwe
#                 # CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO_MCPWE = chopped_sample_per_word_folder_dir_pure_video_mcpwe
    
#     # SENTENCE_CHUNK_SAMPLES_FILE_NAMES = sentence_chunk_samples_info,
#                 # SENTENCE_CHUNK_SAMPLES_INFO_MCPSH = sentence_chunk_samples_info_mcpsh
#                 # SENTENCE_CHUNK_SAMPLES_INFO_MCPSE = sentence_chunk_samples_info_mcpse
#                 # SENTENCE_CHUNK_SAMPLES_INFO_ACPSH = sentence_chunk_samples_info_acpsh
#                 # SENTENCE_CHUNK_SAMPLES_INFO_ACPSE = sentence_chunk_samples_info_acpse
    
#     # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR = chopped_sample_per_sentence_folder_dir
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_MCPSH = chopped_sample_per_sentence_folder_dir_mcpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_MCPSE = chopped_sample_per_sentence_folder_dir_mcpse
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_ACPSH = chopped_sample_per_sentence_folder_dir_acpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_ACPSE = chopped_sample_per_sentence_folder_dir_acpse
    
#     # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO = chopped_sample_per_sentence_folder_dir_pure_audio
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_MCPSH = chopped_sample_per_sentence_folder_dir_pure_audio_mcpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_MCPSE = chopped_sample_per_sentence_folder_dir_pure_audio_mcpse
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_ACPSH = chopped_sample_per_sentence_folder_dir_pure_audio_acpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO_ACPSE = chopped_sample_per_sentence_folder_dir_pure_audio_mcpse 
                
#     # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO = chopped_sample_per_sentence_folder_dir_pure_video
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_MCPSH = chopped_sample_per_sentence_folder_dir_pure_video_mcpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_MCPSE = chopped_sample_per_sentence_folder_dir_pure_video_mcpse
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_ACPSH = chopped_sample_per_sentence_folder_dir_pure_video_acpsh
#                 # CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO_ACPSE = chopped_sample_per_sentence_folder_dir_pure_video_acpse
      
      # WORD_CHUNK_SAMPLES_FILE_NAMES = word_chunk_samples_info
                  # WORD_CHUNK_SAMPLES_INFO_ACPWE = word_chunk_samples_info_acpwe    
                  # WORD_CHUNK_SAMPLES_INFO_MCPWE = word_chunk_samples_info_mcpwe


# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_AUDIO, 
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR_PURE_VIDEO, 
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_AUDIO,
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR_PURE_VIDEO,

# SENTENCE_CHUNK_SAMPLES_FILE_NAMES,
# CHOPPED_SAMPLE_PER_WORD_FOLDER_DIR, 
# CHOPPED_SAMPLE_PER_SENTENCE_FOLDER_DIR




def extract_audio_from_list_mkv_files(INPUT_FILE_NAME, OUTPUT_FILE_NAME, BIT_RATE = '192000'):
    '''
    Additional info https://gist.github.com/protrolium/e0dbd4bb0f1a396fcb55
    
    # convert from mp4 to mkv format
    ffmpeg -i video.mp4 -f mp3 -ab 192000 -vn music.mp3

    The -i option in the above command is simple: it is the path to the input file. The second option -f mp3 tells ffmpeg that the ouput is in mp3 format. The third option i.e -ab 192000 tells ffmpeg that we want the output to be encoded at 192Kbps and -vn tells ffmpeg that we dont want video. The last param is the name of the output file.
    

    Parameters
    ----------
    INPUT_FILE_NAME : str
        Could be these variables LIST_INPUT_WORD_CHUNK_SAMPLES_FILE_NAMES, LIST_INPUT_SENTENCE_CHUNK_SAMPLES_FILE_NAMES,.
    OUTPUT_FILE_NAME : str
        Could be these varaibles LIST_OUTPUT_AUDIO_WORD_CHOPPED_NAMES, LIST_OUTPUT_VIDEO_WORD_CHOPPED_NAMES, LIST_OUTPUT_AUDIO_SENTENCE_CHOPPED_NAMES, LIST_OUTPUT_VIDEO_SENTENCE_CHOPPED_NAMES.
    BIT_RATE : str, optional
        DESCRIPTION. The default is '192000'.

    Returns
    -------
    None.

    '''
    import subprocess
    
    for i in range(0, len(INPUT_FILE_NAME)):
        try:
            # if the same file name exists replace it
            command = 'rm ' + OUTPUT_FILE_NAME[i] + ' >/dev/null 2>&1'
            subprocess.call(command, shell=True)
            command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ INPUT_FILE_NAME[i] + ' -f wav -ab ' + BIT_RATE+ ' -vn ' + OUTPUT_FILE_NAME[i]
            subprocess.call(command, shell=True)
        except:
            command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ INPUT_FILE_NAME[i] + ' -f wav -ab ' + BIT_RATE+ ' -vn ' + OUTPUT_FILE_NAME[i]
            subprocess.call(command, shell=True)
                
    return None







def extract_audio_from_single_mkv_files(INPUT_FILE_NAME, OUTPUT_FILE_NAME, BIT_RATE = '192000'):
    '''
    

    Parameters
    ----------
    INPUT_FILE_NAME : str
        DESCRIPTION.
    OUTPUT_FILE_NAME : str
        DESCRIPTION.
    BIT_RATE : str, optional
        DESCRIPTION. The default is '192000'.

    Returns
    -------
    None.

    '''
    import subprocess
    # if the same file name exists replace it
    try:
        command = 'rm ' + OUTPUT_FILE_NAME + ' >/dev/null 2>&1'
        subprocess.call(command, shell=True)
        command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ INPUT_FILE_NAME + ' -f wav -ab ' + BIT_RATE+ ' -vn ' +OUTPUT_FILE_NAME
        subprocess.call(command, shell=True)
    except:
        command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ INPUT_FILE_NAME + ' -f wav -ab ' + BIT_RATE+ ' -vn ' +OUTPUT_FILE_NAME
        subprocess.call(command, shell=True)

    return None








def convert_from_mp4_to_mkv(FILE_NAME, INPUT_EXTENSION='.mp4', OUTPUT_EXTENSION = '.mkv'):
    '''
    
    # convert from mp4 to mkv format
    #ffmpeg -i input.mp4 -vcodec copy -acodec copy output.mkv
    #ffmpeg -i Moving_to_the_UK_to_study_Finnish_Girls_Experience_none_audio_.mp4 -vcodec copy -acodec copy output3.mkv
    
    Parameters
    ----------
    FILE_NAME : string
        The file name of the video to convert from mp4 to .mkv.
    INPUT_EXTENSION : string, optional
        DESCRIPTION. The default is '.mkv'.

    Returns
    -------
    None.

    '''
    import subprocess
    FORMATED_INPUT_FILE_NAME = FILE_NAME.replace(' ', '\ ') + str(INPUT_EXTENSION)
    FORMATED_OUTPUT_FILE_NAME = FILE_NAME.replace(' ', '\ ') + str(OUTPUT_EXTENSION)
    # if the same file name exists replace it
    try:
        command = 'rm ' + FORMATED_OUTPUT_FILE_NAME + ' >/dev/null 2>&1'
        subprocess.call(command, shell=True)
        command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ FORMATED_INPUT_FILE_NAME + ' -vcodec copy -acodec copy ' +FORMATED_OUTPUT_FILE_NAME
        subprocess.call(command, shell=True)
    except:
        command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ FORMATED_INPUT_FILE_NAME + ' -vcodec copy -acodec copy ' +FORMATED_OUTPUT_FILE_NAME
        subprocess.call(command, shell=True)

    return FORMATED_OUTPUT_FILE_NAME


def remove_audio_from_file_mp4(FILE_NAME, EXTENSION='.mp4'):
    ''' 
    THis command removes the audio of a video in the directory which ends with a .mp4 extension and renames it as 
    # mov, mp4, m4a, 3gp, 3g2, mj2,
    Example of the command run in the terminal ffmpeg -hide_banner -loglevel panic -i FILE_NAME_TO_REMOVE_AUDIO.mp4  -c copy -an _OUTPUT_FILE_NAME.mp4

    '''

    import subprocess
    #subtitle_formats=subprocess.run(['youtube-dl', '--list-sub', URL], capture_output=True)
    # AND AN ESCAPE CHARACTER BEFOR EVERY SPACE
    FORMATED_FILE_NAME = FILE_NAME.replace(' ', '\ ') + str(EXTENSION)
    FORMATED_OUTPUT_FILE_NAME = FILE_NAME.replace(' ', '\ ') + '_none_audio' + str(EXTENSION) 
    
    # if the same file name exists replace it
    try:
        command = 'rm ' + FORMATED_OUTPUT_FILE_NAME + ' >/dev/null 2>&1'
        print('Warning file with the name ' + FORMATED_OUTPUT_FILE_NAME + ' already existed so it was deleted and will be replaced with another of identical name')
        subprocess.call(command, shell=True)
        command = 'ffmpeg'+ ' -hide_banner -loglevel panic' + ' -i ' + FORMATED_FILE_NAME + ' -c copy -an ' + FORMATED_OUTPUT_FILE_NAME 
        subprocess.call(command, shell=True)
    except:
        command = 'ffmpeg' + ' -hide_banner -loglevel panic' + ' -i ' + FORMATED_FILE_NAME + ' -c copy -an ' + FORMATED_OUTPUT_FILE_NAME 
        subprocess.call(command, shell=True)

    return None




def remove_audio_from_mkv_file(INPUT_FILE_NAME, OUTPUT_FILE_NAME):
    '''
    Useful info
    https://stackoverflow.com/questions/38161697/how-to-remove-one-track-from-video-file-using-ffmpeg
    
    Remove a specific audio stream
    
    ffmpeg -i input -map 0 -map -0:a:2 -c copy output
    
        -map 0 selects all streams from the input.
        -map -0:a:2 then deselects audio stream 3. The stream index starts counting from 0, so audio stream 10 would be 0:a:9.
    
    Remove all audio streams
    
    ffmpeg -i input -map 0 -map -0:a -c copy output
    
        -map 0 selects all streams from the input.
        -map -0:a then deselects all audio streams from the input.
    
    Removing other stream types
    
    If you want to remove other stream types you can use the appropriate stream specifier.

        v - video, such as -map -0:v
        a - audio, such as -map -0:a (as shown above)
        s - subtitles, such as -map -0:s
        d - data, such as -map -0:d

    Parameters
    ----------
    INPUT_FILE_NAME : str
        DESCRIPTION.
    OUTPUT_FILE_NAME : str
        DESCRIPTION.
   

    Returns
    -------
    None.

    '''
    import subprocess
    # if the same file name exists replace it
    try:
        command = 'rm ' + OUTPUT_FILE_NAME + ' >/dev/null 2>&1'
        subprocess.call(command, shell=True)
        command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ INPUT_FILE_NAME + ' -map 0 -map -0:a -c copy ' + OUTPUT_FILE_NAME
        subprocess.call(command, shell=True)
    except:
        command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ INPUT_FILE_NAME + ' -map 0 -map -0:a -c copy ' + OUTPUT_FILE_NAME
        subprocess.call(command, shell=True)
        
    return None





def  remove_audio_from_list_mkv_files(INPUT_FILE_NAME, OUTPUT_FILE_NAME):
    '''
    

    Parameters
    ----------
    INPUT_FILE_NAME : list
        Can only accept variables list_input_word_chunk_samples_file_names, list_input_sentence_chunk_samples_file_names.
    OUTPUT_FILE_NAME : list
        Can only accept variables list_output_audio_word_chopped_names, list_output_video_word_chopped_names, list_output_audio_sentence_chopped_names, list_output_video_sentence_chopped_names.

    Returns
    -------
    None.

    '''
    import subprocess
    
    for i in range(0, len(INPUT_FILE_NAME)):
        try:
            # if the same file name exists replace it
            command = 'rm ' + OUTPUT_FILE_NAME[i] + ' >/dev/null 2>&1'
            subprocess.call(command, shell=True)
            command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ INPUT_FILE_NAME[i] + ' -map 0 -map -0:a -c copy ' + OUTPUT_FILE_NAME[i]
            subprocess.call(command, shell=True)
        except:
            command = 'ffmpeg ' + ' -hide_banner -loglevel panic ' + '-i '+ INPUT_FILE_NAME[i] + ' -map 0 -map -0:a -c copy ' + OUTPUT_FILE_NAME[i]
            subprocess.call(command, shell=True)
                
    return None






'''
def remove_audio_from_multiple_mp4(DIRECTORY,EXTENSION='.mp4'):
    ''' 
    # for multiple files
    #module_video_processing.remove_audio_from_multiple_mp4(DIRECTORY='cyprus\ video',EXTENSION='.mp4')
    #THis command removes the audio form all the files in the directory which end with .mp4
    # mov, mp4, m4a, 3gp, 3g2, mj2,
'''

    import subprocess
    #subtitle_formats=subprocess.run(['youtube-dl', '--list-sub', URL], capture_output=True)
    
    command = 'for file in ' + str(DIRECTORY) + '/*' + str(EXTENSION) + ' ; do ffmpeg -i "$file" -c copy -an "noaudio_$file"; done'
    subprocess.call(command, shell=True)
    
    return None

'''




def list_merge_avi_and_wav(IINPUT_VIDEO_FILE_NAME, IINPUT_AUDIO_FILE_NAME, OOUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME):

    import subprocess
    LLIST_FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME =[]

    if (len(IINPUT_VIDEO_FILE_NAME) != len(IINPUT_AUDIO_FILE_NAME) or len(IINPUT_VIDEO_FILE_NAME) != len(OOUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME) or len(IINPUT_AUDIO_FILE_NAME) != len(OOUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME)):
        print('The IINPUT_VIDEO_FILE_NAME, IINPUT_AUDIO_FILE_NAME and OOUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME lists must be of the same length')
        return LLIST_FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME
    else:
        pass
    
    if (IINPUT_VIDEO_FILE_NAME == [] or IINPUT_VIDEO_FILE_NAME == None):
        print('IINPUT_VIDEO_FILE_NAME = [] or None')
        return LLIST_FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME
    
    elif (IINPUT_AUDIO_FILE_NAME == [] or IINPUT_AUDIO_FILE_NAME == None):
        print('IINPUT_AUDIO_FILE_NAME = [] or None')
        return LLIST_FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME
    
    elif (OOUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME == [] or OOUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME == None):
        print('OOUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME = [] or None')
        return LLIST_FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME
    
    else:
        pass
    
    LLIST_FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME =[]
    for i in range(0, len(IINPUT_VIDEO_FILE_NAME)):
        FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME = merge_avi_and_wav(INPUT_VIDEO_FILE_NAME = IINPUT_VIDEO_FILE_NAME[i], INPUT_AUDIO_FILE_NAME = IINPUT_AUDIO_FILE_NAME[i], OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME = OOUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME[i])
        LLIST_FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME.append(FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME)
    
    return LLIST_FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME





def merge_avi_and_wav(INPUT_VIDEO_FILE_NAME, INPUT_AUDIO_FILE_NAME, OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME):
    '''
    https://superuser.com/questions/277642/how-to-merge-audio-and-video-file-in-ffmpeg
    
    Merging video and audio, with audio re-encoding
    
    See this example, taken from this blog entry but updated for newer syntax. It should be something to the effect of:
    
    ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
    
    Here, we assume that the video file does not contain any audio stream yet, and that you want to have the same output format (here, MP4) as the input format.
    
    The above command transcodes the audio, since MP4s cannot carry PCM audio streams. You can use any other desired audio codec if you want. See the FFmpeg Wiki: AAC Encoding Guide for more info.
    
    If your audio or video stream is longer, you can add the -shortest option so that ffmpeg will stop encoding once one file ends.
    Copying the audio without re-encoding
    
    If your output container can handle (almost) any codec – like MKV – then you can simply copy both audio and video streams:
    
    ffmpeg -i video.mp4 -i audio.wav -c copy output.mkv
    
    Replacing audio stream
    
    If your input video already contains audio, and you want to replace it, you need to tell ffmpeg which audio stream to take:
    
    ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4
    
    The -map option makes ffmpeg only use the first video stream from the first input and the first audio stream from the second input for the output file.


    '''
    import subprocess
    
    #FORMATED_INPUT_VIDEO_FILE_NAME = INPUT_VIDEO_FILE_NAME.replace(' ', '\ ')
    #FROMATED_INPUT_AUDIO_FILE_NAME = INPUT_AUDIO_FILE_NAME.replace(' ', '\ ') 
    #FORMATED_OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME = OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME.replace(' ', '\ ')
    
    try:
        command = 'rm ' + OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME + ' >/dev/null 2>&1'
        subprocess.call(command, shell=True)    
        command = 'ffmpeg  -hide_banner -loglevel panic ' + '-i ' + INPUT_VIDEO_FILE_NAME + ' -i ' +  INPUT_AUDIO_FILE_NAME + ' -c copy ' +  OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME
        subprocess.call(command, shell=True)
    except:
        command = 'ffmpeg  -hide_banner -loglevel panic ' + '-i ' + INPUT_VIDEO_FILE_NAME + ' -i ' +  INPUT_AUDIO_FILE_NAME + ' -c copy ' +  OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME
        subprocess.call(command, shell=True)
    print('Saved file ' + OUTPUT_COMBINED_AUDIO_AND_VIDEO_FILE_NAME)
    return None
