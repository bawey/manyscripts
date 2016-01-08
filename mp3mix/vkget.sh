#!/bin/bash

# Used with the following Klipper action:
# Regular expression: ^https?://.+mp3
# Command: /path/to/vkget.sh %s ~/Downloads/vkontakte

dir=$2
if [ -z "${2}" ]; then
    dir=~/Downloads/vk
fi

echo "Target DIR is ${dir}"

if [ ! -d $dir ]; then
    echo "Directory ${dir} does not exist"
    mkdir ${dir}
fi

link=$1

if [ -z $1 ]; then
    echo "Nothing to do!"
    exit
fi

link=$(echo $1 | grep -P "http[^?]+" -o)

filename=$(echo $link | grep -P "[^/]+mp3" -o)

echo "Downloading $filename from $name"

wget $link -O $dir/$filename
