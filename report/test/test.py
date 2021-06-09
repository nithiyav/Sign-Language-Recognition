import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('model.h5')

labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
		'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		
		
cap = cv2.VideoCapture(0)

while True:
	
	ret, frame = cap.read()
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
	test = cv2.resize(frame, (224, 224))
	test = test/255.0
	font = cv2.FONT_HERSHEY_SIMPLEX
	test = np.expand_dims(test, axis = 0)

	prediction = "Prediction "+str(labels[np.argmax(model.predict(test))])

	cv2.putText(frame, prediction, (10, 30), font, 1, (0, 0, 255), 2)
	
	cv2.imshow('Prediction',frame)
	

cap.release()
cap.destroyAllWindows()
	