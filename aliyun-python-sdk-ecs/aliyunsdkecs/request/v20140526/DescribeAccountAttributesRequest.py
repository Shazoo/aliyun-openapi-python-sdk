from aliyunsdkcore.request import RpcRequest
class DescribeAccountAttributesRequest(RpcRequest):

    def __init__(self):
        RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeAccountAttributes','ecs')

    def get_ZoneId(self):
        return self.get_query_params().get('ZoneId')

    def set_ZoneId(self,ZoneId):
        self.add_query_param('ZoneId',ZoneId)

    
