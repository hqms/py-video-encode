class PyEncode(object):
    pass_param = {
        '1PASS': '{ffmpeg} -y -i {infile} -c:v {vcodec} -preset {preset} -threads 3 -b:v {vbitrate} -profile:v'
                 ' {vprofile} -level:v {vlevel} -c:a {acodec} -b:a {abitrate} -ss {starttime} -to {stoptime}'
                 ' -pix_fmt yuv420p -strict -2 -vf scale="{scale}" "{outfile}"'
    }

    MEDIA_INFO_CMD = '{ffprobe} -v quiet -print_format json -show_format -show_streams {infile}'
