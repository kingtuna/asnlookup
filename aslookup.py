class asnLookup():
    """Write class to lookup asn"""
    def __init__(self):
        self.updateDir = "./"
        self.file = str(self.updateDir)+'cidr.txt'
        self.database = {}
        self.loadFile()
    def update(self):
        """Update the asn.txt file from arin and delete the header"""
        import urllib 
        urllib.urlretrieve('http://www.cidr-report.org/as2.0/autnums.html',self.file)
        lines = open(self.file).readlines()
        open(self.file, 'w').writelines(lines[13:-1])
    def remove_tags(self,text):
        import re
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub('', text)
    def loadFile(self):
        """Load File into memory"""
        handler = open(self.file, 'ro')
        for i in handler:
            predata = self.remove_tags(i.strip())
            if predata[:2].upper() == 'AS':
                asn = predata.split(' ', 1)[0][2:]
                name = predata.split(' ', 1)[1]
                self.database[asn] = name
            else:
                continue
    def lookup(self,asn):
        try:
            if asn[:2].upper() == 'AS':
                asn = asn[2:] 
            #print asn
            print self.database[asn]
            return(self.database[asn])
        except:
            return('')

### test
#asnn = asnLookup()
#asnn.update()
#asnn.lookup('6500')
#asnn.loadFile()
