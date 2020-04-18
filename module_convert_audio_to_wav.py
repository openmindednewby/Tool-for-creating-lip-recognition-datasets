''' 
The following script converts ma4 files into wav files which are necessary for aligning the text to the audio
https://github.com/jiaaro/pydub
'''

def dir_conversion_to_wav(FORMAT_FROM='.m4a', DIRECTORY='data/'):
    
    '''
    The following scrypt replaces the .m4a file with a .wav file.
    This function makes use of the code here https://gist.github.com/arjunsharma97/0ecac61da2937ec52baf61af1aa1b759
    '''
    import os
    import argparse

    from pydub import AudioSegment

    formats_to_convert = [FORMAT_FROM]

    for (dirpath, dirnames, filenames) in os.walk(DIRECTORY):
        for filename in filenames:
            if filename.endswith(tuple(formats_to_convert)):

                filepath = dirpath + '/' + filename
                (path, file_extension) = os.path.splitext(filepath)
                file_extension_final = file_extension.replace('.', '')
                try:
                    track = AudioSegment.from_file(filepath, file_extension_final)
                    wav_filename = filename.replace(file_extension_final, 'wav')
                    wav_path = dirpath + '/' + wav_filename
                    print('CONVERTING: ' + str(filepath))
                    file_handle = track.export(wav_path, format='wav')
                    os.remove(filepath)
                except:
                    print("ERROR CONVERTING " + str(filepath))
    return








def file_conversion_to_wav(FORMAT_FROM='.m4a', FILE_NAME='data/', BIT_RATE='192k'):
    '''
    FILE_NAME --> file name to convert
    BIT_RATE --> just the output bit rate
    # Mix down to two channels and set hard output volume
    #awesome.export("mashup.mp3", format="mp3", parameters=["-ac", "2", "-vol", "150"])

    '''
    #import pydub
    import audiosegment
    
    if FORMAT_FROM == '.m4a':
        song = audiosegment.from_file(FILE_NAME + FORMAT_FROM)
        OUTPUT_FILE_NAME=FILE_NAME
        song.export(OUTPUT_FILE_NAME+".wav", format="wav", bitrate="192k")
    
    elif FORMAT_FROM == '.mp3':
        song = audiosegment.from_mp3(FILE_NAME + FORMAT_FROM)
        OUTPUT_FILE_NAME=FILE_NAME
        song.export(OUTPUT_FILE_NAME+".wav", format="wav", bitrate="192k")
    
    elif FORMAT_FROM == '.ogg':
        song = audiosegment.from_ogg(FILE_NAME + FORMAT_FROM)
        OUTPUT_FILE_NAME=FILE_NAME
        song.export(OUTPUT_FILE_NAME+".wav", format="wav", bitrate="192k")
    
    elif FORMAT_FROM == '.flv':
        song = audiosegment.from_flv(FILE_NAME + FORMAT_FROM)
        OUTPUT_FILE_NAME=FILE_NAME
        song.export(OUTPUT_FILE_NAME+".wav", format="wav", bitrate="192k")
  
    elif FORMAT_FROM == '.wma':
        song = audiosegment.from_file(FILE_NAME + FORMAT_FROM)
        OUTPUT_FILE_NAME=FILE_NAME
        song.export(OUTPUT_FILE_NAME+".wav", format="wav", bitrate="192k")
   
    elif FORMAT_FROM == '.aac':
        song = audiosegment.from_flv(FILE_NAME + FORMAT_FROM)
        OUTPUT_FILE_NAME=FILE_NAME
        song.export(OUTPUT_FILE_NAME+".wav", format="wav", bitrate="192k")
    else:
        pass
    return




'''

#Open a WAV file

#from pydub import AudioSegment

#song = AudioSegment.from_wav("never_gonna_give_you_up.wav")

#...or a mp3

#song = AudioSegment.from_mp3("never_gonna_give_you_up.mp3")

#... or an ogg, or flv, or anything else ffmpeg supports

#ogg_version = AudioSegment.from_ogg("never_gonna_give_you_up.ogg")
#flv_version = AudioSegment.from_flv("never_gonna_give_you_up.flv")

#mp4_version = AudioSegment.from_file("never_gonna_give_you_up.mp4", "mp4")
#wma_version = AudioSegment.from_file("never_gonna_give_you_up.wma", "wma")
#aac_version = AudioSegment.from_file("never_gonna_give_you_up.aiff", "aac")

m4a_version = AudioSegment.from_file('data/test3.m4a', "m4a")

song = m4a_version


song.export('test3.wav', format='wav')
song.export("test192k.wav", format="wav", bitrate="192k")
'''


'''
#Slice audio:
# pydub does things in milliseconds
ten_seconds = 10 * 1000
five_seconds = 5 * 1000
first_10_seconds = song[:ten_seconds]

last_5_seconds = song[-five_seconds:]
'''

'''
#Make the beginning louder and the end quieter
# boost volume by 6dB
beginning = first_10_seconds + 6
# reduce volume by 3dB
end = last_5_seconds - 3
'''

'''
#Concatenate audio (add one file to the end of another)

without_the_middle = beginning + end

#How long is it?
without_the_middle.duration_seconds == 15.0

#AudioSegments are immutable

# song is not modified
backwards = song.reverse()
'''

#Crossfade (again, beginning and end are not modified)

# 1.5 second crossfade
#with_style = beginning.append(end, crossfade=1500)

'''
#Repeat
# repeat the clip twice
do_it_over = with_style * 2
'''

'''
#Fade (note that you can chain operations because everything returns an AudioSegment)

# 2 sec fade in, 3 sec fade out
awesome = do_it_over.fade_in(2000).fade_out(3000)
'''

'''
#Save the results (again whatever ffmpeg supports)
#You can pass an optional bitrate argument to export using any syntax ffmpeg supports.
song.export('test3.wav', format='wav')
song.export("test192k.wav", format="wav", bitrate="192k")
'''

'''
#Save the results with tags (metadata)
awesome.export("mashup.mp3", format="mp3", tags={'artist': 'Various artists', 'album': 'Best of 2011', 'comments': 'This album is awesome!'})
'''




#Any further arguments supported by ffmpeg can be passed as a list in a 'parameters' argument, with switch first, argument second. Note that no validation takes place on these parameters, and you may be limited by what your particular build of ffmpeg/avlib supports.

'''
# Use preset mp3 quality 0 (equivalent to lame V0)
awesome.export("mashup.mp3", format="mp3", parameters=["-q:a", "0"])

# Mix down to two channels and set hard output volume
awesome.export("mashup.mp3", format="mp3", parameters=["-ac", "2", "-vol", "150"])
'''