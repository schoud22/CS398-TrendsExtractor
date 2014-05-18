import bing_search
import google_search

pages=3

with open("results.txt") as f:
	content = f.readlines()

	for query in content:
		result=google_search.SearchEngine.search(query, 3)
		fname = query.replace('\n', '')
		fname = fname.replace('"', '')
		fname = fname.replace('|', '')
		fname = fname.replace(',', '')
		fname = fname.replace('.', '')
		fname = fname.replace('&', '')
		fname = fname.replace('\\', '')
		file=open('_google','r+b')
		
		for k in result:
			
		    #file.write(str(k.name)+"\t")
		    file.write(str(k.link)+"\t")
		   # file.write(str(k.description)+"\t")
		    file.write("\n")
		    for line in file:
				file.write(line.replace('/url?q=','') )
		    
		file.flush()
		file.close()
		
		result=bing_search.SearchEngine.search(query, 3)
		fname = query.replace('\n', '')
		fname = fname.replace('"', '')
		fname = fname.replace('|', '')
		fname = fname.replace(',', '')
		fname = fname.replace('.', '')
		fname = fname.replace('&', '')
		fname = fname.replace('\\', '')
		file=open('_bing','w')
		
		for k in result:
		    #file.write(str(k.name)+"\t")
		    file.write(str(k.link)+"\t")
		   # file.write(str(k.description)+"\t")
		    file.write("\n")
		
		file.flush()
		file.close()

	print("done - check dir for results")
