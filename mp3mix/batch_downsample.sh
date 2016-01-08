#~/bin/bash

if [ -z $1 ]; then
    echo "Zero parameters provided, two required."
    exit 1
elif [ ! -d $1 ]; then
    echo "$1 is not a directory."
    exit 1
elif [ -z $2 ]; then
    echo "One parameter provided, two required."
    exit 1
elif [ ! -d $2 ]; then
    echo "$2 is not a directory."
    exit 1
fi

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

src_dir=$1
dst_dir=$2

echo "Source dir: ${src_dir}, destination dir: ${dst_dir}"

# Stackoverflow rules
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

for x in $(ls ${src_dir}/*.mp3); 
do
    md5=$(md5sum $x |  grep -o '^[^ ]*')
    # Name without the leading './' - used to be useful, now it's only interesting
    #stripped_name=${x#'./'}
    echo "Converting $x into $md5 to be saved at $DIR"
    python "${DIR}/ffmpeg_downsample.py" -i $x -o "${dst_dir}/${md5}.mp3" -b 128 -t 50; 
done

IFS=$SAVEIFS