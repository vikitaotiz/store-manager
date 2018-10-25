schema = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "number"},
        "name" : {"$ref" : "#/definitions/non-empty-string"},
        "category" : {"$ref" : "#/definitions/non-empty-string"},
        "quantity" : {"type" : "number"},
        "price" : {"type" : "number"}
    },
    "definitions" : {
        "non-empty-string" : {
            "type" : "string",
            "minLength" : 1 
        }
    }
}