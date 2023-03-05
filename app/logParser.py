import statistics
import json

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def evaluate_results(refTemp, refHum, device_type, device_name, read_values):
    if device_type == 'thermometer':
        if abs(refTemp-statistics.mean(read_values)) < 0.5:
            myDeviation = statistics.stdev(read_values)
            if myDeviation < 3:
                return "ultra precise"
            elif myDeviation < 5:
                return "very precise"
            else:
                return "precise"
        else:  
            return "precise"
    elif device_type == 'humidity':
        for i in range(len(read_values)):
            if abs(read_values[i]-refHum) > 1:
                return "discard"
                exit
            else:
                continue
        return "keep"

def main(file_path):
    readValues = []
    global ini_string, device_name, device_type   
    with open(file_path) as file:
        for line in nonblank_lines(file):
            lineList = line.split()
            if lineList[0] == 'reference':
                refTemp = float(lineList[1])
                refHum = float(lineList[2])            
            else:
                if lineList[0] == 'thermometer' or lineList[0] == 'humidity':
                    if len(readValues) < 1:
                        device_type = lineList[0]
                        device_name = lineList[1]
                        ini_string = '''{ '''
                    else:
                        ini_string = ini_string + '''"''' + device_name + '''": ''' + '''"''' + evaluate_results(refTemp, refHum, device_type, device_name, readValues) + '''",'''
                        device_type = lineList[0]
                        device_name = lineList[1]
                        readValues.clear()    
                else:
                    readValues.append(float(lineList[1]))
        ini_string = ini_string + '''"''' + device_name + '''": ''' + '''"''' + evaluate_results(refTemp, refHum, device_type, device_name, readValues) + '''" }'''
        readValues.clear()       
    resp = json.loads(ini_string)
    return resp
                       
       