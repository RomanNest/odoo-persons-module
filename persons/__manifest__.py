{
    "name": "Persons",
    "version": "1.0",
    "category": "Human Resources",
    "summary": "The App to manage persons",
    "depends": ["base", "website"],
    "data": [
        "views/person_views.xml",
    ],
    "assets": {
    "web.assets_frontend": [
        "persons/templates/*.xml"
    ],
},
    "installable": True,
    "application": True,
}
