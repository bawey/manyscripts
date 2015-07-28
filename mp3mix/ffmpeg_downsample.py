#!/bin/python

import commands
import re
import sys

class TrackInfo:
    
    pattern_bitrate = 'bitrate[\s]*:[\s]*(\d+)[\s]*kb/s'
    pattern_artist = 'artist[\s]*:[\s]*(.+)'
    pattern_title = 'title[\s]*:[\s]*(.+)'
    pattern_filename = "filename=(.+)"
    
    def __init__(self, path):
        command = "ffprobe 2>&1 -i \""+path+"\" -show_format"
        # print "Presenting output for %s" % command
        (status, output) = commands.getstatusoutput(command)
        # print output
        self.bitrate = int(re.search(TrackInfo.pattern_bitrate, output).group(1))
        self.filename = re.search(TrackInfo.pattern_filename, output).group(1)
        self.filename = self.filename[:self.filename.rfind('.')].strip()
        self.title = None
        self.artist = None
        self.guessed = False;
        match = re.search(TrackInfo.pattern_title, output)
        if match: self.title = match.group(1)       
        match = re.search(TrackInfo.pattern_artist, output)
        if match: self.artist = match.group(1)
        
        if self.artist == None or self.title == None:
            (guess_art, guess_title) = self.guess_artist_title()
            if self.artist == None: self.artist = guess_art
            if self.title == None: self.title = guess_title
    
    def guess_artist_title(self):
        if self.filename.find('-') > -1:
            tokens = self.filename.split('-')
            if len(tokens) == 2:
                return (tokens[0].strip(), tokens[1].strip())
        return (self.filename, self.filename);
    
    def repr(self):
        if self.title and self.artist:
            return "%s by %s" % (self.title, self.artist)
        else:
            return self.filename


def main(args):
    info = TrackInfo(args['input'])
    if info.bitrate > args['bitrate'] + args['tolerance']:
        print "Song\'s %s bitrate %d is high enough for conversion." % (info.title, info.bitrate)
        
        command = "ffmpeg -i \"%s\" \"%s\" -b %d " % (args['input'], args['output'], args['bitrate'])
        if not info.title:
            command +=" -metadata title=\"TrackInfo.filename\""
        
    else:
        print "Song\'s %s bitrate %d is fine." % (info.title, info.bitrate)
        command = "cp \"%s\" \"%s\"" % (args['input'], args['output'])
    (status, output) = commands.getstatusoutput(command)
    if status != '0':
        print 'There was some problem: ' + output + '!'
    
def usage():
        print """
ffmpeg_downsampler: ffmpeg frontend to quickly downsample mp3 files. 

Usage:
    ffmpeg_downsampler -i input_file -o output_file -b bitrate_kbps -t input_bitrate_tolerance_kbps        

    Files will be directly copied as long as their bitrate <= desired bitrate + bitrate tolerance."""        

if __name__ == '__main__':
    try:
        args = sys.argv[1:]
        args_map = {}
        args_map['input'] = args[args.index('-i')+1]
        args_map['output'] = args[args.index('-o')+1]
        args_map['bitrate'] = int(args[args.index('-b')+1])
        args_map['tolerance'] = int(args[args.index('-t')+1])
    except:
        usage()
        exit
    
    main(args_map)
    