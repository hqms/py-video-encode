import unittest

from PyEncode import PyEncode


class VideoUtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.video_file_test = './video_test.mp4'
        self.encoder = PyEncode(input_file=self.video_file_test, ffmpeg_dir='/usr/local/bin')

    def test_get_media_info(self):
        expected_result = {
                    "streams": [
                        {
                            "index": 0,
                            "codec_name": "h264",
                            "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
                            "profile": "Constrained Baseline",
                            "codec_type": "video",
                            "codec_time_base": "1/60",
                            "codec_tag_string": "avc1",
                            "codec_tag": "0x31637661",
                            "width": 480,
                            "height": 236,
                            "coded_width": 480,
                            "coded_height": 236,
                            "has_b_frames": 0,
                            "sample_aspect_ratio": "1239:1240",
                            "display_aspect_ratio": "63:31",
                            "pix_fmt": "yuv420p",
                            "level": 21,
                            "chroma_location": "left",
                            "refs": 1,
                            "is_avc": "true",
                            "nal_length_size": "4",
                            "r_frame_rate": "30/1",
                            "avg_frame_rate": "30/1",
                            "time_base": "1/30",
                            "start_pts": 0,
                            "start_time": "0.000000",
                            "duration_ts": 361,
                            "duration": "12.033333",
                            "bit_rate": "646118",
                            "bits_per_raw_sample": "8",
                            "nb_frames": "361",
                            "disposition": {
                                "default": 1,
                                "dub": 0,
                                "original": 0,
                                "comment": 0,
                                "lyrics": 0,
                                "karaoke": 0,
                                "forced": 0,
                                "hearing_impaired": 0,
                                "visual_impaired": 0,
                                "clean_effects": 0,
                                "attached_pic": 0
                            },
                            "tags": {
                                "creation_time": "2013-03-28 21:39:37",
                                "language": "eng",
                                "handler_name": "VideoHandler"
                            }
                        },
                        {
                            "index": 1,
                            "codec_name": "aac",
                            "codec_long_name": "AAC (Advanced Audio Coding)",
                            "profile": "LC",
                            "codec_type": "audio",
                            "codec_time_base": "1/44100",
                            "codec_tag_string": "mp4a",
                            "codec_tag": "0x6134706d",
                            "sample_fmt": "fltp",
                            "sample_rate": "44100",
                            "channels": 2,
                            "channel_layout": "stereo",
                            "bits_per_sample": 0,
                            "r_frame_rate": "0/0",
                            "avg_frame_rate": "0/0",
                            "time_base": "1/44100",
                            "start_pts": 0,
                            "start_time": "0.000000",
                            "duration_ts": 531645,
                            "duration": "12.055442",
                            "bit_rate": "3122",
                            "nb_frames": "521",
                            "disposition": {
                                "default": 1,
                                "dub": 0,
                                "original": 0,
                                "comment": 0,
                                "lyrics": 0,
                                "karaoke": 0,
                                "forced": 0,
                                "hearing_impaired": 0,
                                "visual_impaired": 0,
                                "clean_effects": 0,
                                "attached_pic": 0
                            },
                            "tags": {
                                "creation_time": "2013-03-28 21:39:37",
                                "language": "eng",
                                "handler_name": "SoundHandler"
                            }
                        }
                    ],
                    "format": {
                        "filename": "./video_test.mp4",
                        "nb_streams": 2,
                        "nb_programs": 0,
                        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
                        "format_long_name": "QuickTime / MOV",
                        "start_time": "0.000000",
                        "duration": "12.056000",
                        "size": "990547",
                        "bit_rate": "657297",
                        "probe_score": 100,
                        "tags": {
                            "major_brand": "isom",
                            "minor_version": "512",
                            "compatible_brands": "isomiso2avc1mp41",
                            "creation_time": "2013-03-28 21:39:37",
                            "encoder": "Lavf54.6.100"
                        }
                    }
                }

        res = self.encoder.get_media_info()
        self.maxDiff = None
        self.assertDictEqual(res, expected_result)

    def test_get_video_duration(self):
        duration = 12
        self.assertAlmostEqual(duration, self.encoder.get_video_duration())

    def test_get_video_resolution(self):
        resolution = {'width': 480, 'height': 236}
        self.assertEqual(resolution, self.encoder.get_video_resolution())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
