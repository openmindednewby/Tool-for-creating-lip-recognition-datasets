# Function to remove r replacespecial characters from subtitles
def remove_or_replace_special_char(INPUT_SUB_LIST, CHAR_TO_REPLACE = 'all', CHAR_TO_REPLACE_WITH = ''):
    '''
    

    Parameters
    ----------
    INPUT_SUB_LIST : list
        DESCRIPTION.
    CHAR_TO_REPLACE : str, optional
        DESCRIPTION. The default is 'all'. If 'all is specified then all special characters are removed. The special characters are '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    CHAR_TO_REPLACE_WITH : str, optional
        DESCRIPTION. The default is ''.

    Returns
    -------
    OUTPUT_SUB_LIST : TYPE
        DESCRIPTION.

    '''
    import string
    OUTPUT_SUB_LIST = INPUT_SUB_LIST
    
    if (OUTPUT_SUB_LIST == None or OUTPUT_SUB_LIST == [] ):
        return OUTPUT_SUB_LIST
    else:
        pass
    
    if CHAR_TO_REPLACE == 'all':
        special_characters_str = string.punctuation 
        special_characters_list = list(special_characters_str)
        # FOR EVERY ELEMENT IN special_characters_list
        for i in range(0, len(special_characters_list)):
            CHAR_TO_REMOVE = str(special_characters_list[i])
            # FOR EVERY ELEMENT IN INPUT_SUB_LIST
            for z in range(0, len(INPUT_SUB_LIST)):
                ELEMENT_TO_REPLACE_CHAR = str(INPUT_SUB_LIST[z])
                REPLACED_ELEMENT = ELEMENT_TO_REPLACE_CHAR.replace(CHAR_TO_REMOVE, str(CHAR_TO_REPLACE_WITH)) 
                OUTPUT_SUB_LIST[z] = REPLACED_ELEMENT
            
    else:
        # FOR EVERY ELEMENT IN INPUT_SUB_LIST
        CHAR_TO_REMOVE = str(CHAR_TO_REPLACE)
        for k in range(0, len(INPUT_SUB_LIST)):
            ELEMENT_TO_REPLACE_CHAR = str(INPUT_SUB_LIST[k])
            REPLACED_ELEMENT = ELEMENT_TO_REPLACE_CHAR.replace(CHAR_TO_REPLACE, str(CHAR_TO_REPLACE_WITH))
            OUTPUT_SUB_LIST[k] = REPLACED_ELEMENT
            
    return OUTPUT_SUB_LIST





