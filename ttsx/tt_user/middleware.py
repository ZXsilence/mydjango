# -*- coding: utf-8 -*-
class UrlMiddleware:
    def process_view(self, request, view_name, view_args, view_kwargs):
        if request.path not in [
            '/user/login/',
            '/user/login_submit/',
            '/user/register/',
            '/cart/add/',
            '/cart/count/',
            '/cart/chcount/',
            '/cart/delcart/',
            '/user/user_info/',
            '/user/check_username/',


            # url(r'^phone/$', phone),
            # url(r'^check/$', check),


        ]:
            request.session['url_path'] = request.get_full_path()
            request.session.set_expiry(0)


