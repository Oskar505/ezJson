# ezJson
Easier json reading and updating.

At first you must define object with name of your json file: ezJson = EzJson('data.json').
Than you can use METHODS:

read()

read('arrayName', 'objectName')
read('names', 0)

jsonObjectName is optionally. If you enter only arrayName it will print the whole array.
objectName can be int or str.


readAll()

Reads the whole json document.


readObjectValue()

readObjectValue('arrayName', 'objectName', 'name')
readObjectValue('names', 0, 'firstName')

Reads value of object, in this case it would be Alan.


update()

update('arrayName', 'newObject')
update('names', {"firstName":"Rachel", "age":"20"})

Adds a new object to json array.


There is my json file.
The name of this document is data.json.

{
    "names": [
        {
            "firstName": "Alan",
            "age": "22"
        },
        {
            "firstName": "Pat",
            "age": "12"
        },
        {
            "firstName": "Joe",
            "age": "50"
        },
        {
            "firstName": "Piper",
            "age": "16"
        }
    ]
}
