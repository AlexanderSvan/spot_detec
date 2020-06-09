from moviepy.video.io.bindings import mplfig_to_npimage
from moviepy.editor import VideoFileClip, VideoClip, clips_array, TextClip
import moviepy.editor as mpy

video4 = VideoFileClip("/media/data/Jan/20191205 - ONE-HNE/GIFs/well 40.gif",  audio=False)
video3 = VideoFileClip("/media/data/Jan/20191205 - ONE-HNE/GIFs/well 31.gif",  audio=False)
video2 = VideoFileClip("/media/data/Jan/20191205 - ONE-HNE/GIFs/well 16.gif",  audio=False)
video1 = VideoFileClip("/media/data/Jan/20191205 - ONE-HNE/GIFs/well 7.gif",  audio=False)



txt=TextClip('10 ug/ml ONE', color='white', fontsize=50, stroke_color='black').set_position(("center","top")).set_duration(video4.duration)
video4=mpy.CompositeVideoClip([video4,txt])
txt=TextClip('1 ug/ml ONE', color='white', fontsize=50, stroke_color='black').set_position(("center","top")).set_duration(video4.duration)
video3=mpy.CompositeVideoClip([video3,txt])
txt=TextClip('0.1 ug/ml ONE', color='white', fontsize=50, stroke_color='black').set_position(("center","top")).set_duration(video4.duration)
video2=mpy.CompositeVideoClip([video2,txt])
txt=TextClip('0.01 ug/ml ONE', color='white', fontsize=50, stroke_color='black').set_position(("center","top")).set_duration(video4.duration)
video1=mpy.CompositeVideoClip([video1,txt])


finalclip = mpy.clips_array([[clip.margin(2, color=[255,255,255]) for clip in 
                              [video1.resize(0.6) ,video2.resize(0.6) ,video3.resize(0.6), video4.resize(0.6)]]])
finalclip.write_videofile("ONE_inhib.mp4", fps=10)

"""
HNE
"""

video1 = VideoFileClip("/media/data/Jan/20191205 - ONE-HNE/GIFs/well 55.gif",  audio=False)
video2 = VideoFileClip("/media/data/Jan/20191205 - ONE-HNE/GIFs/well 62.gif",  audio=False)
video3 = VideoFileClip("/media/data/Jan/20191205 - ONE-HNE/GIFs/well 77.gif",  audio=False)
video4 = VideoFileClip("/media/data/Jan/20191205 - ONE-HNE/GIFs/well 84.gif",  audio=False)



txt=TextClip('0.01 ug/ml HNE', color='white', fontsize=50, stroke_color='black').set_position(("center","top")).set_duration(video4.duration)
video1=mpy.CompositeVideoClip([video1,txt])
txt=TextClip('0.1 ug/ml HNE', color='white', fontsize=50, stroke_color='black').set_position(("center","top")).set_duration(video4.duration)
video2=mpy.CompositeVideoClip([video2,txt])
txt=TextClip('1 ug/ml HNE', color='white', fontsize=50, stroke_color='black').set_position(("center","top")).set_duration(video4.duration)
video3=mpy.CompositeVideoClip([video3,txt])
txt=TextClip('10 ug/ml HNE', color='white', fontsize=50, stroke_color='black').set_position(("center","top")).set_duration(video4.duration)
video4=mpy.CompositeVideoClip([video4,txt])


finalclip = mpy.clips_array([[clip.margin(2, color=[255,255,255]) for clip in 
                              [video1.resize(0.6) ,video2.resize(0.6) ,video3.resize(0.6), video4.resize(0.6)]]])
finalclip.write_videofile("HNE_inhib.mp4", fps=10)
