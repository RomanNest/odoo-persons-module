{
    "name": "Persons",
    "version": "1.0",
    "summary": "The App to manage persons",
    "description": "This is my custom Persons module for test",
    "category": "Human Resources",
    "depends": ["base", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/person_views.xml",
        "templates/website_persons_template.xml",
        "templates/persons_form_template.xml",
    ],
    "installable": True,
    "application": True,
}
