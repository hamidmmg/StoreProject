from rest_framework import serializers
from .models import ItemModel, Comment, User, Cart


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


class AddToCartSerializer(serializers.Serializer):
    item_id = serializers.IntegerField(required=True)
    item_count = serializers.IntegerField(required=True)

    def validate(self, data):
        user = self.context['user']
        user_obj = User.objects.get(username=user)
        item_id_list = []
        old_item_count = ItemModel.objects.get(id=data['item_id']).count
        for i in ItemModel.objects.values_list('id'):
            item_id_list.append(i[0])
        if data['item_id'] in item_id_list:
            if old_item_count - (data['item_count']) >= 0:
                ItemModel.objects.filter(id=data['item_id']).update\
                    (count=old_item_count - data['item_count'])
                Cart.objects.get_or_create(user=user_obj,
                                           item_id=data['item_id'],
                                           count=data['item_count']
                                           )
            else:
                raise serializers.ValidationError("we dont have enough item for you!")
        return data
