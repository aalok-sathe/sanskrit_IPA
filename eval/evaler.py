#! /bin/env/ python3

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import transcriber_data as td

def transcribe(text):
    return td.transcribe(text)
    
def transcribe_file(filename):
    lines = None
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    #try:
    for line_index in range(len(lines)):
        print(lines[line_index].split()[0], "\t", transcribe(lines[line_index].split()[0]))
    #except Exception as E:
    #    print(E)

transcribe_file("words.csv")
