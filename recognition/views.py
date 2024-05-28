# recognition/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.base import ContentFile
import face_recognition
import numpy as np
import pickle

from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def add_new_user(request):
    name = request.data.get('name')
    info = request.data.get('info')
    image_file = request.FILES['image']
    
    image = face_recognition.load_image_file(image_file)
    encodings = face_recognition.face_encodings(image)
    
    if len(encodings) == 0:
        return Response({"detail": "No face found in the image"}, status=status.HTTP_400_BAD_REQUEST)
    
    encoding = encodings[0]
    encoding_pickle = pickle.dumps(encoding)
    
    user = User(name=name, info=info, image=image_file, encoding=encoding_pickle)
    user.save()
    
    return Response({"id": user.id, "name": user.name, "info": user.info}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def get_id_info(request):
    results = []
    images = request.FILES.getlist('images')
    
    for image_file in images:
        image = face_recognition.load_image_file(image_file)
        face_encodings = face_recognition.face_encodings(image)
        
        for face_encoding in face_encodings:
            users = User.objects.all()
            known_encodings = [pickle.loads(user.encoding) for user in users]
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index] and (1 - face_distances[best_match_index]) >= 0.6:
                user = users[best_match_index]
                results.append({"id": user.id, "name": user.name, "info": user.info})
            else:
                results.append({"message": "Person ID info doesn't exist for that image"})
    
    return Response({"results": results})

@api_view(['GET'])
def get_all(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
