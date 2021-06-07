from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from labels import *

def normalize(img):

    img = cv2.resize(img, (50, 50))
    img = img / 255
    img = np.expand_dims(img, axis=0)
    return img


class PredictionAPIView(APIView):

    def post(self, request):

        image = request.data['image']

        folder = 'static/uploads/'

        fs = FileSystemStorage(location = folder)
        name = fs.save(image.name, image)

        filepath = folder + name
        print("File Saved in:",filepath)

        input_image = cv2.imread(filepath)

        input_image = normalize(input_image)

        print("Loading model....")
        model = tf.keras.models.load_model('trained-models/model.h5')
        print("Model Loaded Successfully!!")

        prediction = model.predict([input_image])
        prediction = np.argmax(prediction, -1)[0]

        prediction = labels[prediction]

        prediction_path = 'static/predictions/'+prediction+'.jpg'

        return Response({"Status": "Sucess"})