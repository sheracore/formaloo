from rest_framework import serializers
from .models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
        read_only_fields = ('verification_status', 'user', 'created_at', 'updated_at')

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        return super().create(validated_data)
