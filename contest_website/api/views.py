from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

from rest_framework.decorators import api_view

from eth_utils import is_address, to_canonical_address, to_checksum_address

from .models import Registrant


@api_view(['POST'])
def register(request):
    address_key = "address"
    if address_key not in request.POST:
        return HttpResponseBadRequest("`address` not found")
    address = request.POST[address_key]
    if not is_address(address):
        return HttpResponseBadRequest(f"`address` is not in the correct format, address={address}")
    canonical_address = to_canonical_address(address)
    try:
        Registrant.objects.get(address=canonical_address)
    except Registrant.DoesNotExist:
        pass
    else:
        return HttpResponseBadRequest(f"{address} has been registered before")
    r = Registrant(address=canonical_address)
    r.save()
    print(f"{address} is successfully registered")
    return HttpResponse()


@api_view(['GET'])
def get_registrants(request):
    objects = Registrant.objects.all()
    # TODO: Score and sorting.
    # TODO: To get the score, we need a query API.
    #   This API might directly fetch the score from infura,
    #   or get the result from a prepared dedicated database.
    result_list = [
        to_checksum_address(o.address)
        for o in objects
    ]
    return JsonResponse(result_list, safe=False)
