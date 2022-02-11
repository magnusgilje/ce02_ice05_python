import logging
import azure.functions as func
import sys
import hailstone

sys.path.insert(0,"..")


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    n = req.params.get('n')
    if not n:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            n = req_body.get('n')

    if n:
        try:                
            myH = hailstone.Hailstone(int(n))
            return func.HttpResponse(myH.plot())
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            return func.HttpResponse('Error', status_code=404)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass an n in the query string or in the request body for a personalized response.",
             status_code=200
        )
