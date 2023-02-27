from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExplosureLinks, SocialLinks
from .serializers import ExplosureLinksSerializer, SocialLinksSerializer


@api_view(["GET"])
def social_links(request):
    """
    Retrieve a list of all SocialLinks objects and serialize them using the
    SocialLinksSerializer.
    
    Returns:
        Response: A serialized representation of the SocialLinks objects.
    """

    social_links = SocialLinks.objects.all()
    serializer = SocialLinksSerializer(social_links, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def explosure_links(request):
    explosure_links = ExplosureLinks.objects.all()
    serializer = ExplosureLinksSerializer(explosure_links, many=True)
    return Response(serializer.data)
