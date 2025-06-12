from odoo import http
from odoo.http import request


class WebsitePerson(http.Controller):

    @http.route(
        ["/persons"],
        type="http",
        auth="public",
        website=True,
    )
    def persons_list(self, **kwargs):
        persons = (
            request.env["persons.person"].sudo().search([], order="id desc", limit=5)
        )
        return request.render("persons.persons_template", {"persons": persons})

    @http.route(
        "/persons/new",
        type="http",
        auth="public",
        website=True,
        methods=["GET", "POST"],
    )
    def create_person(self, **post):
        if post:
            request.env["persons.person"].sudo().create(
                {
                    "first_name": post.get("first_name"),
                    "last_name": post.get("last_name"),
                    "birthday": post.get("birthday"),
                    "sex": post.get("sex"),
                    "company_id": request.env.company.id,
                }
            )
            return request.redirect("/persons")
        return request.render("persons.persons_form_template")
