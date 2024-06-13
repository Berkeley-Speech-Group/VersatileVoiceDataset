""" 
Subsample VVD

A quick script for subsampling the VVD for the purposes of the demo
"""

import os 
import glob 
import sys 

if __name__ == '__main__':
    # Get all the files, delete if they're not hit.wav or key.wav
    all_audios = glob.glob('./resources/audios/vvd_files/*/*/*.wav')
    sub_audios = glob.glob('./resources/audios/vvd_files/*/*/hit.wav') + glob.glob('./resources/audios/vvd_files/*/*/key.wav')

    for audio in all_audios:
        if audio not in sub_audios:
            os.remove(audio)

    new_audios = glob.glob('./resources/audios/vvd_files/*/*/*.wav')

    print(f"Len of Original Folder {len(all_audios)}")
    print(f"Len of Subsampled Folder {len(new_audios)}")