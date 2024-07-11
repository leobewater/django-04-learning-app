from django.core.exceptions import ObjectDoesNotExist
from django.db import models


# Custom field inherits from on PositiveIntegerField
# Auto adding 1 to the last module of the same for_fields such as course
class OrderField(models.PositiveIntegerField):
    # optional for_fields parameter
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    # Override the pre_save method of the PositiveIntegerField
    def pre_save(self, model_instance, add):
        # You use self.attname, which is the attribute name given to the field in the model. If the attribute’s value is different from None, you calculate the order you should give it as follows
        if getattr(model_instance, self.attname) is None:
            # no current value
            # check whether a value already exists for this field in the model instance.
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    # filter by objects with the same field values
                    # for the fields in "for_fields"
                    query = {
                        field: getattr(model_instance, field)
                        for field in self.for_fields
                    }
                    qs = qs.filter(**query)

                # get the order of the last item
                last_item = qs.latest(self.attname)
                value = getattr(last_item, self.attname) + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
