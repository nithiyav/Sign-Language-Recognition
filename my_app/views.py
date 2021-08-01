import pathlib
import requests
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from labels import *
import os

def normalize(img):

    img = cv2.resize(img, (224, 224))
    img = img / 255
    img = np.expand_dims(img, axis=0)
    return img


class PredictionAPIView(APIView):

    def post(self, request, data = None):

        image = request.data['image']

        folder = 'media/uploads/'

        fs = FileSystemStorage(location = folder)
        name = fs.save(image.name, image)

        filepath = folder + name
        print("File Saved in:",filepath)

        input_image = cv2.imread(filepath)

        input_image = normalize(input_image)

        print("Loading model....")
        model = tf.keras.models.load_model('trained-models/mobilenet/model.h5')
        print("Model Loaded Successfully!!")

        prediction = model.predict([input_image])
        prediction = np.argmax(prediction, -1)[0]

        prediction = labels[prediction]

        prediction_path = 'media/labels/' + prediction + '.jpg'

        prediction = "The Predicted Alphabet is: "+str(prediction)

        data = {"image": filepath,
                "prediction": prediction,
                "prediction_path": prediction_path}

        serializer = PredictionSerialzier(data = data)

        if serializer.is_valid():
            print("Sucess\n")
            #serializer.save()

        file_to_rem = pathlib.Path(filepath)
        file_to_rem.unlink()

        return Response(serializer.data, status = status.HTTP_201_CREATED)

def home(request):
    return render(request, 'test.html')

def result(request):
    return render(request, 'results.html')

def predict(request):

    if request.method == 'POST':

        image = request.FILES['image']

        folder = 'media/uploads/'

        fs = FileSystemStorage(location=folder)
        name = fs.save(image.name, image)

        filepath = folder + name
        print("File Saved in:", filepath)

        input_image = cv2.imread(filepath)

        input_image = normalize(input_image)

        print("Loading model....")
        model = tf.keras.models.load_model('trained-models/mobilenet/model.h5')
        print("Model Loaded Successfully!!")

        prediction = model.predict([input_image])
        prediction = np.argmax(prediction, -1)[0]

        prediction = labels[prediction]

        prediction_path = 'media/labels/' + prediction + '.jpg'

        prediction = "The Predicted Alphabet is: " + str(prediction)

        data = {"image": filepath,
                "prediction": prediction,
                "prediction_path": prediction_path}

        serializer = PredictionSerialzier(data=data)

        if serializer.is_valid():
            print("Sucess\n")
            # serializer.save()

        file_to_rem = pathlib.Path(filepath)
        file_to_rem.unlink()
        print(data)

        return render(request, 'results.html', {'data': data})

