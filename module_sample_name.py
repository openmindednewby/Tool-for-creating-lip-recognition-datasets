''' This function which will print the random name sample variable'''

#-------------------------
# Random password generator function
def passw_gen(MODE=3,LENGTH=10):
   ''' 
   passw_gen(MODE=3,LENGTH=10)
   
   The first argument MODE determins the characters which will be used in the random name generation
   MODE=0 for letters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   MODE=1 for digits: 0123456789
   MODE=2 for special characters: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
   MODE=3 for letters and digits (defult): abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
   MODE=4 for letters and special characters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
   MODE=5 for digits and special characters: 0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
   MODE=6 for digits, letters and special characters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
   
   The second argument LENGTH determins the length of the random generated password'''
   
   import string
   import random
   
   # create a character list which contains all possible character generation modes
   characters=['1','2','3','4','5','6','7']
   characters[0] = string.ascii_letters 
   characters[1] = string.digits 
   characters[2] = string.punctuation 
   characters[3] = string.ascii_letters + string.digits 
   characters[4] = string.ascii_letters + string.punctuation
   characters[5] = string.digits + string.punctuation
   characters[6] = string.ascii_letters + string.digits + string.punctuation
    
   MODE=int(MODE)# convert input into an int
   LENGTH=int(LENGTH)# convert input into an int
   password =  "".join(random.choice(characters[MODE]) for x in range(LENGTH)) # The join() method takes all items in an iterable and joins them into one string.
   return password





#---------------------------
# name generator fuction

from datetime import date

