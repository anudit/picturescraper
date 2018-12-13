import shutil
import requests
import progressbar

max_val = 20000
bar = progressbar.ProgressBar(maxval=max_val,widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(11000,max_val+1):
	bar.update(i+1)
	url = 'http://lms.bennett.edu.in/pluginfile.php/'+str(i)+'/user/icon/lambda/f3'
	h = requests.head(url)
	header = h.headers
	content_type = header.get('content-type')
	if(content_type[0:10] == "image/jpeg"):
		response = requests.get(url, stream=True)
		with open(str(i) + '.jpg', 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response
bar.finish()