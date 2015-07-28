#~/bin/bash

if [ -z "$1" ] || [  -z "$2" ]; then
    echo "Two directories have to be provided as parameters: source and destination."
    exit 1
fi

src_dir=$1
dst_dir=$2

echo "Sourece dir: ${src_dir}, destination dir: ${dst_dir}"

# Stackoverflow rules
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

for x in "${1}/*.mp3"; 
do
    #md5=$(md5sum $x |  grep -o '^[^ ]*')
    # Name without the leading './' - used to be useful, now it's only interesting
    #stripped_name=${x#'./'}
    echo $x
    #python "${DIR}/ffmpeg_downsample.py" -i $x -o "${dst_dir}/${md5}" -b 128 -t 50; 
done