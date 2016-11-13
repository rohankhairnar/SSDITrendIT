from django.http import HttpResponse
from django.template import RequestContext, loader


def cref_cse(request):
    return HttpResponse(
        loader.render_to_string(request,'googlesearch/cref_cse.xml', RequestContext(request)),
        mimetype = 'text/xml'
    )

