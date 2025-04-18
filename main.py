def start_cdc_trading(request):
    request_json = request.get_json()

    print(request_json)
    return {"message": "Hello, World!", "name": "str"}
