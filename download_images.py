from simple_image_download import simple_image_download as simp
response=simp.simple_image_download
keywords=["person face images"]
for key in keywords:
    response().download(key,120)