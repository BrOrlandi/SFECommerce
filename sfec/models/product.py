
from sfec.models.base import BaseModel
from storm.locals import Unicode, Int, Decimal, Bool, ReferenceSet
from category_product import CategoryProduct

class Product(BaseModel):

	__storm_table__ = "sfec_product"

	name = Unicode()
	stock = Int(default=0)
	description = Unicode()
	price = Decimal()
	is_available = Bool(default=False)

	categories = ReferenceSet("Product.id", CategoryProduct.product_id, CategoryProduct.category_id, "Category.id")