def name_gen(TYPE=1,WORD_LENGTH=0,WORD=0,POSITION='X',YEAR=str(date.today())):
    '''
    name_gen(TYPE=1,WORD_LENGTH=0,WORD=0,POSITION='X',YEAR=str(date.today())):         

    The TYPE argument accepts either values of 0 or 1 and is use to add the 'V' for a video file or 'A' for an audio file and 'W' for the file containing the word infront of the random generated name. The defult value is 1 which coresponds to video format.

    The WORD_LENGTH argument accepts any integer between 0 to (length of word -1). It determins how many letters starting from the first letter to include in the file name from the WORD argument. If the argument 'a' is passed, the whole length of the word is added to the file name. If any other string is passed the vlaue is set to 0 and only the first letter is  printed. If a float is passed, if it is of the format 1.0 2.0 0.0 it is intepred as an intiger otherwise WORD_LENGTH=0.

    The WORD argument accepts any STR input and extracts the first letter of the word and assignes it to INDEX_1    
    
    The POSITION argument is used to assign the position of the word in a sentence. For example in the sentence 'Where is Bob', the word Bob is the 3rd word i the sentence there for its position is 3. If no argument is used the 'XX' will be assigned in the 14 and 15 index values of the name.
    
    The YEAR argument should correspond to the current year the file was created in an integer format of YYYY, if no argument is passed the current year the machine is set at the machine is used. 
    '''
    #TYPE
    # Checks to see what argument is passed to TYPE and makes sure the INDEX+0 variable is assigned with The correct argument
    if TYPE == 0:
       INDEX_0 ='A'
    elif TYPE == 1:
       INDEX_0 = 'V'
    elif TYPE ==2:
        INDEX_0 = 'W'
    else:
       INDEX_0 = 'V'
       
    # WORD_LENGTH 
    if (str(type(WORD_LENGTH))==str(str)) and (WORD_LENGTH!='a'):# if integer is input
        WORD_LENGTH=0
    elif (str(type(WORD_LENGTH))==str(float)) and WORD_LENGTH-int(WORD_LENGTH)==0:
            WORD_LENGTH=int(WORD_LENGTH)
    elif (str(type(WORD_LENGTH))==str(float)) and WORD_LENGTH-int(WORD_LENGTH)!=0:
            WORD_LENGTH=0
    else:
        pass

    # WORD
    # Checks to see what argument is passed to WORD and makes sure the INDEX+1 variable is assigned with the first letter of the word

    if str(type(WORD))==str(int):# if integer is input
        WORD=0
        INDEX_1='0'
    elif str(type(WORD))==str(float):# if float input
        WORD=0
        INDEX_1='0'
    elif (str(type(WORD))==str(str) and WORD_LENGTH=='a'):
        INDEX_1=WORD
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==0): 
        INDEX_1=WORD[0]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==1): 
        INDEX_1=WORD[0:2]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==2): 
        INDEX_1=WORD[0:3]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==3): 
        INDEX_1=WORD[0:4]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==4): 
        INDEX_1=WORD[0:5]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==5): 
        INDEX_1=WORD[0:6]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==6): 
        INDEX_1=WORD[0:7]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==7): 
        INDEX_1=WORD[0:8]    
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==8): 
        INDEX_1=WORD[0:9]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==9): 
        INDEX_1=WORD[0:10]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==10): 
        INDEX_1=WORD[0:11]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==11): 
        INDEX_1=WORD[0:12]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==12): 
        INDEX_1=WORD[0:13]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==13): 
        INDEX_1=WORD[0:14]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==14): 
        INDEX_1=WORD[0:15]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==15): 
        INDEX_1=WORD[0:16]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==16): 
        INDEX_1=WORD[0:17]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==17): 
        INDEX_1=WORD[0:18]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==18): 
        INDEX_1=WORD[0:19]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==19): 
        INDEX_1=WORD[0:20]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==20): 
        INDEX_1=WORD[0:21]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==21): 
        INDEX_1=WORD[0:22]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==22): 
        INDEX_1=WORD[0:23]
        
    else:
        WORD='0'
        INDEX_1='0'

    
    #POSITION
    # If a string argument is passed insted of an integer. The value is ignored and the default value 'X' is used FOR BOTH INDEX_14 and INDEX_15
    if str(type(POSITION)) == str(str):
        POSITION= 'X'
        INDEX_15='X'
        INDEX_16='X'
        
    #if an integer value is passed
    if str(type(POSITION))==str(int):
        POSITION=str(POSITION) # convert int to str to allow indexing and len() function
        
        if len(POSITION)==2:# and if its length is equal to 2 transform it into an integer and assign the first value to variable INDEX_14 and second value to variable INDEX_15
            INDEX_15=POSITION[0]
            INDEX_16=POSITION[1]
        elif len(POSITION)==1:# if the legth of the integer passed is equal to 1 convert input into a strign assing 0 for INDEX_14 and the input value for INDEX_15
            INDEX_15='0'
            INDEX_16=POSITION[0]
        # since no sentence can be longer than 100 words, the length passes should be 1 or 2  
        else:
            POSITION= 'X'
            INDEX_15='X'
            INDEX_16='X'
            
    # If a float argument is passed AND its value remains the same if it is converted into an integer. It is accepted if float is of the format 9.0 5.0 3.0 etc
    if (str(type(POSITION)) == str(float) and POSITION-int(POSITION)==0):
        POSITION=int(POSITION)
        POSITION=str(POSITION) # convert to string
        if len(POSITION)==2:
            INDEX_15=POSITION[0]
            INDEX_16=POSITION[1]
        elif len(POSITION)==1:
            INDEX_15='0'
            INDEX_16=POSITION[0]
        else:
            POSITION='X'
            INDEX_15='X'
            INDEX_16='X'
    elif (str(type(POSITION)) == str(float) and POSITION-int(POSITION)!=0):
        POSITION='X'
        INDEX_15='X'
        INDEX_16='X'

            
    # YEAR
    if str(type(YEAR)) == str(int):
        YEAR=str(YEAR)# converts int objects to a string to allow indexing
    
    if str(type(YEAR)) == str(float): # if a float object is passed the output will be the current date of the system which is the defualt value
        YEAR=str(date.today())
        
    if len(YEAR) != 4:    # checks to see whater a 4 digit value is passed as it should, other wise the argument is ingored and the defult value is print which is the current date of the system
        YEAR=str(date.today())
        
    YEAR=YEAR[1:4] # selects the last 3 values of the expected YYYY format
    
    name = INDEX_0+INDEX_1+YEAR+INDEX_15+INDEX_16    
    
    return name







#---------------------------
# Random name and password generator function


from datetime import date