# FUNTION TO PROCESS EASY FORMAT
def filter_easy_format(AUTO_SUB):
    ''' Format AUTO_SUB and return 2 lists 1 with the times the subtitles are printed to the video and the other the corresponding words. FORMATED_AUTO_SUB_CONTENT, FORMATED_AUTO_SUB_TIMES'''
    from itertools import chain
    

    #initialize required variables
    F1_LIST_AUTO_SUB = []
    F2_LIST_AUTO_SUB = []
    F5_LIST_AUTO_SUB = []
    F6_LIST_AUTO_SUB = []
    F7_LIST_AUTO_SUB = []
    AUTO_SUB_CONTENT = []
    AUTO_SUB_TIMINGS = []
    F1_AUTO_SUB_CONTENT = []
    F1_str_cont_sent = []
    F2_str_cont_sent = []
    F3_str_cont_sent = []
    F1_STR_TIME_SENT = []
    F4_str_cont_sent = []
    
    ## filter and create a list 
    LIST_AUTO_SUB=AUTO_SUB.split('align:start position:0%')
    
    # get the length of the list
    LEN_LIST_AUTO_SUB=len(LIST_AUTO_SUB)
    
    # remove dublicate subtitles within the list
    for i in range(LEN_LIST_AUTO_SUB):
        if ('<c>' in str(LIST_AUTO_SUB[i]) or '</c>' in str(LIST_AUTO_SUB[i])):
            F1_LIST_AUTO_SUB.append(str(LIST_AUTO_SUB[i]))
        else:
            pass
        
    # get the length of the new variable
    LEN_F1_LIST_AUTO_SUB=len(F1_LIST_AUTO_SUB)
    
    # filter further unceseccary info
    for k in range(LEN_F1_LIST_AUTO_SUB):
        
        temp_list_var = list(F1_LIST_AUTO_SUB[k])
        temp_str_var = str(F1_LIST_AUTO_SUB[k])
        
        # get the position of '-->' in the file
        INDEX=temp_str_var.find('-->')
        
        
        #first half
        temp_str_var_1=temp_str_var[0:INDEX-13]
        temp_str_var_2=temp_str_var[INDEX+16:]
        total=temp_str_var_1+temp_str_var_2
        F2_LIST_AUTO_SUB.append(total)
        
    # SIMPLIFY
    
    F3_STR_AUTO_SUB=''.join(F2_LIST_AUTO_SUB)
    F4_LIST_AUTO_SUB=F3_STR_AUTO_SUB.split('\n')
    
    #get the length 
    LEN_F4_LIST_AUTO_SUB = len(F4_LIST_AUTO_SUB)
    
    for i in range(LEN_F4_LIST_AUTO_SUB):
        if ('<c>' in str(F4_LIST_AUTO_SUB[i]) or '</c>' in str(F4_LIST_AUTO_SUB[i])):
            F5_LIST_AUTO_SUB.append(str(F4_LIST_AUTO_SUB[i]))
        else:
            pass
    
    
    #get the length 
    LEN_F5_LIST_AUTO_SUB = len(F5_LIST_AUTO_SUB)
    
    # SIMPLYIFY
    for i in range(LEN_F5_LIST_AUTO_SUB):
        a=F5_LIST_AUTO_SUB[i]
        F6_LIST_AUTO_SUB.append(a.split('<c>'))
    
    F7_LIST_AUTO_SUB=list(chain.from_iterable(F6_LIST_AUTO_SUB))
    
    F8_STR_AUTO_SUB = ''.join(F7_LIST_AUTO_SUB)
    
    F9_STR_AUTO_SUB = F8_STR_AUTO_SUB.replace('</c>', ' ')
    F9_STR_AUTO_SUB_BACKUP = F9_STR_AUTO_SUB
    
    
    INDEX2=F9_STR_AUTO_SUB.find('<') # return the firs occurance
    while True:
        if INDEX2 !=-1:
            AUTO_SUB_CONTENT.append(F9_STR_AUTO_SUB[:INDEX2])
            AUTO_SUB_TIMINGS.append(F9_STR_AUTO_SUB[INDEX2:INDEX2+14])
            F9_STR_AUTO_SUB=F9_STR_AUTO_SUB[INDEX2+14:]
            INDEX2=F9_STR_AUTO_SUB.find('<') # return the firs occurance
        elif INDEX2 == -1:
            break
        else:
            break
    #add the end
    AUTO_SUB_CONTENT.append(F9_STR_AUTO_SUB)
    
    
    
    temp_str_var = AUTO_SUB
    
    # get the position of '-->' in the file
    INDEX3=temp_str_var.find('-->')
    
    
    #first half
    temp_str_var_5=temp_str_var[INDEX3-13:INDEX3-1]
    
    
    # add <00:00:00.000> to AUTO_SUB_TIMINGS
    AUTO_SUB_TIMINGS.insert(0,'<' +temp_str_var_5+ '>')
    
    # remove first and last space if it exists. Note the AUTO_SUB_CONTENT is by 1 value larger than the timings which is expected as the initial value of AUTO_SUB_TIMINGS is missing from the AUTO_SUB_TIMINGS
    LEN_AUTO_SUB_CONTENT=len(AUTO_SUB_CONTENT)
    for i in range(LEN_AUTO_SUB_CONTENT):
        STR_AUTO_SUB_CONTENT=AUTO_SUB_CONTENT[i]
        if STR_AUTO_SUB_CONTENT[0] == ' ':
            STR_AUTO_SUB_CONTENT = STR_AUTO_SUB_CONTENT[1:]
        elif STR_AUTO_SUB_CONTENT[0] != ' ':
            pass
        else:
            pass
        
        if STR_AUTO_SUB_CONTENT[-1] == ' ':
            STR_AUTO_SUB_CONTENT = STR_AUTO_SUB_CONTENT[:-1]
        elif STR_AUTO_SUB_CONTENT[-1] != ' ':
            pass
        else:
            pass
        F1_AUTO_SUB_CONTENT.append(STR_AUTO_SUB_CONTENT)
        
    FORMATED_AUTO_SUB_CONTENT_PER_WORD = F1_AUTO_SUB_CONTENT
    FORMATED_AUTO_SUB_TIMES_PER_WORD = AUTO_SUB_TIMINGS
    
    
    # NOW WE SHALL ALSO FIND THE SUBTITLES WHICH ARE ALINGED IN TERMS OF sentences RATHER THAN per word
    
    cont_sent, time_sent =filter_hard_format(MAN_SUB=AUTO_SUB)
    
    # filter cont_sent
    L=len(cont_sent)
    for i in range(L):
        str_cont_sent=str(cont_sent[i])
        if (str_cont_sent.find('<c>')!=-1 or str_cont_sent.find('</c>')!=-1):
            pass
        elif (str_cont_sent.find('<c>')==-1 or str_cont_sent.find('</c>')==-1):
            F1_str_cont_sent.append(str_cont_sent)
        else:
            pass
    LL=len(F1_str_cont_sent)
    for i in range(LL):
        str_F2_str_cont_sent=str(F1_str_cont_sent[i])
        F2_str_cont_sent.append(str_F2_str_cont_sent.replace('align:start position:0%', ''))
    
    #simplify
    # remove first and last space if it exists the first and last \n if it exists.
    
    LEN_F2_str_cont_sent=len(F2_str_cont_sent)
    for i in range(LEN_F2_str_cont_sent):
        STR_F2_str_cont_sent=F2_str_cont_sent[i]
        
        if STR_F2_str_cont_sent[0] == '\n':
            STR_F2_str_cont_sent = STR_F2_str_cont_sent[1:]
        elif STR_F2_str_cont_sent[0] != 'n':
            pass
        else:
            pass
        
        if STR_F2_str_cont_sent[-1] == '\n':
            STR_F2_str_cont_sent = STR_F2_str_cont_sent[:-1]
        elif STR_F2_str_cont_sent[-1] != '\n':
            pass
        else:
            pass
        
        if STR_F2_str_cont_sent[0] == ' ':
            STR_F2_str_cont_sent = STR_F2_str_cont_sent[1:]
        elif STR_F2_str_cont_sent[0] != ' ':
            pass
        else:
            pass
        
        if STR_F2_str_cont_sent[-1] == ' ':
            STR_F2_str_cont_sent = STR_F2_str_cont_sent[:-1]
        elif STR_F2_str_cont_sent[-1] != ' ':
            pass
        else:
            pass
        
        try:    
            if STR_F2_str_cont_sent[0] == '\n':
                STR_F2_str_cont_sent = STR_F2_str_cont_sent[1:]
            elif STR_F2_str_cont_sent[0] != 'n':
                pass
            else:
                pass
            
            if STR_F2_str_cont_sent[-1] == '\n':
                STR_F2_str_cont_sent = STR_F2_str_cont_sent[:-1]
            elif STR_F2_str_cont_sent[-1] != '\n':
                pass
            else:
                pass
        except:
            pass
        
        F3_str_cont_sent.append(STR_F2_str_cont_sent)
    
    #Now we will take care of the timings
    
    #simplify
    LLL=len(time_sent)
    
    for i in range(LLL):
        str_time_sent=time_sent[i]
        f1_str_time_sent = str_time_sent.replace(' ', '')
        f2_str_time_sent = f1_str_time_sent.replace('-->','')
        f3_str_time_sent = f2_str_time_sent.replace(':','')
        f4_str_time_sent = f3_str_time_sent.replace('.','')
        if (int(f4_str_time_sent[9:])-int(f4_str_time_sent[:9]))==10:
            pass
            #F1_STR_TIME_SENT.append(None)
        elif (int(f4_str_time_sent[9:])-int(f4_str_time_sent[:9]))>=10:
            F1_STR_TIME_SENT.append(str_time_sent)
        else:
            F1_STR_TIME_SENT.append(str_time_sent)
    
    
    
    
    # check for any doublicates
    LT=len(F1_STR_TIME_SENT)
    LC=len(F3_str_cont_sent)
    # PRESERVE F3_str_cont_sent AND MODIFY F3_str_cont_sent
    
    if LC==LT:
        pass
    elif LC>LT:
        # SIZE_DIFFERENCE is the value we wish to remove
        SIZE_DIFFERENCE=LC-LT
        # THE FOLLWONG BLOCK OF CODE CHECKS FOR EVERY VALUE IN THE LIST F3_str_cont_sent and compares it witht the values right above and belos if both the above value and below value are containd in the middle value, the middle vale is removed
        for i in range(LC-2):
            A1 = str(F3_str_cont_sent[i])
            A2 = str(F3_str_cont_sent[i+1])
            A3 = str(F3_str_cont_sent[i+2])
            #A1_CONT_A2=A1.find(str(A2))
            #A1_CONT_A3=A1.find(str(A3))
            
            A2_CONT_A1=A2.find(str(A1))
            A2_CONT_A3=A2.find(str(A3))
            
            #A3_CONT_A1=A3.find(str(A1))
            #A3_CONT_A2=A3.find(str(A2))
            
            if (A2_CONT_A1 != -1 and A2_CONT_A3 != -1):
                pass
            else:
                F4_str_cont_sent.append(A2)
        
        F4_str_cont_sent.insert(0, str(F3_str_cont_sent[0]))
        F4_str_cont_sent.insert(len(F4_str_cont_sent), str(F3_str_cont_sent[-1]))
        
        # requires further imporvement to check both ends for dublicates
        '''
        # check the first and last avariable for dublicate values
        S1 = str(F4_str_cont_sent[0])
        S2 = str(F4_str_cont_sent[1])
        S3 = str(F4_str_cont_sent[len(F4_str_cont_sent)-2])
        S4 = str(F4_str_cont_sent[len(F4_str_cont_sent)-1])
        
        S1_CONT_S2=S1.find(S2)
        S2_CONT_S1=S2.find(S1)
        
        S3_CONT_S4=S3.find(S4)
        S4_CONT_S3=S4.find(S3)
        
        if (S1_CONT_S2 != -1): # S1 contains the value of S2 remove the S2 from F4_str_cont_sent
    #        F4_str_cont_sent.pop(1) 
            F4_str_cont_sent.pop(0) # remove the value which contains both intsted, the largest
    
        elif (S2_CONT_S1 != -1):
    #        F4_str_cont_sent.pop(0)
            F4_str_cont_sent.pop(1) # remove the value which contains both intsted, the largest. For instance A = 'HELLO', B = 'HELLOW WORLD' remove B
        else:
            pass
    
        # same but for the last values
        if (S3_CONT_S4 != -1): # S3 contains the value of S4 remove the S4 from F4_str_cont_sent
            F4_str_cont_sent.pop(len(F4_str_cont_sent)-2)
    #        F4_str_cont_sent.pop(len(F4_str_cont_sent)-1)
    
        elif (S4_CONT_S3 != -1):
            F4_str_cont_sent.pop(len(F4_str_cont_sent)-1)
    #        F4_str_cont_sent.pop(len(F4_str_cont_sent)-2)
    
        else:
            pass
        '''
            
        if len(F4_str_cont_sent) != LT:
            print('Error something as gone wrong in the processing of variable F4_str_cont_sent. The length of F4_str_cont_sent should be equal to the length of F1_STR_TIME_SENT and it is not.')
        else:
            pass
    
    elif LC<LT:
        print('Error something as gone wrong in the processing of variable F3_str_cont_sent. The length of F3_str_cont_sent should be equal or greater than the length of F1_STR_TIME_SENT and it is not.')
    else:
        pass
        
    FORMATED_AUTO_SUB_CONTENT_PER_SENTENCE = F4_str_cont_sent
    FORMATED_AUTO_SUB_TIMES_PER_SENTENCE = F1_STR_TIME_SENT
    
    del AUTO_SUB
    del AUTO_SUB_CONTENT
    del F2_LIST_AUTO_SUB
    del F3_STR_AUTO_SUB
    del F4_LIST_AUTO_SUB
    del F5_LIST_AUTO_SUB
    del F6_LIST_AUTO_SUB
    del F7_LIST_AUTO_SUB
    del F8_STR_AUTO_SUB
    del F9_STR_AUTO_SUB
    del F9_STR_AUTO_SUB_BACKUP
    del F1_LIST_AUTO_SUB
    del INDEX
    del INDEX2
    del LEN_AUTO_SUB_CONTENT
    del LEN_F1_LIST_AUTO_SUB
    del LEN_F4_LIST_AUTO_SUB
    del LEN_F5_LIST_AUTO_SUB
    del LEN_LIST_AUTO_SUB
    del LIST_AUTO_SUB
    del STR_AUTO_SUB_CONTENT
    del a
    #    del file
    del i
    del k
    del temp_list_var
    del temp_str_var
    del temp_str_var_1
    del temp_str_var_2
    del total 
    del F1_AUTO_SUB_CONTENT
    del AUTO_SUB_TIMINGS
    del temp_str_var_5
    del INDEX3
    del A1
    del A2
    del A2_CONT_A1
    del A2_CONT_A3
    del F1_STR_TIME_SENT
    del F1_str_cont_sent
    del F2_str_cont_sent
    del F3_str_cont_sent
    del F4_str_cont_sent
    del L
    del LC
    del A3
    del LEN_F2_str_cont_sent
    del LL
    del LLL
    del LT
    del SIZE_DIFFERENCE
    del STR_F2_str_cont_sent
    del cont_sent
    del f1_str_time_sent
    del f2_str_time_sent
    del f3_str_time_sent
    del f4_str_time_sent
    del str_F2_str_cont_sent
    del str_cont_sent
    del str_time_sent
    del time_sent
        
    return FORMATED_AUTO_SUB_CONTENT_PER_WORD, FORMATED_AUTO_SUB_TIMES_PER_WORD, FORMATED_AUTO_SUB_CONTENT_PER_SENTENCE, FORMATED_AUTO_SUB_TIMES_PER_SENTENCE



