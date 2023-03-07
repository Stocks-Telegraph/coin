from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExplorerLinks, SocialLinks
from .serializers import ExplorerLinksSerializer, SocialLinksSerializer
from rest_framework import status


@api_view(["GET"])
def social_links(request):
    """
    Retrieve a list of all SocialLinks objects and serialize them using the
    SocialLinksSerializer.

    Returns:
        Response: A serialized representation of the SocialLinks objects.
    """
    symbol = request.GET.get("symbol").upper()
    social_links = SocialLinks.objects.filter(symbol__symbol=symbol)
    if not social_links.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SocialLinksSerializer(social_links, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def explorer_links(request):
    symbol = request.GET.get("symbol").upper()
    explorer_links = ExplorerLinks.objects.filter(symbol__symbol=symbol)
    if not explorer_links.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ExplorerLinksSerializer(explorer_links, many=True)
    return Response(serializer.data)
