import hashlib

class MD5(object):

        def md5(self,fname):
	    try:
	            hash_md5 = hashlib.md5()
	            with open(fname, "rb") as f:
	                for chunk in iter(lambda: f.read(4096), b""):
	                    hash_md5.update(chunk)
	            return hash_md5.hexdigest()
	    except:
		    return "Diretorio"

