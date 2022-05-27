import cv2
import os
import glob

def extract_frames_from_single_video(video_path, save_folder):
    """
    : video_path: location of the video
    : save_folder: folder to save extracted frames
    Creates a seperate folder for frames. 
    Picks one frame every 10 frames. Creates 180 images
    """

    video = cv2.VideoCapture(video_path)

    current_frame = 0

    while(True):
        ret, frame = video.read()

        if not os.path.exists(save_folder + '/' + str(video_path[-15:-4]) + '/'):
            print("Creating Save directory for frame: ", video_path[-15:-4])
            os.makedirs(save_folder + '/' + str(video_path[-15:-4]) + '/')

        if ret:
            current_frame += 1
            if (current_frame % 200) == 0 and current_frame < 1300:

                frame_name = save_folder + '/' + str(video_path[-15:-4])+ '/' + str(video_path[-15:-4]) + '_' + str(current_frame//200) + '.jpg'
                print("Creating frame: " + frame_name)

                cv2.imwrite(frame_name, frame)
        
        else:
            break


def extract_frames():
    """
    Extract frames from surgtoolloc2022_dataset folder and saves 180 frames form \
    every video in data folder
    """

    video_list = []

    video_folder = './surgtoolloc2022_dataset/_release/training_data/video_clips/*.mp4'
    video_save_path = './data'

    for file in glob.iglob(video_folder, recursive=True):
        video_list.append(file)

    for video_path in video_list:
        extract_frames_from_single_video(video_path, video_save_path)

extract_frames()