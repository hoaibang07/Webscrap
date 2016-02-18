from shutil import copyfile

for x in xrange(1,10):
    des = 'getlink/get2thYoutubeLink' + str(x) + '.py'
    copyfile('get2thYoutubeLink.py', des)