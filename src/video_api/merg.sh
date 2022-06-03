#!/bin/bash
for f in ./videos/*.mp4 ; do echo file \'$f\' >> list.txt; done && ffmpeg -f concat -safe 0 -i list.txt -s 1280x720 -crf 24 -vf scale=640:-2 stitched-video.mp4 && rm list.txt
