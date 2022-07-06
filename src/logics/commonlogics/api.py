from main.actions.rest_actions import RestActions
from main.commonutils.config_manager import ConfigManager


class APITest:
    def get_api_response(self):
        tokenURL = "https://igs-neon360-web.pt.playtech.corp/Neon360-PlayerResultApi/Customers/Search?SearchTerm=27284"
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
        authorization = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjUzN0M5QTFERDI5ODNBNEQ3QTdFNEI5NzBBMzEyQzQxNjE3MTdCOTRSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IlUzeWFIZEtZT2sxNmZrdVhDakVzUVdGeGU1USJ9.eyJuYmYiOjE2NTY1ODQ2MzYsImV4cCI6MTY1NjU4ODIzNiwiaXNzIjoiaHR0cHM6Ly9xYTI0LndlYi5pbnRlbGxpZ2VudGdhbWluZ3N5c3RlbXMuY29tL25lb25pZGVudGl0eS9uZW9uaWRlbnRpdHlzZXJ2ZXIiLCJhdWQiOlsibmVvbl9pZGVudGl0eV9hcGlfdXNlcm1hbmFnZW1lbnQiLCJuZW9uX2lkZW50aXR5X2FwaV9wcm9maWxlIiwibmVvbl9lbmdhZ2VtZW50X2FwaV9yZXNvdXJjZSIsIm5lb25fMzYwIiwibmVvbjM2MF9wbGF5ZXJyZXN1bHQiLCJuZW9uMzYwX3BsYXllcnJlc3VsdF9kZXYiLCJodHRwczovL3FhMjQud2ViLmludGVsbGlnZW50Z2FtaW5nc3lzdGVtcy5jb20vbmVvbmlkZW50aXR5L25lb25pZGVudGl0eXNlcnZlci9yZXNvdXJjZXMiXSwiY2xpZW50X2lkIjoibmVvbl9pZGVudGl0eV90ZXN0X2NsaWVudCIsInN1YiI6IjA3NDRkOWIxLTkxNmQtNDcxOC05NTgzLTE1N2EzMGRmNjFjZiIsImF1dGhfdGltZSI6MTY1NjU4NDYzNiwiaWRwIjoibG9jYWwiLCJjdXJyZW50X3ZlbnVlX2lkIjoiNDgiLCJyb2xlIjpbIkFwcGxpY2F0aW9uIiwiQ1JNSG9zdEFwcGxpY2F0aW9uIiwiRGFzaGJvYXJkc01hY2hpbmVzIiwiRGFzaGJvYXJkc01hbmFnZW1lbnQiLCJEYXNoYm9hcmRzTWFya2V0aW5nIiwiRGFzaGJvYXJkc1RhYmxlcyIsIkZsb29yTGVucyIsIkZsb29yU3R1ZGlvIiwibmVvbl8zNjAiLCJOZW9uMzYwUGxheWVyUmVzdWx0IiwiTmVvbjM2MFBsYXllclJlc3VsdERldiIsIk5lb25FbmdhZ2VtZW50IiwiTmVvbklkZW50aXR5U2FtcGxlc0FuZ3VsYXIiLCJSZWFkT25seSIsIlJvbGVGb3JBbmd1bGFyRXhhbXBsZSIsIlVuc3BlY2lmaWVkIiwiVXNlck1hbmFnZW1lbnQiXSwidXNlcl92ZW51ZV9pZCI6WyI0OCIsIjY3IiwiODQiLCIxMDAwIl0sImlhdCI6MTY1NjU4NDYzNiwic2NvcGUiOlsibmVvbl9hcGkiLCJvcGVuaWQiLCJwcm9maWxlIl0sImFtciI6WyJwd2QiXX0.ZH2Nf-ti251OkIUQd52dcQVadFScerZiV91Pa0gFNhKSGX5PIERBu8P2dr5u5ad4Hrb0Z_fqJ6NmOL2IMBP9L3pLKV4JgaEGgEg7l_A8rTF6yMYG76oXul-EyJxe1Nvyz96OWa3SU7MO1ARgMX5jCTWpFIGPb7shV9JWEQuNbNoAwFQUlAtYC8GPmMvT__v8a9LFMcP6UwVyyKAXjQyeruC5Jd6w0sGjUOsL4RI5_EqN68T3uFlYDN4LE3hg1HhQ40RpUsjVwF3bJndDG_c7tjZW7u6DxS-pBJ0llOZur9urpSPZNxOnIGAtaCy5-jcqIiTiWaYZXAve2DlA5FEUGg'
        return authorization


APITest().get_api_response()
