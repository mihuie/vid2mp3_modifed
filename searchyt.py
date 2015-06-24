#!/usr/bin/python3

import requests
import sys, os
from bs4 import BeautifulSoup
import time
from vid2mp3 import *
from colored import fg, bg, attr

index_color = fg('black') + bg('yellow') + attr('bold') 
dur_color = fg('orchid') 
color = fg('yellow') + attr('bold')
reset = attr('reset')

youtube = 'https://www.youtube.com'
search_url = '/results?search_query='

def search(data):
	print ('\nRetrieving results.... \n')

	count = 1
	url = []

	for page in range(1,6):
		res = requests.get(youtube + search_url + data + '&page='+str(page))
		res.raise_for_status()

		soup = BeautifulSoup(res.text)
		search_r_title = soup.select('.yt-lockup-title a')
		search_r_duration = soup.select('.yt-lockup-title span')

		for i in range(len(search_r_title)):
			
			if not 'Playlis' in search_r_duration[i].text and \
			not 'Channel' in search_r_duration[i].text and \
			len(search_r_duration[i].text) < 19:
				if len(search_r_title[i].get('title')) > 45: 
					print ('{}{}{}\t{}{}{}\t{}...'.format(
							index_color, 
							str(count).ljust(4,' '), 
							reset,
							dur_color,
							search_r_duration[i].text.strip('- Duration: ').strip('.'),
							reset, 
							search_r_title[i].get('title')[:45])
					)
				else:
					print ('{}{}{}\t{}{}{}\t{}'.format(
							index_color, 
							str(count).ljust(4,' '), 
							reset,
							dur_color,
							search_r_duration[i].text.strip('- Duration: ').strip('.'),
							reset, 
							search_r_title[i].get('title'))
					)
				count += 1
				url.append(search_r_title[i].get('href'))

	while (1):
		choice = input('\n' + color + 'Enter the number corresponding with your choice ("x" to exit) : ' + reset)
		if choice is 'x':
			print ('... Bye... \n')
			sys.exit(0)
		else:
			print ('\n')
			make_url(youtube + url[int(choice) - 1])



if __name__ == '__main__':
    if len(sys.argv) > 1:
        search('+'.join(sys.argv[1:]))
    else:    
    	print ("usage:\n searchyt [term]")

