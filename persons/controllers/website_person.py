from odoo import http
from odoo.http import request


class WebsitePerson(http.Controller):

    @http.route(
        ["/persons"], type="http", auth="public", website=True,
    )
    def persons_list(self, **kwargs):
        persons = (
            request.env["persons.person"]
            .sudo()
            .search([], order="id desc", limit=5)
        )
        return request.render("persons.persons_template", {
            "persons": persons
        })


