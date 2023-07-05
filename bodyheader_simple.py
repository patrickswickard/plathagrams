import urllib3
import requests

#fields = {
#    "foo": "bar",
#    "somefile": ("somefile.txt", "contents of somefile"),
#    "imagegfile": ("cats.png", open("cats.png").read(), "image/png"),
#}

fields = {
    "inputtext": "lemon=melon",
    "submit" : "Generate Animated Gif",
    "bgcolor" : "#FF0000",
    "textcolor" : "#000000",
    "borderwidth" : "8",
    "cornerradius" : "8",
}

body, header = urllib3.encode_multipart_formdata(fields)
#print(body)

#print(header)

def request_animation_from_site():
  request_url = 'https://wordsmith.org/anagram/animation.cgi'
  fields = {
    "inputtext": "lemon=melon",
    "submit" : "Generate Animated Gif",
    "bgcolor" : "#FF0000",
    "textcolor" : "#000000",
    "borderwidth" : "8",
    "cornerradius" : "8",
  }

  body, ctheader = urllib3.encode_multipart_formdata(fields)
  headers = {'Content-type': ctheader}
  result = requests.post(request_url,body,headers=headers).text
  print(result)

request_animation_from_site()
