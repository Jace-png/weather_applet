from firstdjango.settings import SRTATIC_URL_SELF
# print(SRTATIC_URL_SELF)
class Code:
    SUCCESS = 2000
    FAILED = 2222
    # @classmethod
    def get(self, code):
        if code == self.SUCCESS:
            return 'response success'
        elif code == self.FAILED:
            return 'response failed'
        else:
            return "I don't no"


class ResponseMixin():
    @staticmethod
    def wrap_response(response,**kwargs):
        if not response.get('code'):
            response['code'] = Code.SUCCESS
        elif not response.get('codedes'):
            code = Code()
            response['codedes'] = code.get(response.get('code'))
        return response

class SavePicMixin:
    @classmethod
    def savepic(cls,filename,filecontent):
        # print(SRTATIC_URL_SELF+'filename')
        with open(SRTATIC_URL_SELF+filename,'wb')as f :
            f.write(filecontent)

# c = SavePicMixin.savepic('abc','123')
