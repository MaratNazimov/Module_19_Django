import io
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('title', 'cat_id')

class UserModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class UserSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()


from rest_framework.renderers import JSONRenderer

def encode():
    model = UserModel('Tom', 'TestTest')
    model_sr = UserSerializer(model)
    print(model_sr, type(model_sr))
    json = JSONRenderer().render(model_sr.data)
    print(json, type(json))

from rest_framework.parsers import JSONParser

def decode():
    sr = io.BytesIO(b'{"title":"Tom","content":"TestTest"}')
    data = JSONParser().parse(sr)
    serializer = UserSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)

