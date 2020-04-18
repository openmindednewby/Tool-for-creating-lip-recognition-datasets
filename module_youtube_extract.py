def sub_type(MAN_SUB, AUTO_SUB, MAN_SUB_EXIST, AUTO_SUB_EXIST):
    '''
    The following function is used to determine weather or not the subtitles have assigned timings per word or per sentence.
    
    MAN_SUB ----> manual subtitles variable
    AUTO_SUB----> automaticaly generated subtitles variable
    MAN_SUB_EXIST ---> output of previous comand
    AUTO_SUB_EXIST ---> outpur of precious command
    
    
    man_sub_easy_type, auto_sub_easy_type
    
     if string_subtitle_formats.find('align:start position:0%') != -1: # not found
        automatic_subtitles_exist= False
        print('Warning the current video does not contain automaticaly generated subtitles')
    else:
        automatic_subtitles_exist= True
        pass
    
    '''
    
    # check if manual subtitles exist
    if MAN_SUB_EXIST== True:
        # check man sub type exists
        STR_MAN_SUB = str(MAN_SUB)
        if STR_MAN_SUB.find('align:start position:0%') != -1:
            MAN_SUB_EASY_TYPE = True
            print('The time frames in ' + 'MAN_SUB' + ' are per word, hence aligment is not needed.')
        elif STR_MAN_SUB.find('align:start position:0%') == -1:
            MAN_SUB_EASY_TYPE = False
            print('The time frames in ' + 'MAN_SUB' + ' are per centence, hence aligment is needed.')
        else:
            pass
        
    elif MAN_SUB_EXIST == False:
            MAN_SUB_EASY_TYPE = None
    else:
        pass
        
    # check if automatic subtitles exist
    if AUTO_SUB_EXIST == True:
        # check man sub type exists
        STR_AUTO_SUB = str(AUTO_SUB)
        if STR_AUTO_SUB.find('align:start position:0%') != -1:
            AUTO_SUB_EASY_TYPE = True
            print('The time frames in ' + 'AUTO_SUB' + ' are per word, hence aligment is not needed.')
        elif STR_AUTO_SUB.find('align:start position:0%') == -1:
            AUTO_SUB_EASY_TYPE = False
            print('The time frames in ' + 'AUTO_SUB' + ' are per centence, hence aligment is needed.')
        else:
            pass
        
    elif AUTO_SUB_EXIST == False:
            AUTO_SUB_EASY_TYPE = None
    else:
        pass

    return MAN_SUB_EASY_TYPE, AUTO_SUB_EASY_TYPE
        
    








