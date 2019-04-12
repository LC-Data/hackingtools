#!/usr/bin/env python

import os
import requests 
import time

def main():

	urlList = [line.rstrip('\n') for line in open('./urls2.txt')];											#Should be a file with target urls on new lines
	methods = ['GET', 'POST', 'PATCH', 'TRACE', 'DELETE', 'HEAD', 'PUT', 'OPTIONS', 'CONNECT', 'FAKE'];				#These are all of the standard HTTP methods - will test each method/url combo

	print("Methods tested: " + str(methods));

	for p in range (0, len(urlList)):
		print(urlList[p]);

	attack = raw_input("Do you wish to continue?:(y/n) ").lower();
	if attack == "y":
		hit(urlList, methods);
	elif attack == "n":
		print("Not ready to make requests?;");			#Make this go back to somewhere useful
		main();
	else:
		print("try again;");			#same here
		main();

def hit(URLs, methods):

	twoHundreds = [];
	twoxx = 0;
	threeHundreds = [];

	#verify=False, allow_redirects=False  //These args after a .get() request will ignore cert issues and disallow redirects (so it won't hit unauthenticated then get redirected and return a 200)

	for url in range(0,len(URLs)):
		#print(os.system("curl -X 'GET' --url 'https://9.118.0.157'" + lineList[i] + " --insecure -I"));
		#print(i);

		for method in range(0, len(methods)):
			time.sleep(2);
			print("Trying to " + str(methods[method]) + " " + str(URLs[url]));
			request = requests.get(URLs[url]);

			if (str(request.status_code)[0]) == "2":
				print("********************UNAUTHENTICATED CONNECTION " + str(request.status_code) + "********************");
				print(request.status_code), "\n\n\n";
				twoxx += 1;
				if (URLs[url]) not in twoHundreds:
					twoHundreds.append(URLs[url]);
					print(twoHundreds);
			elif (str(request.status_code)[0]) == "3":
				print("<=<=<=<=<=<=REDIRECTION STATUS CODE " + str(request.status_code) + "=>=>=>=>=>=>");
				if (URLs[url]) not in threeHundreds:
					threeHundreds.append(URLs[url]);
					print(threeHundreds);
			else:

				print(request);
				#print("\n\n\n");
				print(request.status_code);
				print(methods[method], URLs[url]), "\n\n\n\n";

	print("There were " + str(twoxx) + " successful UNAUTHENTICATED requests made.");

main();
