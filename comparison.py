import json
import containers
import images
import schema

def containerANDImageIssue(COIM, schema) :
    print(COIM)
    result = ""
    opposite = {"PASS" : "FAIL" , "FAIL" : "PASS"}
    for key in schema.keys():
        if str(COIM[key]) == "<type 'list'>" : 
            for val in COIM[key] :
                result = schema[key].keys()[0] if val in schema[key][schema[key].keys()[0]] else opposite[schema[key].keys()[0]]
                if result == "FAIL": 
                    break
        else :        
            result = schema[key].keys()[0] if (COIM[key] in schema[key][schema[key].keys()[0]]) else opposite[schema[key].keys()[0]]
        print key+ " => ",result

# Actual Values
containerActual = containers.Container().container_param('7a6c6fbce3a1')
imageActual = images.Image().get_image_id('mongo')

# For Container comparisation
print("\n====================CONTAINER===================================\n")
containerANDImageIssue(containerActual, schema.container)

#For Image comparisation
print("\n====================IMAGES======================================\n")
containerANDImageIssue(imageActual, schema.images)

