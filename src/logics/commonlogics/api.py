from main.actions.rest_actions import RestActions
from main.commonutils.config_manager import ConfigManager


class APITest:
    def get_api_response(self):
        tokenURL = "url"
        print("current url--", tokenURL)
        test = "api/users"
        global url
        url = tokenURL
        print(url)
        header = self.construct_headers()
        headers1={'Content-Type':'application/json;charset=utf-8',
                 'Authorization':f'{header}',
                 'Accept':'gzip, deflate, br'}
        print(headers1)

        response = RestActions().get_json_response_with_header(url, headers=headers1)
        print(response)

    def construct_headers(self):
        authorization = 'Bearer token'
        return authorization


APITest().get_api_response()
