from rest_framework import serializers
from .models import ItemModel, Comment,User


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'


class AddCommentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=True)
    body = serializers.CharField(max_length=500, required=True)
    item_id = serializers.IntegerField(required=True)

    def validate(self, data):
        user = self.context['user']
        user_obj = User.objects.get(username=user)
        item_id_list = []
        for i in ItemModel.objects.values_list('id'):
            item_id_list.append(i[0])
        if data['item_id'] in item_id_list:
            Comment.objects.create(
                user_id=user_obj.id,
                ItemModel_id=data['item_id'],
                title=data['title'],
                body=data['body']
            )
        else:
            raise serializers.ValidationError("this item dosnt exist!")
        return data
