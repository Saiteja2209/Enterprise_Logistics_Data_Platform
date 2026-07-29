select
    {{ dbt_utils.generate_surrogate_key(['product_id']) }}   as product_key,
    product_id,
    product_name,
    category,
    brand,
    cost_price,
    selling_price
from {{ ref('stg_products') }}
