from PyEncode import PyEncode

encode = PyEncode(ffmpeg_dir='/usr/local/bin', input_file='./video_test.mp4')
res = encode.get_media_info()
print(res)
