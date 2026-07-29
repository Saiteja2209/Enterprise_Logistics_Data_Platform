select
    {{ dbt_utils.generate_surrogate_key(['order_item_id']) }} as order_item_key,
    order_item_id,
    order_id,

    {{ dbt_utils.generate_surrogate_key(['customer_id']) }}  as customer_key,
    {{ dbt_utils.generate_surrogate_key(['employee_id']) }} as employee_key,
    {{ dbt_utils.generate_surrogate_key(['product_id']) }}   as product_key,
    {{ dbt_utils.generate_surrogate_key(['warehouse_id']) }} as warehouse_key,
    {{ dbt_utils.generate_surrogate_key(['partner_id']) }}   as partner_key,
    cast(to_char(cast(order_date as date), 'YYYYMMDD') as number)          as order_date_key,
    cast(to_char(cast(delivery_date as date), 'YYYYMMDD') as number)       as delivery_date_key,

    order_status,
    payment_method,

    quantity,
    item_selling_price                                        as unit_selling_price,
    cost_price                                                as unit_cost_price,
    line_amount,
    total_margin,
    margin_pct,
    order_total_amount

from {{ ref('int_order_items_enriched') }}