def filter_hard_format(MAN_SUB):
    ''' Format MAN_SUB and return 2 lists 1 with the times the subtitles are printed to the video and the other the corresponding words. FORMATED_AUTO_SUB_CONTENT, FORMATED_AUTO_SUB_TIMES'''

    LIST_MAN_SUB = list(MAN_SUB)
    
    #create necessary lists
    MAN_SUB_TIMING = []
    MAN_SUB_CONTENT_INDEX = []
    MAN_SUB_CONTENT = []
    F1_MAN_SUB_CONTENT = []
    
    # create man_sub_timing and man_content_index
    for k in range(len(LIST_MAN_SUB)):            
        if (LIST_MAN_SUB[k] == '-' and LIST_MAN_SUB[k + 1] == '-' and LIST_MAN_SUB[k+2] == '>'):
            MAN_SUB_TIMING.append(''.join(LIST_MAN_SUB[k-13:k+16]))
            MAN_SUB_CONTENT_INDEX.append(k)                
        else:
            pass
        
    # create MAN_SUB_CONTENT
    for l in range(len(MAN_SUB_CONTENT_INDEX)):
    
        if l == len(MAN_SUB_CONTENT_INDEX)-1:                                                      
            MAN_SUB_CONTENT.append(''.join(LIST_MAN_SUB[MAN_SUB_CONTENT_INDEX[l]+16:]))
    
        elif l != len(MAN_SUB_CONTENT_INDEX):
            man_low_indx_bound=MAN_SUB_CONTENT_INDEX[l]+16
            man_high_indx_bound=MAN_SUB_CONTENT_INDEX[l+1]-13
            MAN_SUB_CONTENT.append(''.join(LIST_MAN_SUB[man_low_indx_bound:man_high_indx_bound]))
    
        else:
            pass
    
    # remove first and last space if it exists the first and last \n if it exists.
    
    LEN_MAN_SUB_CONTENT=len(MAN_SUB_CONTENT)
    for i in range(LEN_MAN_SUB_CONTENT):
        STR_MAN_SUB_CONTENT=MAN_SUB_CONTENT[i]
        
        if STR_MAN_SUB_CONTENT[0] == '\n':
            STR_MAN_SUB_CONTENT = STR_MAN_SUB_CONTENT[1:]
        elif STR_MAN_SUB_CONTENT[0] != 'n':
            pass
        else:
            pass
        
        if STR_MAN_SUB_CONTENT[-1] == '\n':
            STR_MAN_SUB_CONTENT = STR_MAN_SUB_CONTENT[:-1]
        elif STR_MAN_SUB_CONTENT[-1] != '\n':
            pass
        else:
            pass
        
        if STR_MAN_SUB_CONTENT[0] == ' ':
            STR_MAN_SUB_CONTENT = STR_MAN_SUB_CONTENT[1:]
        elif STR_MAN_SUB_CONTENT[0] != ' ':
            pass
        else:
            pass
        
        if STR_MAN_SUB_CONTENT[-1] == ' ':
            STR_MAN_SUB_CONTENT = STR_MAN_SUB_CONTENT[:-1]
        elif STR_MAN_SUB_CONTENT[-1] != ' ':
            pass
        else:
            pass
        
        try:    
            if STR_MAN_SUB_CONTENT[0] == '\n':
                STR_MAN_SUB_CONTENT = STR_MAN_SUB_CONTENT[1:]
            elif STR_MAN_SUB_CONTENT[0] != 'n':
                pass
            else:
                pass
            
            if STR_MAN_SUB_CONTENT[-1] == '\n':
                STR_MAN_SUB_CONTENT = STR_MAN_SUB_CONTENT[:-1]
            elif STR_MAN_SUB_CONTENT[-1] != '\n':
                pass
            else:
                pass
        except:
            pass
        
        F1_MAN_SUB_CONTENT.append(STR_MAN_SUB_CONTENT)
    
    del man_high_indx_bound
    del man_low_indx_bound
    del l
    del k
    del i
    del STR_MAN_SUB_CONTENT
    del MAN_SUB_CONTENT_INDEX
    del MAN_SUB
    del LIST_MAN_SUB
    del LEN_MAN_SUB_CONTENT
    del MAN_SUB_CONTENT
    FORMATED_MAN_SUB_CONTENT = F1_MAN_SUB_CONTENT
    FORMATED_MAN_SUB_TIMES = MAN_SUB_TIMING
    del F1_MAN_SUB_CONTENT
    del MAN_SUB_TIMING
    return FORMATED_MAN_SUB_CONTENT, FORMATED_MAN_SUB_TIMES





