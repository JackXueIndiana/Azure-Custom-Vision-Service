import http.client, urllib.request, urllib.parse, urllib.error
import time
import cv2
import json

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Prediction-key': 'b6d0387b81fb415e851b8b4a92f68419',
}

params = urllib.parse.urlencode({
    # Request parameters
    'iterationId': 'b453c1ce-ec22-4d3a-a01f-ef691eaaccf5'
})

try:
    t0 = time.time()
    filename = "C:\\Users\\xinxue\\Desktop\\positiveExamples\\ABC2016-11-28_150251.png"
    
    with open(filename, "rb") as imageFile:
        f = imageFile.read()
        
        b = bytearray(f)
  
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v1.0/Prediction/<Your Key>/image?%s" % params, b, headers)
        response = conn.getresponse()
        data = response.read()
        
        print(data)
        jdata = json.loads(data)
        returnTag = jdata['Predictions'][0]['Tag']
        if returnTag == 'Positive':
            image = cv2.imread(filename,0)
            cv2.imshow("Input", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(image)
            cv2.circle(image, maxLoc, 50, (255, 0, 0), 2)
            cv2.imshow("Found the location", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print(maxLoc)
        else:
            print('Negative so do nothing.')
            
        conn.close()
        
    t1 = time.time()
    t = t1-t0
    print(t)
except Exception as e:
    #print("[Errno {0}] {1}".format(e.errno, e.strerror))
    print('Something wrong')
