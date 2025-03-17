from playwright.sync_api import Playwright

order_payload = {"orders": [{"country": "India", "productOrderedId": "67a8dde5c0d3e6622a297cc8"}]}



class RestApis:
    def get_token(self, playwright: Playwright,user_cred):
        email = user_cred['user_email']
        passwd = user_cred['user_pass']
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_context.post(url="api/ecom/auth/login",
                                   data={'userEmail':email,'userPassword':passwd}, headers={"Content-Type": "application/json"})
        assert response.ok
        response_body = response.json()
        return response_body['token']

    def create_order(self, playwright: Playwright,user_cred):
        token = self.get_token(playwright,user_cred)
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_context.post(url='/api/ecom/order/create-order',
                                   data=order_payload,
                                   headers={"Authorization": token, "Content-Type": "application/json"})
        assert response.ok
        response_json = response.json()
        order_id = response_json["orders"][0]
        return order_id

