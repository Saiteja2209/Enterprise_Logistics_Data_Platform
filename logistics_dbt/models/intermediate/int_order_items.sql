select
    oi.order_item_id,
    oi.order_id,
    oi.product_id,
    oi.quantity,
    oi.selling_price                               as item_selling_price,
    o.customer_id,
    o.employee_id,
    o.warehouse_id,
    o.partner_id,
    o.order_date,
    o.delivery_date,
    o.order_status,
    o.payment_method,
    o.total_amount                                 as order_total_amount
from {{ ref('stg_order_items') }} oi
inner join {{ ref('stg_orders') }} o
    on oi.order_id = o.order_id