def list_available_subtitles(URL, FILE_NAME, TXT_CLEAN=True, TXT=True, JSON=True):
    ''' 
    The follwoing fuction lists all available formats
    
    Things to note:
        vtt ---> contains both the subtitles and the timings they are presented in the video. Depending on wheather or not they are automaticaly or manualy added the timing could be per word or for a number of words.
        ttml ---> contains only the subtitles text and can be opened with a browser
        srv3 ---> contains only the subtitles text and can be opened with a browser
        srv2 ---> same as srv3 but some characters cannot be interpret properly such as  &#39 insted of '
        srv1 ---> same as srv3 but some characters cannot be interpret properly such as  &#39 insted of '
        
        Note: Unfortunately it has been obsereved in some cases such as the following video 'https://www.youtube.com/watch?v=YHCZt8LeQzI&fbclid=IwAR2e436VcxEBWWnnz48W2vPU4iTfFpxgglA9U7uIOFP1XCA1sdp4h_qnmLI^C' in which both manualy added and automaticaly generated subtitles excist youtube-dl bug preventing us from downloading the automaticaly generated subtitles.
    '''
    import subprocess
    import json

    subtitle_formats=subprocess.run(['youtube-dl', '--list-sub', URL], capture_output=True)
    string_subtitle_formats = str(subtitle_formats)
    # clean output
       
    # define file names
    COMPLETE_FILE_NAME=FILE_NAME+'_available_sub'+'.txt'
    COMPLETE_FILE_NAME_CLEAN=FILE_NAME+'_available_sub'+'_clean'+'.txt'
    COMPLETE_FILE_NAME_JSON=FILE_NAME+'_available_sub'+'.json'
    if TXT==True:
        f = open(COMPLETE_FILE_NAME, 'w')
        f.write(string_subtitle_formats)
        f.close()
        print('List of available subtitles saved as ', COMPLETE_FILE_NAME)
    else:
        pass
    
    if JSON==True:
        json = json.dumps(string_subtitle_formats)
        f = open(COMPLETE_FILE_NAME_JSON, 'w')
        f.write(json)
        f.close()
        print('List of available subtitles saved as ', COMPLETE_FILE_NAME_JSON)
    else:
        pass    
    
    if TXT_CLEAN==True:
        string_subtitle_formats=string_subtitle_formats.replace('\\n', '\n')
        f = open(COMPLETE_FILE_NAME_CLEAN, 'w')
        f.write(string_subtitle_formats)
        f.close()
        print('List of available subtitles saved as ', COMPLETE_FILE_NAME_CLEAN)
    else:
        pass
    
    
    #check to see if manual subtitles are found
    if string_subtitle_formats.find('has no subtitles') != -1: # the find command prints -1 if the result is not found. if it is found it prints the first index value
        manual_subtitles_exist= False
        print('Warning the current video does not contain manual subtitles posted by the owner')
    else:
        manual_subtitles_exist = True
        pass

    # check to see in automatic subtitles excist
    if string_subtitle_formats.find('has no automatic captions') != -1: # not found
        automatic_subtitles_exist= False
        print('Warning the current video does not contain automaticaly generated subtitles')
    else:
        automatic_subtitles_exist= True
        pass

    return string_subtitle_formats, manual_subtitles_exist, automatic_subtitles_exist









# download audio visual subtitles
def down_audio_video(URL, VIDEO_QUALITY_CODE, AUDIO_QUALITY_CODE, MERGE=False, FILE_NAME='%(title)s.f%(format_id)s.%(ext)s'):
    '''
    
    The following function us used to download the audio and video from youtube.
    
    AUDIO_QUALITY_CODE and VIDEO_QUALITY_CODE---> code should be found and selected from the output of function 'list_available_AV_formats'
    MERGE----> Specifies if we would like to merge the output or keep the audio and video as separate files.  
    FILE_NAMES ---> We can specify any name we would like to the files (the extension will be different and thuse  we will still be able to distinguish the files). We could also name them with the same name as the owner of the youtubue video using the specified format '%(title)s.f%(format_id)s.%(ext)s'
    
    '''
    import subprocess
# very useful resource 
#https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection
#https://www.ostechnix.com/youtube-dl-tutorial-with-examples-for-beginners/ 
    # https://askubuntu.com/questions/486297/how-to-select-video-quality-from-youtube-dl/1097056#1097056
    # youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 https://youtu.be/FWGC9SqA3J0
    #
    if MERGE==True:
        print('Download initiated')
        AV_QUALITY_CODES=str(VIDEO_QUALITY_CODE)+'+'+str(AUDIO_QUALITY_CODE)
        subprocess.run(['youtube-dl', '-f', AV_QUALITY_CODES, '-o', FILE_NAME+'.%(ext)s', URL], capture_output=True)
        print('Download completed')
        print('File saved as',FILE_NAME)
        return None
    elif MERGE==False:
        print('Download initiated')
        # if the extension is not added simply one file overwrites the other and you end up with a single file
        # In addition it seems that the the video format contains audio as well
        #AV_QUALITY_CODES=str(VIDEO_QUALITY_CODE)+','+str(AUDIO_QUALITY_CODE)
        #subprocess.run(['youtube-dl', '-f', AV_QUALITY_CODES, '-o', FILE_NAME+'.%(ext)s', URL], capture_output=True)    
        subprocess.run(['youtube-dl', '-f', str(VIDEO_QUALITY_CODE), '-o', FILE_NAME+'.%(ext)s', URL], capture_output=True)
        subprocess.run(['youtube-dl', '-f', str(AUDIO_QUALITY_CODE), '-o', FILE_NAME+'.%(ext)s', URL], capture_output=True)
        print('Download completed')
        print('Files saved as',FILE_NAME)
        return None
    else:
        pass


        

