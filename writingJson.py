import json

curve_dict = {
    "diamondStick" : [[0.0, 0.0, 0.0], 
                      [0.0, 0.0, 5.0], 
                      [0.0, 1.0, 6.0], 
                      [0.0, 0.0, 7.0], 
                      [0.0, -1.0, 6.0], 
                      [0.0, 0.0, 5.0], 
                      [1.0, 0.0, 6.0], 
                      [0.0, 0.0, 7.0], 
                      [-1.0, 0.0, 6.0], 
                      [0.0, 0.0, 5.0], 
                      [-1.0, 0.0, 6.0], 
                      [0.0, 1.0, 6.0], 
                      [1.0, 0.0, 6.0], 
                      [0.0, -1.0, 6.0], 
                      [-1.0, 0.0, 6.0]],
    "crossHeadStick" : [[0.0, 0.0, 0.0], 
                        [0.0, 0.0, 5.0], 
                        [-1.0, 0.0, 6.0], 
                        [0.0, 0.0, 7.0], 
                        [1.0, 0.0, 6.0], 
                        [0.0, 0.0, 5.0], 
                        [0.0, 0.0, 7.0], 
                        [1.0, 0.0, 6.0], 
                        [-1.0, 0.0, 6.0]],
}

filePath = "C:\\Users\\Yourim Kim\\Documents\\maya\\2022\\scripts\\mayaTools\\curveShapeData.json"

with open(filePath, "w") as json_file:
    json.dump(curve_dict, json_file, sort_keys = True, indent=4)