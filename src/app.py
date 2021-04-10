import json
import numpy as np

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello Numpy!",
            "test"   : "np.array([1,2,3]).tolist()",
            "result" :  np.array([1,2,3]).tolist()
        }),
    }