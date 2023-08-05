from rest_framework.serializers import ModelSerializer
from todo_app.models import Todo

class ReadTodoListSerializer(ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('id', 'title', 'completed', 'updated_at')