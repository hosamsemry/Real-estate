from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Listing
from .serializers import ListingSerializer

class ManageListingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if not request.user.is_realtor:
            return Response(
                {'error': 'You do not have permission to perform this action.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Listing created successfully.'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data.', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request):
        try:
            user = request.user

            if not user.is_realtor:
                return Response(
                    {'error': 'You do not have permission to perform this action.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            slug = request.query_params.get('slug')
            if slug:
                try:
                    listing = Listing.objects.get(slug=slug)
                    serializer = ListingSerializer(listing)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Listing.DoesNotExist:
                    return Response(
                        {'error': 'Listing not found.'},
                        status=status.HTTP_404_NOT_FOUND,
                    )
            else:
                listings = Listing.objects.filter(is_published=True)
                serializer = ListingSerializer(listings, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': 'An error occurred while retrieving listings.', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ListingDetailView(APIView):
    def get(self, request):
        try:
            slug = request.query_params.get('slug')
            if not slug:
                return Response(
                    {'error': 'Slug is required.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if not Listing.objects.filter(slug=slug, is_published=True).exists():
                return Response(
                    {'error': 'Listing not found.'},
                    status=status.HTTP_404_NOT_FOUND,
                )

            listing = Listing.objects.get(slug=slug, is_published=True)
            serializer = ListingSerializer(listing)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response(
                {'error': 'An error occurred while retrieving the listing.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    

class ListingsView(APIView):
    def get(self, request):
        permission_classes = (permissions.AllowAny, )
        try:
           
            listings = Listing.objects.filter(is_published=True)
            serializer = ListingSerializer(listings, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(
                {'error': 'An error occurred while retrieving listings.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )