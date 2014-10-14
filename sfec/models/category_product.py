from storm.locals import Int
from storm.base import Storm

class CategoryProduct(Storm):

	__storm_table__ = "sfec_category_product"
	__storm_primary__ = "category_id","product_id"

	category_id = Int()
	product_id = Int()