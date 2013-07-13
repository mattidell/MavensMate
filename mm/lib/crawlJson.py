import json
import types
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def crawlDict(jsonData, depth, query, parentVisiblity):	
	depth += 1
	visibility = 0
	childVisibility = 0
	for key, value in jsonData.items():
		if isinstance(value, basestring) and query in value.lower():			
			visibility = 1
		elif not isinstance(value, types.DictType) and not isinstance(value, types.ListType) and query in str(value).lower():
			visibility = 1
	for key, value in jsonData.items():
		if crawl(value, depth, query, visibility) > 0:
			childVisibility = 1			
		visibility = visibility if visibility > childVisibility else childVisibility
	jsonData["visibility"] = visibility
	if visibility == 0:
		jsonData["cls"] = "hidden"
	return visibility

def crawlArray(jsonData, depth, query, parentVisiblity):
	depth += 1
	elementsToRemove = []
	index = 0
	for value in jsonData:
		if isinstance(value, basestring):
			childVisibility = query in value.lower()
		elif isinstance(value, types.DictType):
			childVisibility = crawl(value, depth, query, parentVisiblity)
			value["index"] = index
		else:
			childVisibility = query in str(value).lower()
		if childVisibility == 0 and parentVisiblity == 0:
			elementsToRemove.append(value)
			try:
				value["cls"] = "hidden"
			except:
				pass
		else:
			try:
				value["expanded"] = True
			except:
				pass
		index += 1
	for value in elementsToRemove:
		pass

def crawl(jsonData, depth, query, parentVisiblity):
	if(isinstance(jsonData,types.DictType)):
		return crawlDict(jsonData, depth, query, parentVisiblity)
	elif(isinstance(jsonData, types.ListType)):
		crawlArray(jsonData, depth, query, parentVisiblity)		
		#return len(jsonData) > 0
		for jd in jsonData:
			#print '\n\n'
			#print jd
			if 'visibility' in jd and jd['visibility'] == 1:
				return True
		return False
		# if 'cls' in jsonData and jsonData['cls'] == 'hidden':
		# 	return False
		# else:
		# 	return True
	else:	
		return 0

def startCrawl(jsonData, query):
	crawl(jsonData, 0, query.lower(), 0)