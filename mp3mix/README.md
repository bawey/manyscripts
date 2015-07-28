Downsampling and mixng audio files for a "car mp3 mix"
======================================================

The problem: fill up a 700MB cd with as many decent-quality mp3 files as possible.
Additionally, car's audio system cannot shuffle the tracks making it worthwhileto preshuffle them.

Downsampling could be done quite easily with something like:
    `find -iname *.mp3 -exec "ffmpeg -i {} {}_copy -b 128" \;`
    
Such approach is ok as long as files's bitrate rests (well) above 128.
Otherwise the files end up being recompressed between similar bitrates which incurs a quality loss on top of the space-quality tradeoff.
One approach would be to manually cherrypick the files already conforming to our standards and compress only the rest.
You could probably identify such files with some music player, file browser by hand playing around the following command:
    `ffprobe -i some.mp3 -show_entries format=bit_rate:format_tags=artist,title 2>/dev/null`

`ffmpeg_downsample.py` relays the conversion work to ffmpeg while making sure that lower quality files are copied directly.
Not to convert files of near-desired quality, `-t` (tolerance) parameter allows indicating how many extra kbps are fine without converting

Besides the syntax is very similar to that of ffmpeg:
    `ffmpeg_downsample -i input.mp3 -o output.mp3 -b desired_kbps -t tolerance_kbps`
To launch the scrpti for a whole folder, invoke:
    `batch_downsample input_dir output_dir`
 


