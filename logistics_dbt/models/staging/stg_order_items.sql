select
    order_item_id,
    order_id,
    product_id,
    quantity,
    selling_price
from {{ source('raw', 'order_items') }}