# function responsible for inputs and outputs
def format_sub(MAN_SUB_EXIST, AUTO_SUB_EXIST, MAN_SUB_EASY_TYPE, AUTO_SUB_EASY_TYPE, MAN_SUB, AUTO_SUB):
    '''
    This function calls the follwing other functions based on the input criteria

    I_MAN_SUB_EXIST=False
    I_AUTO_SUB_EXIST=True
    I_MAN_SUB_EASY_TYPE=False
    I_AUTO_SUB_EASY_TYPE= True

    cont_per_word_easy, time_per_word_easy, cont_per_sentence_easy, time_per_sentence_easy = filter_easy_format(AUTO_SUB=I_AUTO_SUB)
    cont_per_sentence_hard, time_per_sentence_hard =filter_hard_format(MAN_SUB=I_MAN_SUB)

    '''
    # auto sub
    if AUTO_SUB_EXIST==True:
        #print(-5)
        if AUTO_SUB_EASY_TYPE==True:
            
            AUTO_CONT_PER_WORD_EASY, AUTO_TIME_PER_WORD_EASY, AUTO_COUNT_PER_SENTENCE_EASY, AUTO_TIME_PER_SENTENCE_EASY = filter_easy_format(AUTO_SUB)
            AUTO_COUNT_PER_SENTENCE_HARD=None
            AUTO_TIME_PER_SENTENCE_HARD=None
            #print('-4')
            
        elif AUTO_SUB_EASY_TYPE==False:
        
            AUTO_COUNT_PER_SENTENCE_HARD, AUTO_TIME_PER_SENTENCE_HARD =filter_hard_format(AUTO_SUB)
            AUTO_CONT_PER_WORD_EASY=None
            AUTO_TIME_PER_WORD_EASY=None
            AUTO_COUNT_PER_SENTENCE_EASY=None
            AUTO_TIME_PER_SENTENCE_EASY=None
            #print('-3')
        
        else:
            print('Please provide a value for AUTO_SUB_EASY_TYPE,  True or false')
            #print('-2')
            
    elif AUTO_SUB_EXIST==False:
        
        AUTO_CONT_PER_WORD_EASY=None
        AUTO_TIME_PER_WORD_EASY=None
        
        AUTO_COUNT_PER_SENTENCE_EASY=None
        AUTO_TIME_PER_SENTENCE_EASY=None
        
        AUTO_COUNT_PER_SENTENCE_HARD=None
        AUTO_TIME_PER_SENTENCE_HARD=None
        #print('-1')

    else:
        print('Please provide a value for AUTO_SUB_EXIST,  True or false')

        AUTO_CONT_PER_WORD_EASY=None
        AUTO_TIME_PER_WORD_EASY=None
        
        AUTO_COUNT_PER_SENTENCE_EASY=None
        AUTO_TIME_PER_SENTENCE_EASY=None
        
        AUTO_COUNT_PER_SENTENCE_HARD=None
        AUTO_TIME_PER_SENTENCE_HARD=None
        #print('0')
    
    # man sub
    if MAN_SUB_EXIST==True:
        #print('0')
        if MAN_SUB_EASY_TYPE==True:
            
            MAN_COUNT_PER_WORD_EASY,  MAN_TIME_PER_WORD_EASY,  MAN_COUNT_PER_SENTENCE_EASY,  MAN_TIME_PER_SENTENCE_EASY = filter_easy_format(MAN_SUB)
            MAN_COUNT_PER_SENTENCE_HARD=None
            MAN_TIME_PER_SENTENCE_HARD=None
            #print('1')
        elif MAN_SUB_EASY_TYPE==False:
            MAN_COUNT_PER_SENTENCE_HARD, MAN_TIME_PER_SENTENCE_HARD =filter_hard_format(MAN_SUB)
            MAN_COUNT_PER_WORD_EASY=None
            MAN_TIME_PER_WORD_EASY=None
            MAN_COUNT_PER_SENTENCE_EASY=None
            MAN_TIME_PER_SENTENCE_EASY=None
            #print('2')

        else:
            print('Please provide a value for MAN_SUB_EASY_TYPE,  True or false')
            MAN_COUNT_PER_WORD_EASY=None
            MAN_TIME_PER_WORD_EASY=None
           
            MAN_COUNT_PER_SENTENCE_EASY=None
            MAN_TIME_PER_SENTENCE_EASY=None
           
            MAN_COUNT_PER_SENTENCE_HARD=None
            MAN_TIME_PER_SENTENCE_HARD=None
            #print('3')
    elif MAN_SUB_EXIST==False:
        MAN_COUNT_PER_WORD_EASY=None
        MAN_TIME_PER_WORD_EASY=None
       
        MAN_COUNT_PER_SENTENCE_EASY=None
        MAN_TIME_PER_SENTENCE_EASY=None
       
        MAN_COUNT_PER_SENTENCE_HARD=None
        MAN_TIME_PER_SENTENCE_HARD=None
        #print('4')
    else:
        print('Please provide a value for MAN_SUB_EXIST,  True or false')

        MAN_COUNT_PER_WORD_EASY=None
        MAN_TIME_PER_WORD_EASY=None
       
        MAN_COUNT_PER_SENTENCE_EASY=None
        MAN_TIME_PER_SENTENCE_EASY=None
       
        MAN_COUNT_PER_SENTENCE_HARD=None
        MAN_TIME_PER_SENTENCE_HARD=None
        #print('5')
    

    
    return AUTO_CONT_PER_WORD_EASY, AUTO_TIME_PER_WORD_EASY, AUTO_COUNT_PER_SENTENCE_EASY, AUTO_TIME_PER_SENTENCE_EASY, AUTO_COUNT_PER_SENTENCE_HARD, AUTO_TIME_PER_SENTENCE_HARD, MAN_COUNT_PER_WORD_EASY, MAN_TIME_PER_WORD_EASY, MAN_COUNT_PER_SENTENCE_EASY, MAN_TIME_PER_SENTENCE_EASY, MAN_COUNT_PER_SENTENCE_HARD, MAN_TIME_PER_SENTENCE_HARD
        






























