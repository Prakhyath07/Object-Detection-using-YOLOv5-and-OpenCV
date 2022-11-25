from yolov5 import *
import cv2


cap = cv2.VideoCapture("traffic_small.mp4")
modelWeights = "models/yolov5s.onnx"
net = cv2.dnn.readNet(modelWeights)

count =0
while True:
	ret,frame = cap.read()
	if not ret:
		break
	
	count+=1
	if count%3!=0:
		continue

	print(frame.shape)
	
	## create a mask with white pixels
	mask = np.ones(frame.shape,dtype=np.uint8)
	mask.fill(255)

  
	roi = frame[150:,:]
	roi_corners = np.array([[(0,150),(852,150),(852,480),(0,480)]], dtype=np.int32)
	
	# fill the ROI into the mask
	cv2.fillPoly(mask,roi_corners,0)
	
	# applying th mask to original image
	masked_image = cv2.bitwise_or(frame, mask)

	# cv2.polylines(frame,[np.array(area,np.int32)],True,(15,220,10),6)
	# Process image.
	detections = pre_process(masked_image, net)
	img = post_process(frame.copy(), detections)
	
	# img = cv2.bitwise_or(frame, img)
	t, _ = net.getPerfProfile()
	label = 'Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())
	print(label)
	cv2.putText(img, label, (20, 40), FONT_FACE, FONT_SCALE, RED, THICKNESS, cv2.LINE_AA)

	cv2.imshow('Output', img)

	
	
	
	key=cv2.waitKey(10)
	if key==27:
		break
	

# if __name__ == '__main__':
# 	# Load class names.
# 	classesFile = "coco.names"
# 	classes = None
# 	with open(classesFile, 'rt') as f:
# 		classes = f.read().rstrip('\n').split('\n')

# 	# Load image.
# 	frame = cv2.imread('sample.jpg')

# 	# Give the weight files to the model and load the network using them.
# 	modelWeights = "models/yolov5s.onnx"
# 	net = cv2.dnn.readNet(modelWeights)

# 	# Process image.
# 	detections = pre_process(frame, net)
# 	img = post_process(frame.copy(), detections)