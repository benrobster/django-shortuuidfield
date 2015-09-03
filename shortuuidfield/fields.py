import shortuuid
import six
import sys
from django.db.models import CharField


class ShortUUIDField(CharField):
    """
    A field which stores a Short UUID value in base57 format. This may also have
    the Boolean attribute 'auto' which will set the value on initial save to a
    new UUID value (calculated using shortuuid's default (uuid4)). Note that while all
    UUIDs are expected to be unique we enforce this with a DB constraint.
    """

    def __init__(self, auto=True, *args, **kwargs):
        self.auto = auto
        # We store UUIDs in base57 format, which is fixed at 22 characters.
        kwargs['max_length'] = 22
        if auto:
            # Do not let the user edit UUIDs if they are auto-assigned.
            kwargs['editable'] = False
            kwargs['blank'] = True
           # kwargs['unique'] = True  # if you want to be paranoid, set unique=True in your instantiation of the field.

        super(ShortUUIDField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        """
        This is used to ensure that we auto-set values if required.
        See CharField.pre_save
        """
        value = super(ShortUUIDField, self).pre_save(model_instance, add)
        if self.auto and not value:
            # Assign a new value for this attribute if required.
            value = six.text_type(shortuuid.uuid())
            setattr(model_instance, self.attname, value)
        return value

    def formfield(self, **kwargs):
        if self.auto:
            return None
        return super(ShortUUIDField, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [r"^shortuuidfield\.fields\.ShortUUIDField"])
except ImportError:
    pass
