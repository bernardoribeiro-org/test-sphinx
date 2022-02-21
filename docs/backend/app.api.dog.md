# app.api.dog module

Dogs endpoints


### _class_ app.api.dog.Dog(api=None, \*args, \*\*kwargs)
Bases: `flask_restx.resource.Resource`

defines Dog GET by id endpoint


#### get(id)
Fetch a dog given its identifier


#### methods(_ = {'GET'_ )
A list of methods this view can handle.


### _class_ app.api.dog.DogList(api=None, \*args, \*\*kwargs)
Bases: `flask_restx.resource.Resource`

defines Dog list endpoint


#### get()
List all dogs


#### methods(_ = {'GET'_ )
A list of methods this view can handle.
