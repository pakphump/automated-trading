def start_cdc_trading(request):
    request_json = request.get_json()
    name = request_json.args.get("name")
    return {"message": "Hello, World!", "name": name}
