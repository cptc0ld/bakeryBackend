import json
from textwrap import indent

from rest_framework import renderers, status


class JsonRenderer(renderers.JSONRenderer):

    def render(self, data, media_type=None, renderer_context=None):
        response = renderer_context['response']
        ret = {
            "status": response.status_code,
            "data": data
        }
        if response.status_code == status.HTTP_200_OK:
            ret["message"] = "OK"
            print(ret)
            return super(JsonRenderer, self).render(ret, media_type, renderer_context)

        if response.status_code == status.HTTP_404_NOT_FOUND:
            ret["message"] = "Page not found"
            return super(JsonRenderer, self).render(ret, media_type, renderer_context)

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            ret["message"] = "Unauthorized access"
            return super(JsonRenderer, self).render(ret, media_type, renderer_context)

        if response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            ret["message"] = "Server error"
            return super(JsonRenderer, self).render(ret, media_type, renderer_context)