# Download subtitles posted by video owners and automaticaly generated subtitles
def down_sub(URL, FILE_NAME='SUBTITLES', TYPE='vtt', LANGUAGE='en', MAN_SUB=True, AUTO_SUB=True, SAVE=False):
    
    '''
    This funtion downloads the subtitles of the URL provided. The list of supported websites are listed here:https://ytdl-org.github.io/youtube-dl/supportedsites.html
    The function outputs both manual and automatic subtitles to the specified format. Not it is required that only one of the parameters 'VTT=True, TTML=False, SRV3=False, SRV2=False, SRV1=False' is set to True 
    MAN_SUB --> specifies if we would like to download the subtitles posted by the owner
    AUTO_SUB ---> specifies if we would like to download the automaticaly generated subtitles of youtube
    FILE_NAME ---> just the file name to store the subtitles. DO NOT ADD A EXTENSION TO THE NAME
    DEL_FILE ---> this delets the file which is created in the process of downlading the subtitles as the youtube-dl command doesn't naturaly output a result insted it saves in a text file
    LANGUAGE ---> can be specified from the results of the list of available files, for english we use 'en'
    The extansion the subtitles are saved is .en.vtt which is text readable format and can  be opened with the open funtion and the .en.vtt extension
    TYPE---> accepts one of the following assuming it excists. see the out put of the list of available subbtitle formats function.
    'vtt'  ---> contains both subtitles and the time they are been shown in the video
    'ttml' ---> contains only the subtitles text and can be opened with a browser
    'srv3' ---> contains only the subtitles text and can be opened with a browser
    'srv2' ---> same as srv3 but some characters cannot be interpret properly such as  &#39 insted of '
    'srv1' ---> same as srv3 but some characters cannot be interpret properly such as  &#39 insted of '
    
    -------------------


youtube-dl --write-auto-sub -o '%(autonumber)s.%(ext)s' --sub-format 'vtt'  --sub-lang=en  --skip-download https://www.youtube.com/watch?v=YHCZt8LeQzI&fbclid=IwAR2e436VcxEBWWnnz48W2vPU4iTfFpxgglA9U7uIOFP1XCA1sdp4h_qnmLI^C

youtube-dl --write-auto-sub -o '%(autonumber)s.%(ext)s' --sub-format 'ttml'  --sub-lang=en  --skip-download https://www.youtube.com/watch?v=YHCZt8LeQzI&fbclid=IwAR2e436VcxEBWWnnz48W2vPU4iTfFpxgglA9U7uIOFP1XCA1sdp4h_qnmLI^C


%(title)s.f%(format_id)s.%(autonumber)s._available_sub_.%(ext)s

MAN_SUB==True and AUTO_SUB==False and VTT=True and TTML=False and SRV3=False and SRV2=False and SRV1=False and MAN_SUB=True and AUTO_SUB=True

-------------------
    
    '''
    import subprocess
    import os
    
    #create file names
    FILE_NAME_AUTO=FILE_NAME+'_auto_sub'
    COMPLETE_FILE_NAME_AUTO=FILE_NAME_AUTO + '.' + LANGUAGE + '.' + TYPE

    FILE_NAME_MAN=FILE_NAME+'_man_sub'
    COMPLETE_FILE_NAME_MAN=FILE_NAME_MAN + '.' + LANGUAGE + '.' + TYPE
    
    # download manual subtitles
    if MAN_SUB == True:
        subprocess.run(['youtube-dl', '--write-sub', '--sub-lang', 'en', '--sub-format', TYPE, '--skip-download','-o', FILE_NAME_MAN, URL], capture_output=True)
        with open(COMPLETE_FILE_NAME_MAN, "r") as manual_sub: # as the function automaticaly stores the result into a file and does not return anything we need to read the file created and load it to the memory
            manual_sub_content = manual_sub.read()
        print('Manual subtitles downloaded')
        string_manual_sub_content = str(manual_sub_content)
    else:
        string_manual_sub_content = False
        pass
    
    # download auto subtitles
    if AUTO_SUB == True:
        subprocess.run(['youtube-dl', '--write-auto-sub', '--sub-lang', 'en', '--sub-format', TYPE, '--skip-download','-o', FILE_NAME_AUTO, URL], capture_output=True)
        with open(COMPLETE_FILE_NAME_AUTO, "r") as auto_sub: # as the function automaticaly stores the result into a file and does not return anything we need to read the file created and load it to the memory
            auto_sub_content = auto_sub.read()
        print('Auto subtitles downloaded')
        string_auto_sub_content = str(auto_sub_content)
    else:
        string_auto_sub_content = False
        pass
    
    
    if SAVE==False:
        try:
            os.remove(COMPLETE_FILE_NAME_MAN)
            print('File ' + COMPLETE_FILE_NAME_MAN + ' removed.')
        except:
            pass
        try:
            os.remove(COMPLETE_FILE_NAME_AUTO)
            print('File ' + COMPLETE_FILE_NAME_AUTO + ' removed.')
        except:
            pass
    else:
        pass
    
    return string_manual_sub_content, string_auto_sub_content
    

  


