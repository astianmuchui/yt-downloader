import webbrowser



print("Type URL")
url = input()
if input != "":
   download = url[:12] + "ss" + url[12:]
   webbrowser.open(download)   