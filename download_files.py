import urllib2, urllib
import time


#1 is alabama
#2,3 don't exist
#7,10,11,14 doesn't exist
for x in xrange(55):
    try:
        num = str(x+1)
        if x < 10:
            num = '0' + num
    
        url = "https://www2.census.gov/geo/relfiles/cdsld13/%s/dist_co_cd_%s.txt" % (num,num)

        print url
    
        res = urllib2.urlopen(url)

        html = res.read()

        split_page = html.split(' ') 
        state = split_page[0]
        state = state[0] + state[1:].lower()
        if state == 'New' or state == 'West' or state == 'North' or state == 'South':
            state += '_%s' % (split_page[1][0] + split_page[1][1:].lower())

        
        with open('Districts/%s.txt' % (state), 'w') as dt:
            dt.write(html)
                
        time.sleep(0.2)
  
    except:
        pass
