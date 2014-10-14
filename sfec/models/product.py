
from sfec.models.base import BaseModel
from storm.locals import Unicode, Int, Float, Bool

class Product(BaseModel):

	__storm_table__ = "sfec_product"

	name = Unicode()
	stock = Int(default=0)
	description = Unicode()
	price = Decimal(default=0.0)
	is_available = Bool(default=false)

    categories = ReferenceSet(Product.id, CategoryProduct.product_id, CategoryProduct.category_id, "Category.id")
