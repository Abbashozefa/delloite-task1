import json, unittest, datetime
import math

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    jsonObject["location"]= {
        "country": "japan",
        "city": "tokyo",
        "area": "keiyō-industrial-zone",
        "factory": "daikibo-factory-meiyo",
        "section": "section-1"
    }
    jsonObject["data"]= {
        "status": "healthy",
        "temperature": 22
    }
    jsonObject.pop("operationStatus")
    jsonObject.pop("temp")
   
  

    return jsonObject


def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    jsonObject["deviceID"]= "dh28dslkja"
    jsonObject["deviceType"]= "LaserCutter"
    jsonObject["location"]= {
        "country": "japan",
        "city": "tokyo",
        "area": "keiyō-industrial-zone",
        "factory": "daikibo-factory-meiyo",
        "section": "section-1"
    }
    jsonObject.pop("device")
    jsonObject.pop("country")
    jsonObject.pop("city")
    jsonObject.pop("area")
    jsonObject.pop("factory")
    jsonObject.pop("section")
    
    date = datetime.datetime.strptime(jsonObject["timestamp"], '%Y-%m-%dT%H:%M:%S.%fZ')
    jsonObject["timestamp"] = int((date - datetime.datetime(1970, 1, 1)).total_seconds()*1000)
    
    
    
    

    return jsonObject
  

def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)
    
    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()
