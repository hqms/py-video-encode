import json
import shlex

import subprocess


class PyEncode(object):
    pass_param = {
        '1PASS': '{ffmpeg} -y -i {infile} -c:v {vcodec} -preset {preset} -threads 3 -b:v {vbitrate} -profile:v'
                 ' {vprofile} -level:v {vlevel} -c:a {acodec} -b:a {abitrate} -ss {starttime} -to {stoptime}'
                 ' -pix_fmt yuv420p -strict -2 -vf scale="{scale}" "{outfile}"'
    }

    media_info_cmd = '{ffprobe} -v quiet -print_format json -show_format -show_streams {input_file}'

    media_info = None

    def __init__(self, **kwargs):
        self.settings = kwargs

    def get_media_info(self):
        cmd = self.media_info_cmd.format(ffprobe=self.settings['ffmpeg_dir'] + '/ffprobe', input_file=self.settings['input_file'])
        args = shlex.split(str(cmd))

        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        out, err = p.communicate()
        self.media_info = json.loads(out.decode("utf-8"))

        if err is not None:
            return False
        else:
            return self.media_info

    def get_video_duration(self):
        if self.media_info is None:
            self.media_info = self.get_media_info()

        return int(float(self.media_info['format']['duration']))

    def get_video_resolution(self):
        if self.media_info is None:
            self.media_info = self.get_media_info()

        for stream in self.media_info['streams']:
            if 'width' in stream:
                return {'width': stream['width'], 'height': stream['height']}

        return {}
