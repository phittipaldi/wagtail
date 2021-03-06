from __future__ import absolute_import, unicode_literals

from django.utils.deprecation import MiddlewareMixin

from wagtail.wagtailcore.models import Site


class SiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        Set request.site to contain the Site object responsible for handling this request,
        according to hostname matching rules
        """
        try:
            request.site = Site.find_for_request(request)
        except Site.DoesNotExist:
            request.site = None
