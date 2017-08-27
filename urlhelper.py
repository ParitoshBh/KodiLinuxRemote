class UrlHelper:
    protocol = 'http://'
    part = '/jsonrpc?request={"jsonrpc":"2.0",'
    ip_address = None
    port = None

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

    def prepareUrl(self, method_name, player_id = None):
        url = '%s%s:%s%s"id":1,"method":"%s"}' % (self.protocol, self.ip_address, self.port, self.part, method_name)

        if player_id is not None:
            url = '%s%s:%s%s"id":1,"method":"%s","params":{"playerid":%s}}' % (self.protocol, self.ip_address, self.port, self.part, method_name, player_id)
        
        return url