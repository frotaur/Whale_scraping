import cv2
import os
viddir = "Whale_videos"
videos = os.listdir("Whale_videos")
print(videos)
for vid in videos:
	name,ext = os.path.splitext(vid)
	print("ext : {}".format(ext))
	if ext==".mp4":
		vidcap = cv2.VideoCapture(os.path.join(viddir,vid))
		fps = vidcap.get(cv2.CAP_PROP_FPS)
		print("FRP :",fps)
		print(vidcap.isOpened())
		success,image = vidcap.read()
		print(success)
		count=0
		cv2.imwrite(os.path.join(viddir,"pics","{}{}.jpg".format(name[:min(6,len(name)-1)],count//60)),image)
		for i in range(1):
			if(count % 60==0):
				cv2.imwrite(os.path.join(viddir,"pics","{}{}.jpg".format(name[:min(6,len(name)-1)],count//60)),image)
			success,image=vidcap.read()
			print("Read")
			count+=1
