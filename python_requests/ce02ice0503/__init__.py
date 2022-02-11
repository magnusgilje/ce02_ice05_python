import logging
import azure.functions as func
import sys
import requests
import get_weather_info

sys.path.insert(0,"..")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    region = req.params.get('region')
    if not region:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            region = req_body.get('region')

    if region:
        try:                
            myW = get_weather_info.Get_weather_info(region)
            return func.HttpResponse(myW.description())
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            return func.HttpResponse('Error', status_code=404)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a region (AL,AK,AS,AR,AZ,CA,CO,CT,DE,DC,FL,GA,GU,HI,ID,IL,IN,IA,KS,KY,LA,ME,MD,MA,MI,MN,MS,MO,MT,NE,NV,NH,NJ,NM,NY,NC,ND,OH,OK,OR,PA,PR,RI,SC,SD,TN,TX,UT,VT,VI,VA,WA,WV,WI,WY) in the query string or in the request body for a personalized response.",
             status_code=200
        )
