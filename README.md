# Datamosh

Datamosh is a python script for datamoshing MPEG4-encoded AVI videos. 

Here's an example of a datamoshed video I found on the internet!

https://www.youtube.com/watch?v=sAAMYkcZqkE

## Getting Started

These instructions will get you the project up and running on your local mac. See `Running Datamosh` for notes on how to datamosh a video.

### Python3

Follow these next set of instructions if your mac does not have Python 3 installed.

If you dont have hombrew installed, open your terminal and run:
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
```

Then install Python3 using:
```
$ brew install python3
```

### ffmpeg

Follow these next set of instructions if your mac does not have ffmpeg installed.

If you dont have hombrew installed, open your terminal and run:
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
```

Then install ffmpeg, by running the following in the terminal:
```
$ brew install ffmpeg
```

End with an example of getting some data out of the system or using it for a little demo

## Running Datamosh

To datamosh a video, run the following command in your terminal once you cd into the directory
```
$ python3 datamosh.py [video file name]
```
The datamoshed video will be in a new directory: `datamoshed_videos/`
