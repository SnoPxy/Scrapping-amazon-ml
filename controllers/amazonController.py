from services.amazonService import AmazonService
from controllers.libraryController import *

class amazonController:
    def main(self, produto, preco_maximo, link_count ):
        driver = webdriver.Chrome()
        amazon_control = AmazonService(produto, preco_maximo, link_count)
        amazon_control.valor_amazon()


        
