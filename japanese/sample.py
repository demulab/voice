# -*- coding: utf-8 -*-
"""
Usage: python sample.py input.wav
"""
import sys
import base64
import json
import urllib2
 
#　Cloud-based speech recognition URL
URL ='http://rospeex.ucri.jgn-x.jp/nauth_json/jsServices/VoiceTraSR'
 
def read_wavfile(filename):
    with open(filename,'rb') as rf:
        wav = rf.read()
    return wav
 
def post_to_recognizer(wav):
    buf = base64.b64encode(wav)
    json_data = { "method":"recognize",
                  "params":( "ja",
                             {"audio":buf, "audioType":"audio/x-wav", "voiceType":"*" } ) }
    json_obj = json.dumps(json_data)
    req = urllib2.Request(URL, json_obj)
    cont = urllib2.urlopen(req).read()
    return cont
 
def print_text(json_str):
    json_obj = json.loads(json_str)
#    print json_obj['result'].encode('utf-8')
    print json_obj['result']
 
if __name__=='__main__':
    argv = sys.argv
    wav = read_wavfile(argv[1])
    recognition_result = post_to_recognizer(wav)
    print_text(recognition_result)
