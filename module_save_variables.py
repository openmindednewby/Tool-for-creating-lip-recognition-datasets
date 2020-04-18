''' module to save subtitles '''


# acpwe #auto_content_per_word_easy
# atpwe #auto_time_per_word_easy
# acpse #auto_content_per_sentence_easy
# atpse #auto_time_per_sentence_easy
# acpsh #auto_content_per_sentence_hard
# atpsh #auto_time_per_sentence_hard

# mcpwe #man_content_per_word_easy
# mtpwe #man_time_per_word_easy
# mcpse #man_content_per_sentence_easy
def save_pandas_dict_results(VAR_INPUT, FILE_NAME, CSV=True, TXT=True):
    
    
    import pickle
    import csv
    
    if str(type(VAR_INPUT)) != str(type({})):
        print('Error the input value in the function save_dict_results must be a dictionary')
        return None
    else:
        pass
    
    COMPLETE_FILE_NAME_CSV=FILE_NAME+'.csv'
    COMPLETE_FILE_NAME_TXT=FILE_NAME+'.txt'
    
    if CSV == True:
        w = csv.writer(open(COMPLETE_FILE_NAME_CSV, "w"))
        for key, val in VAR_INPUT.items():
            w.writerow([key, val])
    else:
        pass
    
    if TXT == True:
        f = open(COMPLETE_FILE_NAME_TXT,"w")
        f.write( str(VAR_INPUT) )
        f.close()
    else:
        pass
    return None
def save_sub(VAR_INPUT, FILE_NAME, TXT=True, JSON=True, TXT_SEPARATOR = '\n'):
    '''
 
    VAR_INPUT ---> variable to save.
    TO save in TXT format we must input a list

    '''    
    import json
    
    
   
    COMPLETE_FILE_NAME=FILE_NAME+'.txt'
    COMPLETE_FILE_NAME_JSON=FILE_NAME+'.json'
    
    # Chekc the VAR_INPUT if it is type None and if it is terminate the function 
    if VAR_INPUT==None:
        #print('The variable was not saved as it is a None object')
        return None
    else:
        pass
    
    
    if TXT==True:
        f = open(COMPLETE_FILE_NAME, 'w')
        for i in range(len(VAR_INPUT)):
                f.write(str(VAR_INPUT[i]) + TXT_SEPARATOR)
        f.close()
        #print('Variable saved as ', COMPLETE_FILE_NAME)
    else:
        pass
    
    if JSON==True:
        json = json.dumps(VAR_INPUT)
        f = open(COMPLETE_FILE_NAME_JSON, 'w')
        f.write(json)
        f.close()
        #print('Variable saved as ', COMPLETE_FILE_NAME_JSON)
    else:
        pass    
    
    return None

