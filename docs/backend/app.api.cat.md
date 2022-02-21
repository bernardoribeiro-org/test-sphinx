# app.api.cat module

cats endpoints


### _class_ app.api.cat.Cat(api=None, \*args, \*\*kwargs)
Bases: `flask_restx.resource.Resource`

defines Cat GET by id endpoint


#### get(id)
Fetch a cat given its identifier


#### methods(_ = {'GET'_ )
A list of methods this view can handle.


### _class_ app.api.cat.CatList(api=None, \*args, \*\*kwargs)
Bases: `flask_restx.resource.Resource`

defines Cat list endpoint


#### get()
List all cats


#### methods(_ = {'GET'_ )
A list of methods this view can handle.
