
from sfec.models.base import BaseModel
from storm.properties import Unicode
import category_product

class Category(BaseModel):

	 __storm_table__ = "sfec_category"

    name = Unicode()
    products = ReferenceSet(Category.id, CategoryProduct.category_id, CategoryProduct.product_id, "Product.id")

    def __init__(self, name):
        self.name = name