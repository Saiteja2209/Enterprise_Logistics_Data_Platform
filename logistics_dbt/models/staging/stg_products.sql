select
    product_id,
    product_name,
    category,
    brand,
    cost_price,
    selling_price
from {{ source('raw', 'products') }}
