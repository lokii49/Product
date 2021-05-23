class Product:
    def __init__(self, productId, productName, productPrice, stockQuantity, reorderingQuantity, ownerName):
        self.productId = productId
        self.productName = productName
        self.productPrice = productPrice
        self.stockQuantity = stockQuantity
        self.reorderingQuantity = reorderingQuantity
        self.ownerName = ownerName

class ProductManagementSystem:
    def __init__(self, productList):
        self.productList = productList

    def getMaxProductPrice(self, ownername):
        self.ownername = ownername
        price = []
        for item in self.productList:
            if self.ownername == item.ownerName:
                price.append(item.productPrice)
        return max(price)

    def isStockAvailable(self, productname):
        self.productname = productname
        details = []
        for item in self.productList:
            if self.productname == item.productName and item.stockQuantity <= item.reorderingQuantity:
                details.append(item.productId)
                details.append(item.stockQuantity)
        return details


if __name__ == '__main__':
    productList = []
    for i in range(5):
        productId = int(input())
        productName = input()
        productPrice = int(input())
        stockQuantity = int(input())
        reorderingQuantity = int(input())
        ownerName = input()
        productList.append(Product(productId, productName, productPrice, stockQuantity, reorderingQuantity, ownerName))
    ownername = input()
    productname = input()
    obj = ProductManagementSystem(productList)
    result1 = obj.getMaxProductPrice(ownername)
    print(result1)
    result2 = obj.isStockAvailable(productname)
    print(' '.join(map(str, result2)))