select
    oi.order_item_id,
    oi.order_id,
    oi.product_id,
    oi.quantity,
    oi.item_selling_price,
    oi.customer_id,
    oi.employee_id,
    oi.warehouse_id,
    oi.partner_id,
    oi.order_date,
    oi.delivery_date,
    oi.order_status,
    oi.payment_method,
    oi.order_total_amount,
    p.product_name,
    p.category,
    p.brand,
    p.cost_price,
    round(oi.item_selling_price * oi.quantity, 2)   as line_amount,
    round((oi.item_selling_price - p.cost_price) * oi.quantity, 2) as total_margin,
    round(
        (oi.item_selling_price - p.cost_price) / nullif(p.cost_price, 0) * 100,
        2
    )                                               as margin_pct
from {{ ref('int_order_items') }} oi
inner join {{ ref('stg_products') }} p
    on oi.product_id = p.product_id
