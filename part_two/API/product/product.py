import json
import part_two.util.logger as logging
import requests
import time


class Product(object):
    """
    Class to call the main functions of the API related to Products
    More information in: https://woocommerce.github.io/woocommerce-rest-api-docs/
    """

    def __init__(self, url, auth, wait=1):
        self.url = url
        self.auth = auth
        self.wait = wait

    def create(self, product, retries=5):
        """ Create a product via API
        :param product: json, send the product with this format:
        {
            "name": "Product Name",
            "type": "simple",
            "regular_price": "price with the format xx.xx",
            "description": "Product Description",
            "short_description": "Product Short Description"

            # Images and categories are optional
            "images": [
                {
                    "src": "source of the image"
                }
            ]
            "categories": [
                {
                    "id": "id of the category"
                }
            ]
        }
        :param retries: int, amount of tries to call the function because the call may fail
        :return: json, the product
        """
        url = self.url + '/wp-json/wc/v3/products'
        body = {
            'name': product["name"],
            'type': product["type"],
            'regular_price': product["regular_price"],
            'description': product["description"],
            'short_description': product["short_description"]
        }
        # checks if the optional attributes should be added to the body
        if "images" in product:
            body["images"] = product["images"]
        if "categories" in product:
            body["categories"] = product["categories"]

        # makes the post call
        response = requests.post(url, json=body, auth=self.auth)

        # checks if the response was successful
        if response.ok:
            logging.info("Product was created successfully")
            return json.loads(response.content)
        else:
            # checks if there are enough attempts left to retry the call
            if retries > 0:
                logging.warn(self.create, "Error when creating the product. Attempts left: {}".format(retries))
                # gives time to retry the call, by default 1 second
                time.sleep(self.wait)
                # recursively calls itself  to retry the call
                return self.create(product, retries - 1)

            # if the call failed and retries is 0, logs the error and throws an exception
            error = "Product was not created successfully\nMessage: " + response.content
            logging.error(error)
            raise Exception(error)

    def delete(self, product_id, retries=5):
        """ Delete a product via API
        :param product_id: str, the ID of the product to delete
        :param retries: int, amount of tries to call the function because the call may fail
        :return: json, deleted product
        """
        url = (self.url + "/wp-json/wc/v3/products/{}").format(product_id)
        response = requests.delete(url, auth=self.auth)
        # checks if the response was successful
        if response.ok:
            logging.info("Product was deleted successfully")
            return json.loads(response.content)
        else:
            # checks if there are enough attempts left to retry the call
            if retries > 0:
                logging.warn(self.create, "Error when creating the product. Missing attempts: {}".format(retries))
                # gives time to retry the call, by default 1 second
                time.sleep(self.wait)
                # recursively calls itself  to retry the call
                return self.delete(product_id, retries - 1)

            # if the call failed and retries is 0, logs the error and throws an exception
            error = "Product was not created successfully\nMessage: " + response.content
            logging.error(error)
            raise Exception(error)
