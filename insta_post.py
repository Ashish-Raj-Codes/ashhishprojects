from instagrapi import Client # type: ignore
cl = Client()
cl.login("kumar_kaushal_ranjh", "ur password")

cl.photo_upload("image.jpg", "This is an automated post from Python!")