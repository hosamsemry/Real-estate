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



# class ManageListingView(APIView):
#     def get():
#         pass

#     def post(self, request):
#         try:
#             user = request.user

#             if not user.is_realtor:
#                 return Response(
#                     {'error': 'You do not have permission to perform this action.'},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             data = request.data

#             title = data.get('title')
#             slug = data.get('slug')
#             if Listing.objects.filter(slug=slug).exists():
#                 return Response(
#                     {'error': 'Slug already exists.'},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             address = data.get('address')
#             city = data.get('city')
#             state = data.get('state')
#             zip_code = data.get('zip_code')
#             description = data.get('description')
#             price = data.get('price')
#             try:
#                 price = int(price)
#             except:
#                 return Response(
#                     {
#                         'error': 'Price must be a number.'},
#                         status=status.HTTP_400_BAD_REQUEST,
#                 )
            
#             bedrooms = data.get('bedrooms')
#             try:
#                 bedrooms = int(bedrooms)
#             except:
#                 return Response(
#                     {
#                         'error': 'bedrooms must be a number.'},
#                         status=status.HTTP_400_BAD_REQUEST,
#                 )
            
#             bathrooms = data.get('bedbathroomsrooms')
#             try:
#                 bathrooms = float(bathrooms)
#             except:
#                 return Response(
#                     {
#                         'error': 'bathrooms must be a floating value.'},
#                         status=status.HTTP_400_BAD_REQUEST,
#                 )
#             if bathrooms >= 10 or bathrooms <= 0 :
#                 bathrooms = 1.0

#             bathrooms = round(bathrooms, 1)

#             sale_type = data.get('sale_type')
#             if sale_type == "FOR_RENT":
#                 sale_type = "For Rent"
#             else:
#                 sale_type = "For Sale"

#             home_type = data.get('home_type')
#             if home_type == "CONDO":
#                 home_type = "Condo"
#             elif home_type == "HOUSE":
#                 home_type = "House"
#             else:
#                 home_type = "Townhouse"

#             main_photo = data.get('main_photo')
#             photo_1 = data.get('photo_1')
#             photo_2 = data.get('photo_2')
#             photo_3 = data.get('photo_3')

#             is_published = data.get('is_published')
#             if is_published == "true":
#                 is_published = True
#             else:
#                 is_published = False

#             Listing.objects.create(
#                 title=title,
#                 slug=slug,
#                 address=address,
#                 city=city,
#                 state=state,
#                 zip_code=zip_code,
#                 description=description,
#                 price=price,
#                 bedrooms=bedrooms,
#                 bathrooms=bathrooms,
#                 sale_type=sale_type,
#                 home_type=home_type,
#                 main_photo=main_photo,
#                 photo_1=photo_1,
#                 photo_2=photo_2,
#                 photo_3=photo_3,
#                 is_published=is_published
#             )

#             return Response(
#                 {'message': 'Listing created successfully.'},
#                 status=status.HTTP_201_CREATED,
#             )


#         except:
#             return Response(
#                 {'error': 'Invalid data.'},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
            