''' testing section'''
##
#file = open('SUBTITLES_auto_sub1.en.vtt', 'r') 
#I_AUTO_SUB = file.read()


#file = open('SUBTITLES_man_sub.en.vtt', 'r') 
#I_MAN_SUB = file.read() 
##

##
# test filter_easy_format
#cont_per_word_easy, time_per_word_easy, cont_per_sentence_easy, time_per_sentence_easy = filter_easy_format(AUTO_SUB=I_AUTO_SUB)
##
##
# test filter_hard_format
#cont_per_sentence_hard, time_per_sentence_hard =filter_hard_format(MAN_SUB=I_MAN_SUB)
##

##
# I_MAN_SUB_EXIST=True # 0
# I_AUTO_SUB_EXIST=True #-5

# I_MAN_SUB_EASY_TYPE=False # 2
# I_AUTO_SUB_EASY_TYPE= True #-4
##

##
# I_MAN_SUB_EXIST=False # 4
# I_AUTO_SUB_EXIST=False #-1

# I_MAN_SUB_EASY_TYPE=False # 2
# I_AUTO_SUB_EASY_TYPE= True #-4
##
  
##  
#I_MAN_SUB_EXIST=True # 0
#I_AUTO_SUB_EXIST=True #-5

#I_MAN_SUB_EASY_TYPE=False # 2
#I_AUTO_SUB_EASY_TYPE= True #-4
##

##
'''
acpwe#auto_cont_per_word_easy
atpwe#auto_time_per_word_easy
acpse#auto_count_per_sentence_easy
atpse#auto_time_per_sentence_easy
acpsh#auto_count_per_sentence_hard
atpsh#auto_time_per_sentence_hard

mcpwe#man_count_per_word_easy
mtpwe#man_time_per_word_easy
mcpse#man_count_per_sentence_easy
mtpse#man_time_per_sentence_easy
mcpsh#man_count_per_sentence_hard
mtpsh#man_time_per_sentence_hard
'''
#acpwe, atpwe, acpse, atpse, acpsh, atpsh, mcpwe, mtpwe, mcpse, mtpse, mcpsh, mtpsh = format_sub(MAN_SUB_EXIST = I_MAN_SUB_EXIST, AUTO_SUB_EXIST = I_AUTO_SUB_EXIST, MAN_SUB_EASY_TYPE = I_MAN_SUB_EASY_TYPE, AUTO_SUB_EASY_TYPE = I_AUTO_SUB_EASY_TYPE, MAN_SUB = I_MAN_SUB, AUTO_SUB = I_AUTO_SUB)
##

##
#del I_MAN_SUB_EXIST
#del I_AUTO_SUB_EXIST
#del I_MAN_SUB_EASY_TYPE
#del I_AUTO_SUB_EASY_TYPE
#del I_AUTO_SUB
#del I_MAN_SUB
#del I_AUTO_SUB
##