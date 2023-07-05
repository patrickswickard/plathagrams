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
    "animwidth" : "300",
    "animheight" : "100",
    "textcolor" : "#000000",
    "font" : "Times",
    "fstyle" : "normal",
    "justify" : "center",
    "spacing" : "0",
    "stroketext" : "0",
    "verticalshift" : "0",
    "bgcolor" : "#FF0000",
    "textshadow" : "0",
    "shadowcolor" : "#f7ff1c",
    "shadowblur" : "0",
    "borderwidth" : "2",
    "bordercolor" : "#000000",
    "cornerradius" : "8",
    "steps" : "30",
    "pause" : "50",
    "gifanimation" : "1",
    "source" : "advanced-form",
}

body, header = urllib3.encode_multipart_formdata(fields)
#print(body)

#print(header)

def request_animation_from_site():
  request_url = 'https://wordsmith.org/anagram/animation.cgi'
  fields = {
    "inputtext": "lemon=melon",
    "submit" : "Generate Animated Gif",
    "animwidth" : "300",
    "animheight" : "100",
    "textcolor" : "#000000",
    "font" : "Times",
    "fstyle" : "normal",
    "justify" : "center",
    "spacing" : "0",
    "stroketext" : "0",
    "verticalshift" : "0",
    "bgcolor" : "#FF0000",
    "textshadow" : "0",
    "shadowcolor" : "#f7ff1c",
    "shadowblur" : "0",
    "borderwidth" : "2",
    "bordercolor" : "#000000",
    "cornerradius" : "8",
    "steps" : "30",
    "pause" : "50",
    "gifanimation" : "1",
    "source" : "advanced-form",
  }
  body, ctheader = urllib3.encode_multipart_formdata(fields)
  headers = {'Content-type': ctheader}
  result = requests.post(request_url,body,headers=headers).text
  print(result)

request_animation_from_site()
