from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import ProductMaterials, Warehouse


class ProductMaterialsAPIView(APIView):
    def get(self, request):
        # so'rov jo'natiladi
        products_required = request.data.get("products_required", [])
        # So'rov natijalari uchun bo'sh ro'yxat
        final_result = []

        for product_info in products_required:
            # Mahsulot vaqtincha saqlanadigan o'zgaruvchilar
            product_name = product_info["product_name"]
            product_qty = product_info["product_qty"]
            product_materials_list = []

            # Mahsulotlar uchun kerakli materiallarni ombordan topish
            product_materials = ProductMaterials.objects.filter(product_name__product_name=product_name)

            for product_material in product_materials:
                # Mahsulotning material nomi va kerakli miqdori olish
                material_name = product_material.material_name.name
                quantity_required = float(product_material.quantity) * int(product_qty)

                # Materialni omborda qidirish
                warehouses = Warehouse.objects.filter(material_id__name=material_name)
                warehouses_data = []

                for warehouse in warehouses:
                    if quantity_required <= 0:
                        break

                    # Ombordan kerakli miqdorni olamiz
                    qty_from_warehouse = min(quantity_required, warehouse.remainder)

                    warehouse_data = {
                        "warehouse_id": warehouse.id,
                        "material_name": material_name,
                        "qty": qty_from_warehouse,
                        "price": warehouse.price
                    }
                    warehouses_data.append(warehouse_data)
                    quantity_required -= qty_from_warehouse

                product_materials_list.extend(warehouses_data)

            # Natijani saqlash va qaytarish
            product_result = {
                "product_name": product_name,
                "product_qty": product_qty,
                "product_materials": product_materials_list
            }
            final_result.append(product_result)
        # natijani qayataradi
        return Response({"result": final_result})
