class UrlHelper:
    protocol = 'http://'
    part = '/jsonrpc?request={"jsonrpc":"2.0",'
    ip_address = None
    port = None

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

    def prepare_url_with_param(self, method_name, params):
        url = '%s%s:%s%s"id":1,"method":"%s","params":' % (self.protocol, self.ip_address, self.port, self.part, method_name)

        for pos in params:
            # print(params[pos])
            if type(params[pos]['value']).__name__ == 'int':
                # url = '%s%s:%s%s"id":1,"method":"%s","params":{"%s":%s}}' % (self.protocol, self.ip_address, self.port, self.part, method_name, params[pos]['name'], params[pos]['value'])
                url = url + '{"' + params[pos]['name'] + '":' + params[pos]['value'] + '}'
            else:
                # url = '%s%s:%s%s"id":1,"method":"%s","params":{"%s":"%s"}}' % (self.protocol, self.ip_address, self.port, self.part, method_name, params[pos]['name'], params[pos]['value'])
                url = url + '{"' + params[pos]['name'] + '":"' + params[pos]['value'] + '"}'
        
        url = url + '}'

        # print(url)
        
        return url

    def prepare_url_without_param(self, method_name):
        url = '%s%s:%s%s"id":1,"method":"%s"}' % (self.protocol, self.ip_address, self.port, self.part, method_name)
        return url

    def prepare_param(self, parent, param):
        parent[len(parent) + 1] = param
        return parent