'''
# one method to capture output from the terminal
output = subprocess.Popen( './list_all_formats.sh', stdout=subprocess.PIPE ).communicate()[0]
'''
#This function lists all available audio and video formats for download.
def list_available_AV_formats(URL, CLEAN=True, LIST=True, SAVE=False, FILE_NAME='list_all_formats'):
    '''
    This function extracts all the formating information about the URL video
    substitude the URL with the video URL you would like to download
    Clean  removes unecessary  text fromt the format infomration
    LIST produces a list with each format in a row insted of a str obj
    SAVE=True saves your file with in a text file with the specified FILE_NAME
    '''
    import subprocess
    
    # executes command and captures the output 
    list_all_formats=subprocess.run(['youtube-dl', '--list-formats', URL], capture_output=True)
    
    #creates a str variable of all available formats
    string_list_all_formats = str(list_all_formats)
        
        
    # returns un cleaned info
    if (CLEAN == False and SAVE== False and LIST==False):      
        print('Available formats have been extracted from the URL:', URL)
        return string_list_all_formats

    # returns un cleaned info and saves to filename
    if (CLEAN == False and SAVE== True and LIST==False):  
        # saves the output of the command
        f = open(FILE_NAME + '.txt', 'w')
        f.write(string_list_all_formats)
        f.close()
        print('File with all available AV formats for the URL:', URL, 'have been saved in', FILE_NAME)
        return string_list_all_formats
                
    
    # returns clean format
    if (CLEAN == True and SAVE== False and LIST==False):      
        
        # Finds the position in which the usful information origintes
        index_of_useful_info=string_list_all_formats.find('format code  extension  resolution note') + len('format code  extension  resolution note')
        
        # creates a new var with only that info
        useful_info_available_formats=string_list_all_formats[index_of_useful_info:]
        
        # Clean info and rename
        simple_useful_info_available_formats=useful_info_available_formats.replace('\'' ,' ')
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace(' , stderr=b  )', ' ')
        
        # Clean info so that each line contains a single AV format
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace('\\n', '\n')
        
        # remove additional white space from the ends
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()
        
        return simple_useful_info_available_formats
    
    # returns clean format and saves to file as well
    if (CLEAN == True and SAVE== True and LIST==False):      
        
        # Finds the position in which the usful information origintes
        index_of_useful_info=string_list_all_formats.find('format code  extension  resolution note') + len('format code  extension  resolution note')
        
        # creates a new var with only that info
        useful_info_available_formats=string_list_all_formats[index_of_useful_info:]
        
        # Clean info and rename
        simple_useful_info_available_formats=useful_info_available_formats.replace('\'' ,' ')
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace(' , stderr=b  )', ' ')
        
        # Clean info so that each line contains a single AV format
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace('\\n', '\n')
        
        # remove additional white space from the ends
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()
        
        # saves the output of the command
        f = open(FILE_NAME + '.txt', 'w')
        f.write(simple_useful_info_available_formats)
        f.close()
        return simple_useful_info_available_formats
    
    # returns clean format as a list
    if (CLEAN == True and SAVE== False and LIST==True):      
        
        # Finds the position in which the usful information origintes
        index_of_useful_info=string_list_all_formats.find('format code  extension  resolution note') + len('format code  extension  resolution note')
        
        # creates a new var with only that info
        useful_info_available_formats=string_list_all_formats[index_of_useful_info:]
        
        # Clean info and rename
        simple_useful_info_available_formats=useful_info_available_formats.replace('\'' ,' ')
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace(' , stderr=b  )', ' ')
        
        # remove additional white space from the ends
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()        
    
        # creates a list and assigns each audio or video format to its dedicated slot
        list_useful=simple_useful_info_available_formats.rsplit('\\n')
        
        # Removes empty elements. Note: should have removed all '' in the list however the one towards the end remains :/
        list_useful= list(filter(('').__ne__, list_useful))    
        return list_useful
        
        
        # returns clean format as a list and saves to a file
    if (CLEAN == True and SAVE== True and LIST==True):      
        
        # Finds the position in which the usful information origintes
        index_of_useful_info=string_list_all_formats.find('format code  extension  resolution note') + len('format code  extension  resolution note')
        
        # creates a new var with only that info
        useful_info_available_formats=string_list_all_formats[index_of_useful_info:]
        
        # Clean info and rename
        simple_useful_info_available_formats=useful_info_available_formats.replace('\'' ,' ')
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace(' , stderr=b  )', ' ')
        
        # remove additional white space from the ends
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()
    
        # creates a list and assigns each audio or video format to its dedicated slot
        list_useful=simple_useful_info_available_formats.rsplit('\\n')
        
        # Removes empty elements. Note: should have removed all '' in the list however the one towards the end remains :/
        list_useful= list(filter(('').__ne__, list_useful))   
        
        # Clean info so that each line contains a single AV format. This will only be used for the saved file
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace('\\n', '\n')
        
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()

        
        
        # saves the output of the command
        f = open(FILE_NAME + '.txt', 'w')
        f.write(simple_useful_info_available_formats)
        f.close()
        return list_useful