def name_and_pass_gen(PASS_GEN_MODE=3,PASS_GEN_LENGTH=10,TYPE=1,WORD_LENGTH=0,WORD=0,POSITION='X',YEAR=str(date.today())):
    '''
    name_and_pass_gen(PASS_GEN_MODE=3,PASS_GEN_LENGTH=10,TYPE=1,WORD_LENGTH=0,WORD=0,POSITION='X',YEAR=str(date.today())):
    
    PASS_GEN_MODE and PASS_GEN_LENGTH are arguments of the passw_gen function.
     
    The TYPE argument accepts either values of 0 or 1 and is use to add the 'V' for a video file or 'A' for an audio file and 'W' for the file containing the word infront of the random generated name. The defult value is 1 which coresponds to video format.

    The WORD_LENGTH argument accepts any integer between 0 to (length of word -1). It determins how many letters starting from the first letter to include in the file name from the WORD argument. If the argument 'a' is passed, the whole length of the word is added to the file name. If any other string is passed the vlaue is set to 0 and only the first letter is  printed. If a float is passed, if it is of the format 1.0 2.0 0.0 it is intepred as an intiger otherwise WORD_LENGTH=0.

    The WORD argument accepts any STR input and extracts the first letter of the word and assignes it to INDEX_1    
    
    The POSITION argument is used to assign the position of the word in a sentence. For example in the sentence 'Where is Bob', the word Bob is the 3rd word i the sentence there for its position is 3. If no argument is used the 'XX' will be assigned in the 14 and 15 index values of the name.
    
    The YEAR argument should correspond to the current year the file was created in an integer format of YYYY, if no argument is passed the current year the machine is set at the machine is used. 
    '''

    # generate a random password
    password=passw_gen(PASS_GEN_MODE,PASS_GEN_LENGTH)
    
    #TYPE
    # Checks to see what argument is passed to TYPE and makes sure the INDEX+0 variable is assigned with The correct argument
    if TYPE == 0:
       INDEX_0 ='A'
    elif TYPE == 1:
       INDEX_0 = 'V'
    elif TYPE ==2:
        INDEX_0 = 'W'
    else:
       INDEX_0 = 'V'
       
    # WORD_LENGTH 
    if (str(type(WORD_LENGTH))==str(str)) and (WORD_LENGTH!='a'):# if integer is input
        WORD_LENGTH=0
    elif (str(type(WORD_LENGTH))==str(float)) and WORD_LENGTH-int(WORD_LENGTH)==0:
            WORD_LENGTH=int(WORD_LENGTH)
    elif (str(type(WORD_LENGTH))==str(float)) and WORD_LENGTH-int(WORD_LENGTH)!=0:
            WORD_LENGTH=0
    else:
        pass

    # WORD
    # Checks to see what argument is passed to WORD and makes sure the INDEX+1 variable is assigned with the first letter of the word

    if str(type(WORD))==str(int):# if integer is input
        WORD=0
        INDEX_1='0'
    elif str(type(WORD))==str(float):# if float input
        WORD=0
        INDEX_1='0'
    elif (str(type(WORD))==str(str) and WORD_LENGTH=='a'):
        INDEX_1=WORD
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==0): 
        INDEX_1=WORD[0]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==1): 
        INDEX_1=WORD[0:2]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==2): 
        INDEX_1=WORD[0:3]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==3): 
        INDEX_1=WORD[0:4]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==4): 
        INDEX_1=WORD[0:5]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==5): 
        INDEX_1=WORD[0:6]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==6): 
        INDEX_1=WORD[0:7]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==7): 
        INDEX_1=WORD[0:8]    
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==8): 
        INDEX_1=WORD[0:9]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==9): 
        INDEX_1=WORD[0:10]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==10): 
        INDEX_1=WORD[0:11]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==11): 
        INDEX_1=WORD[0:12]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==12): 
        INDEX_1=WORD[0:13]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==13): 
        INDEX_1=WORD[0:14]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==14): 
        INDEX_1=WORD[0:15]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==15): 
        INDEX_1=WORD[0:16]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==16): 
        INDEX_1=WORD[0:17]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==17): 
        INDEX_1=WORD[0:18]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==18): 
        INDEX_1=WORD[0:19]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==19): 
        INDEX_1=WORD[0:20]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==20): 
        INDEX_1=WORD[0:21]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==21): 
        INDEX_1=WORD[0:22]
    elif (str(type(WORD))==str(str) and int(WORD_LENGTH)==22): 
        INDEX_1=WORD[0:23]
        
    else:
        WORD='0'
        INDEX_1='0'

    
    #POSITION
    # If a string argument is passed insted of an integer. The value is ignored and the default value 'X' is used FOR BOTH INDEX_14 and INDEX_15
    if str(type(POSITION)) == str(str):
        POSITION= 'X'
        INDEX_15='X'
        INDEX_16='X'
        
    #if an integer value is passed
    if str(type(POSITION))==str(int):
        POSITION=str(POSITION) # convert int to str to allow indexing and len() function
        
        if len(POSITION)==2:# and if its length is equal to 2 transform it into an integer and assign the first value to variable INDEX_14 and second value to variable INDEX_15
            INDEX_15=POSITION[0]
            INDEX_16=POSITION[1]
        elif len(POSITION)==1:# if the legth of the integer passed is equal to 1 convert input into a strign assing 0 for INDEX_14 and the input value for INDEX_15
            INDEX_15='0'
            INDEX_16=POSITION[0]
        # since no sentence can be longer than 100 words, the length passes should be 1 or 2  
        else:
            POSITION= 'X'
            INDEX_15='X'
            INDEX_16='X'
            
    # If a float argument is passed AND its value remains the same if it is converted into an integer. It is accepted if float is of the format 9.0 5.0 3.0 etc
    if (str(type(POSITION)) == str(float) and POSITION-int(POSITION)==0):
        POSITION=int(POSITION)
        POSITION=str(POSITION) # convert to string
        if len(POSITION)==2:
            INDEX_15=POSITION[0]
            INDEX_16=POSITION[1]
        elif len(POSITION)==1:
            INDEX_15='0'
            INDEX_16=POSITION[0]
        else:
            POSITION='X'
            INDEX_15='X'
            INDEX_16='X'
    elif (str(type(POSITION)) == str(float) and POSITION-int(POSITION)!=0):
        POSITION='X'
        INDEX_15='X'
        INDEX_16='X'

            
    # YEAR
    if str(type(YEAR)) == str(int):
        YEAR=str(YEAR)# converts int objects to a string to allow indexing
    
    if str(type(YEAR)) == str(float): # if a float object is passed the output will be the current date of the system which is the defualt value
        YEAR=str(date.today())
        
    if len(YEAR) != 4:    # checks to see whater a 4 digit value is passed as it should, other wise the argument is ingored and the defult value is print which is the current date of the system
        YEAR=str(date.today())
        
    YEAR=YEAR[1:4] # selects the last 3 values of the expected YYYY format
    
    
    name = INDEX_0+INDEX_1+password+YEAR+INDEX_15+INDEX_16
    
    
    
    return name











