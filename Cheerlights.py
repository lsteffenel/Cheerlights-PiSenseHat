from sense_hat import SenseHat
import sys
import thingspeak
import json
import struct

ch = thingspeak.Channel(1417)

results = ch.get({'results': 1}) // get json from Thingspeak

x = json.loads(results)

rgbstr=x['feeds'][0]['field2'] // gets the #RGB code
str=rgbstr[1:]  // extracts the #
print (str)

#convert hex RGB into int [R,G,B]
#struct.unpack('BBB',str.decode('hex')) // Python 2.7
rgb = struct.unpack('BBB',bytes.fromhex(str))   // Python 3

print(rgb)

sense = SenseHat()
a = int (rgb[0])
b = int (rgb[1])
c = int (rgb[2])
X = [a, b, c] 
print (X)

mark = [
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
]

sense.set_pixels(mark)
