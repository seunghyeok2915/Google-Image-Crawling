from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation
a = input("키워드를입력하세요")
b = input("개수를입력하세요")
arguments = {"keywords":a,"limit":b,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images