#---------------------------
# Random name and password generator function


from datetime import date

def add_name_and_pass(FILE_NAME='', PASSWORD=''):
    '''
    add_name_and_pass(FILE_NAME='', PASSWORD='')
    
    FILE_NAME corresponds to the name of the file generated from the name_gen function
    
    PASSWORD the random string of integers generated from the pass_gen function
    
    This fanction preserves the same format of function name_and_pass_gen regardless of the FILE_NAME or PASSWORD
    '''
    if (str(type(FILE_NAME))==str(int)) or (str(type(FILE_NAME)) == str(float)) or (str(type(PASSWORD))==str(int)) or (str(type(PASSWORD)) == str(float)):
        return print('Only string inputs are accepted for function add_name_and_pass')
    
    LENGTH=len(FILE_NAME)
    name = FILE_NAME[0:int(LENGTH-5)] + PASSWORD + FILE_NAME[int(LENGTH-5):]
    
    return name





#---------------------
# Create a folder and assign with the input name 
def folder_gen(RANDOM_STRING, FILE_PERMISION = '777'):
    ''' RANDOM_STRING ---> is the name of the folder to be generated
        FILE_PERMISION ---> The rights to the folder
    '''
    import os
    import subprocess

    # create the folder
    command = 'mkdir -m' + str(FILE_PERMISION) +' ' + str(RANDOM_STRING) # + ' >/dev/null 2>&1'
    subprocess.call(command, shell=True)

    # get the full path as an output
    FOLDER_PATH = os.path.abspath(str(RANDOM_STRING))
    FOLDER_PATH = str(FOLDER_PATH)

    return FOLDER_PATH