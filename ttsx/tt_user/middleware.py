# -*- coding: utf-8 -*-
class UrlMiddleware:
    def process_view(self, request, view_name, view_args, view_kwars):
        if request.path not in [
            '/user/login/',
            '/user/login_submit/',
            '/user/register/',


            # url(r'^phone/$', phone),
            # url(r'^check/$', check),


        ]:
            request.session['url_path'] = request.get_full_path()


