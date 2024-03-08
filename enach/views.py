import json
import statistics
from django.shortcuts import redirect, render
from easebuzz_lib.easebuzz_payment_gateway import Easebuzz
from django.http import QueryDict

from utils.restful_response import send_response
# Based on API call change the Merchant key and salt key for (initaite payment) on testing
MERCHANT_KEY = "2PBP7IABZ2"
SALT = "DAH88E3UWQ"
ENV = "test"

# create Easebuzz object and send data
easebuzzObj = Easebuzz(MERCHANT_KEY, SALT, ENV)

def initiate_payment(request):
    postDict = {
        'txnid': 'T3SAT0B5OL',
        'firstname': 'jitendra',
        'phone': '1231231235',
        'email': 'jitendra@gmail.com',
        'amount': '1.03',
        'productinfo': 'Apple Mobile',
        'surl': 'http://localhost:8000/response/',
        'furl': 'http://localhost:8000/response/',
        'city': 'aaaa',
        'zipcode': '123123',
        'address2': 'aaaa',
        'state': 'aaaa',
        'address1': 'aaaa',
        'country': 'aaaa',
        'udf1': 'aaaa',
        'udf2': 'aaaa',
        'udf3': 'aaaa',
        'udf4': 'aaaa',
        'udf5': 'aaaa'
    }
    params = QueryDict('', mutable=True)
    params.update(postDict)
    final_response = easebuzzObj.initiatePaymentAPI(params)
    result = json.loads(final_response)
    
    # final_response = easebuzzObj.initiatePaymentAPI(postDict)
    # print(final_response, "test")
    # result = json.loads(final_response)
    if result['status'] == 1:
        # Note: result['data'] contains the payment link.
        return result['data']
    else:
        #return render(request, 'response.html', {'response_data': final_response})
        return send_response(
            status=statistics.HTTP_400_BAD_REQUEST,
            developer_message="Invalid credentials",
        )