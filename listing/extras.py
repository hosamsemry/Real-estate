from .models import Listing


def delete_realtors_listing_data(realtor_email):
    if Listing.objects.filter(realtor=realtor_email).exists():
        listings = Listing.objects.filter(realtor=realtor_email)
        for listing in listings:
            listing.delete()