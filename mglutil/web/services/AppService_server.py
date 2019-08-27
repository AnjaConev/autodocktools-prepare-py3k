##################################################
# file: AppService_server.py
#
# skeleton generated by "ZSI.generate.wsdl2dispatch.ServiceModuleWriter"
#      /usr/local/bin/wsdl2py wsdl/opal.wsdl
#
##################################################

from ZSI.schema import GED, GTD
from ZSI.TCcompound import ComplexType, Struct
from .AppService_types import *
from ZSI.ServiceContainer import ServiceSOAPBinding

# Messages  
getAppMetadataRequest = GED("http://nbcr.sdsc.edu/opal/types", "getAppMetadataInput").pyclass

getAppMetadataResponse = GED("http://nbcr.sdsc.edu/opal/types", "getAppMetadataOutput").pyclass

getAppConfigRequest = GED("http://nbcr.sdsc.edu/opal/types", "getAppConfigInput").pyclass

getAppConfigResponse = GED("http://nbcr.sdsc.edu/opal/types", "getAppConfigOutput").pyclass

launchJobRequest = GED("http://nbcr.sdsc.edu/opal/types", "launchJobInput").pyclass

launchJobResponse = GED("http://nbcr.sdsc.edu/opal/types", "launchJobOutput").pyclass

launchJobBlockingRequest = GED("http://nbcr.sdsc.edu/opal/types", "launchJobBlockingInput").pyclass

launchJobBlockingResponse = GED("http://nbcr.sdsc.edu/opal/types", "launchJobBlockingOutput").pyclass

queryStatusRequest = GED("http://nbcr.sdsc.edu/opal/types", "queryStatusInput").pyclass

queryStatusResponse = GED("http://nbcr.sdsc.edu/opal/types", "queryStatusOutput").pyclass

getOutputsRequest = GED("http://nbcr.sdsc.edu/opal/types", "getOutputsInput").pyclass

getOutputsResponse = GED("http://nbcr.sdsc.edu/opal/types", "getOutputsOutput").pyclass

getOutputAsBase64ByNameRequest = GED("http://nbcr.sdsc.edu/opal/types", "getOutputAsBase64ByNameInput").pyclass

getOutputAsBase64ByNameResponse = GED("http://nbcr.sdsc.edu/opal/types", "getOutputAsBase64ByNameOutput").pyclass

destroyRequest = GED("http://nbcr.sdsc.edu/opal/types", "destroyInput").pyclass

destroyResponse = GED("http://nbcr.sdsc.edu/opal/types", "destroyOutput").pyclass


# Service Skeletons
class AppService(ServiceSOAPBinding):
    soapAction = {}
    root = {}

    def __init__(self, post='/axis/services/AppServicePort', **kw):
        ServiceSOAPBinding.__init__(self, post)

    def soap_getAppMetadata(self, ps, **kw):
        request = ps.Parse(getAppMetadataRequest.typecode)
        return request,getAppMetadataResponse()

    soapAction['http://nbcr.sdsc.edu/opal/getAppMetadata'] = 'soap_getAppMetadata'
    root[(getAppMetadataRequest.typecode.nspname,getAppMetadataRequest.typecode.pname)] = 'soap_getAppMetadata'

    def soap_getAppConfig(self, ps, **kw):
        request = ps.Parse(getAppConfigRequest.typecode)
        return request,getAppConfigResponse()

    soapAction['http://nbcr.sdsc.edu/opal/getAppConfig'] = 'soap_getAppConfig'
    root[(getAppConfigRequest.typecode.nspname,getAppConfigRequest.typecode.pname)] = 'soap_getAppConfig'

    def soap_launchJob(self, ps, **kw):
        request = ps.Parse(launchJobRequest.typecode)
        return request,launchJobResponse()

    soapAction['http://nbcr.sdsc.edu/opal/launchJob'] = 'soap_launchJob'
    root[(launchJobRequest.typecode.nspname,launchJobRequest.typecode.pname)] = 'soap_launchJob'

    def soap_launchJobBlocking(self, ps, **kw):
        request = ps.Parse(launchJobBlockingRequest.typecode)
        return request,launchJobBlockingResponse()

    soapAction['http://nbcr.sdsc.edu/opal/launchJobBlocking'] = 'soap_launchJobBlocking'
    root[(launchJobBlockingRequest.typecode.nspname,launchJobBlockingRequest.typecode.pname)] = 'soap_launchJobBlocking'

    def soap_queryStatus(self, ps, **kw):
        request = ps.Parse(queryStatusRequest.typecode)
        return request,queryStatusResponse()

    soapAction['http://nbcr.sdsc.edu/opal/queryStatus'] = 'soap_queryStatus'
    root[(queryStatusRequest.typecode.nspname,queryStatusRequest.typecode.pname)] = 'soap_queryStatus'

    def soap_getOutputs(self, ps, **kw):
        request = ps.Parse(getOutputsRequest.typecode)
        return request,getOutputsResponse()

    soapAction['http://nbcr.sdsc.edu/opal/getOutputs'] = 'soap_getOutputs'
    root[(getOutputsRequest.typecode.nspname,getOutputsRequest.typecode.pname)] = 'soap_getOutputs'

    def soap_getOutputAsBase64ByName(self, ps, **kw):
        request = ps.Parse(getOutputAsBase64ByNameRequest.typecode)
        return request,getOutputAsBase64ByNameResponse()

    soapAction['http://nbcr.sdsc.edu/opal/getOutputAsBase64ByName'] = 'soap_getOutputAsBase64ByName'
    root[(getOutputAsBase64ByNameRequest.typecode.nspname,getOutputAsBase64ByNameRequest.typecode.pname)] = 'soap_getOutputAsBase64ByName'

    def soap_destroy(self, ps, **kw):
        request = ps.Parse(destroyRequest.typecode)
        return request,destroyResponse()

    soapAction['http://nbcr.sdsc.edu/opal/destroy'] = 'soap_destroy'
    root[(destroyRequest.typecode.nspname,destroyRequest.typecode.pname)] = 'soap_destroy'

