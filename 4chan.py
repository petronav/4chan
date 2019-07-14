import requests
import webbrowser
import time
import json
import random


with open('boards.txt', 'r') as f:
	boards = [i.strip() for i in f.readlines()]
cache = {cache : '' for cache in boards}

def r4chan():
	board = random.choice(boards)
	thread_nums = []
	data = ''
	if cache[board] != '':
		data = cache[board]
	else:
		data = (requests.get('http://a.4cdn.org/'+board+'/catalog.json')).json()
		cache[board] = data
		time.sleep(2)
	for page in data:
		for thread in page['threads']:
			thread_nums.append(thread['no'])
	thread = random.choice(thread_nums)
	imgs = []
	pd = (requests.get('http://a.4cdn.org/'+board+'/thread/'+str(thread)+'.json')).json()
	for post in pd['posts']:
		try:
			imgs.append(str(post['tim'])+str(post['ext']))
		except:
			pass
	time.sleep(2)

	image = random.choice(imgs)
	image_url = 'https://is2.4chan.org/' + board + '/' + image
	thread = 'https://boards.4chan.org/' + board + '/thread/' + str(thread)
	return image_url, thread

def main(total_images):
	for i in range(total_images):
		url = r4chan()
		webbrowser.open(url[0])
		print(url[1])
		time.sleep(2)


if __name__ == '__main__':
	main(5)