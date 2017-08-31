class UrlHelper:
    protocol = 'http://'
    part = '/jsonrpc?request={"jsonrpc":"2.0",'
    ip_address = None
    port = None

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

    def prepareUrl(self, method_name, param = None):
        url = '%s%s:%s%s"id":1,"method":"%s"}' % (self.protocol, self.ip_address, self.port, self.part, method_name)

        if param is not None:
            if type(param['value']).__name__ == 'int':
                url = '%s%s:%s%s"id":1,"method":"%s","params":{"%s":%s}}' % (self.protocol, self.ip_address, self.port, self.part, method_name, param['name'], param['value'])
            else:
                url = '%s%s:%s%s"id":1,"method":"%s","params":{"%s":"%s"}}' % (self.protocol, self.ip_address, self.port, self.part, method_name, param['name'], param['value'])

        print(url)
        
        return url