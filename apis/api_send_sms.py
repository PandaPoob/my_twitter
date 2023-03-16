from bottle import post, request, response
import requests

@post("/api-send-sms")
def _():
    try:
        phone_number = request.forms.get("phone_number", "")
        text_msg = request.forms.get("text_msg", "")
        if not phone_number:
            raise Exception("Must have phone number")
        if not text_msg:
            raise Exception("Must have text message")
        url = 'https://smses.eu.pythonanywhere.com/api-send-sms'
        payload = {"user_api_key": 'ec2ede3ce8e64245be1fb58aff56c458', "sms_message": text_msg, "sms_to_phone": phone_number}
        r = requests.post(url, data=payload)
        #print(type(r.status_code))
        #if r.status_code != 200:
            #print(r.text)
            #raise Exception(str(r.text))
        return {"info": {"phone_number": phone_number, "text_msg": text_msg}}
    except Exception as ex:
        print(ex)
        response.status = 400
        return {"info": str(ex)}
    finally:
        pass