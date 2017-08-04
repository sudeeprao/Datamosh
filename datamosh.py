start_sec = 0
start_effect_sec = 0
end_effect_sec   = 10
end_sec = 60
repeat_p_frames = 15
output_width = 480
fps = 20

output_directory = 'datamoshed_videos'

import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 2:
	print('Please use Datamosh with Python version 3.2')
	sys.exit()

import os
import argparse
import subprocess

# make sure the video exists
def quit_if_no_video_file(video_file):
	if not os.path.isfile(video_file):
		raise argparse.ArgumentTypeError("Couldn't find {}. You might want to check the file name??".format(video_file))
	else:
		return(video_file)

# make sure the output directory exists
def confirm_output_directory(output_directory):
	if not os.path.exists(output_directory): os.mkdir(output_directory)

	return(output_directory)

parser = argparse.ArgumentParser() 

parser.add_argument('input_video', type=quit_if_no_video_file, help="File to be moshed")
parser.add_argument('--start_sec',        default = start_sec,        type=float, help="Time the video starts on the original footage's timeline. Trims preceding footage.")
parser.add_argument('--end_sec',    	  default = end_sec,          type=float, help="Time on the original footage's time when it is trimmed.")
parser.add_argument('--start_effect_sec', default = start_effect_sec, type=float, help="Time the effect starts on the trimmed footage's timeline. The output video can be much longer.")
parser.add_argument('--end_effect_sec',   default = end_effect_sec,   type=float, help="Time the effect ends on the trimmed footage's timeline.")
parser.add_argument('--repeat_p_frames',  default = repeat_p_frames,  type=int,   help="If this is set to 0 the result will only contain i-frames. Possibly only a single i-frame.")
parser.add_argument('--output_width',     default = output_width,     type=int,   help="Width of output video in pixels. 480 is recommended for social media friendly posts. Datamosh hates odd number of pixels.")
parser.add_argument('--fps',              default = fps,              type=int,   help="The number of frames per second the initial video is converted to before datamoshing.")
parser.add_argument('--output_dir',       default = output_directory, type=confirm_output_directory, help="Output directory")

locals().update( parser.parse_args().__dict__.items() )

if output_width % 2 != 0: output_width += 1

end_effect_hold = end_effect_sec - start_effect_sec
start_effect_sec = start_effect_sec - start_sec

end_effect_sec = start_effect_sec + end_effect_hold

print('start time from original video: ',str(start_sec))
print('end time from original video: ',str(end_sec))
print('mosh effect applied at: ',str(start_effect_sec))
print('mosh effect stops being applied at: ',str(end_effect_sec))

if start_effect_sec > end_effect_sec:
	print("Cant datamosh because --start_effect_sec begins after --end_effect_sec")
	sys.exit()

input_avi =  os.path.join(output_dir, 'datamoshing_input.avi')
output_avi = os.path.join(output_dir, 'datamoshing_output.avi')
output_video = os.path.join(output_dir, 'moshed_{}.mp4'.format(file_name))


# where the magic happens

try:
	null = open("/dev/null", "w")
	#try and open FFMPEG
	subprocess.Popen("ffmpeg", stdout=null, stderr=null)
	null.close()

except OSError:
	print("ffmpeg was not found. Please check the README.md and install it")
	sys.exit()

subprocess.call('ffmpeg -loglevel error -y -i ' + input_video + ' ' +
				' -crf 0 -pix_fmt yuv420p -r ' + str(fps) + ' ' +
				' -ss ' + str(start_sec) + ' -to ' + str(end_sec) + ' ' +
				input_avi, shell=True)

in_file  = open(input_avi,  'rb')
out_file = open(output_avi, 'wb')

in_file_bytes = in_file.read()


in_file.close()
out_file.close()

subprocess.call('ffmpeg -loglevel error -y -i ' + output_avi + ' ' +
				' -crf 18 -pix_fmt yuv420p -vcodec libx264 -acodec aac -r ' + str(fps) + ' ' +
				' -vf "scale=' + str(output_width) + ':-2:flags=lanczos" ' + ' ' +
				#' -ss ' + str(start_sec) + ' -to ' + str(end_sec) + ' ' +
				output_video, shell=True)
os.remove(input_avi)
os.remove(output_avi)


