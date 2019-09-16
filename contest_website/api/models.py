from django.db import models

from .constants import SIZE_ADDRESS_BYTES, SIZE_SIGNATURE_BYTES


class Registrant(models.Model):
    address = models.BinaryField(max_length=SIZE_ADDRESS_BYTES)
    signature = models.BinaryField(max_length=SIZE_SIGNATURE_BYTES)

    def __str__(self) -> str:
        return hex(int.from_bytes(self.address, 'big'))
