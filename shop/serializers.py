from rest_framework import serializers
from .models import ItemModel, Comment, User, Cart, CartItem


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
    items_list = serializers.ListField\
        (child=serializers.ListField(child=serializers.IntegerField(), required=True, allow_null=False, min_length=1,
                                     max_length=2), required=True, allow_null=False, min_length=1)

    # item_id = serializers.IntegerField(required=True)
    # item_count = serializers.IntegerField(required=True)

    def validate(self, data):
        user = self.context['user']
        user_obj = User.objects.get(username=user)
        user_cart, _ = Cart.objects.get_or_create(user=user_obj)
        for i in range(len(data['items_list'])):
            item_id = data['items_list'][i][0]
            count = data['items_list'][i][1]
            # print(item_id)
            last_obj = CartItem.objects.filter(item_id=item_id, user=user_obj)
            if last_obj:
                last_count = last_obj.first().count
            else:
                last_count = 0
            old_item_count = ItemModel.objects.get(id=item_id).count
            print(last_count)
            if old_item_count - count >= 0:
                if last_obj:
                    CartItem.objects.filter(item_id=item_id, user=user_obj).update(count=last_count+count)
                else:
                    CartItem.objects.create(user=user_obj, cart=user_cart, item_id=item_id, count=count)
                ItemModel.objects.filter(id=item_id).update\
                    (count=old_item_count - count)
            else:
                raise serializers.ValidationError("we dont have enough item for you!")

        # item_id_list = []
        # old_item_count = ItemModel.objects.get(id=data['item_id']).count
        # for i in ItemModel.objects.values_list('id'):
        #     item_id_list.append(i[0])
        # if data['item_id'] in item_id_list:
        #     if old_item_count - (data['item_count']) >= 0:
        #         ItemModel.objects.filter(id=data['item_id']).update\
        #             (count=old_item_count - data['item_count'])
        #         Cart.objects.get_or_create(user=user_obj,
        #                                    item_id=data['item_id'],
        #                                    count=data['item_count']
        #                                    )
        #     else:
        #         raise serializers.ValidationError("we dont have enough item for you!")
        return data