# META DATA
def meta_data(URL,  FILE_NAME='', TXT_CLEAN=True, TXT=True, JSON=True,DOWNLOAD=False):
    ''' 
    This function extracts the meta data of a youtube video and saves it into a file
    URL of the format URL = 'https://www.youtube.com/watch?v=YHCZt8LeQzI&fbclid=IwAR2e436VcxEBWWnnz48W2vPU4iTfFpxgglA9U7uIOFP1XCA1sdp4h_qnmLI'
    DOWNLOAD =  either True or False. we will use a different functio to download content in which we could also specify the format we woul like
    FILE_NAME ---> Do not include the extension of the fle, in case both TXT_CLEAN and TXT = True the '_clean_format' is added at the en of the file name
    
    
    Notes   print('upload date : %s' %(meta['upload_date']))
            print('uploader    : %s' %(meta['uploader']))
            print('views       : %d' %(meta['view_count']))

            meta.items
            meta.keys
            meta.
    
    '''
    
#    from __future__ import unicode_literals
    import __future__
    import youtube_dl
    import json
    ydl_opts = {}

    
    # gets the meta data of the video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(URL, download=DOWNLOAD) 

    meta_keys=list(meta.keys())
    meta_values=list(meta.values())

    COMPLETE_FILE_NAME = FILE_NAME + '_meta_data'+'.txt'
    COMPLETE_FILE_NAME_CLEAN = FILE_NAME + '_meta_data'+'_clean'+'.txt'
    COMPLETE_FILE_NAME_JSON = FILE_NAME + '_meta_data'+'.json'

    if TXT==True:    # save into text file
        f = open(COMPLETE_FILE_NAME, 'w')
        f.write( str(meta) )
        f.close()
    else:
        pass
        
    if TXT_CLEAN==True:    # save into text file with nice format and adds _clean_format.txt at the end.
        with open(COMPLETE_FILE_NAME_CLEAN, 'w') as f:
            for i in range(len(meta_keys)):
                f.write(str(meta_keys[i]) + ':' + str(meta_values[i]) + '\n')
    else:
        pass

    if  JSON==True:    #save into a json file
        json = json.dumps(meta)
        f = open(COMPLETE_FILE_NAME_JSON, 'w')
        f.write(json)
        f.close()
    else:
        pass
        

    return meta
    
