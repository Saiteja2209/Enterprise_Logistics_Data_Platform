select
    order_id,
    customer_id,
    employee_id,
    warehouse_id,
    partner_id,
    order_date,
    delivery_date,
    order_status,
    payment_method,
    total_amount
from {{ source('raw', 'orders') }}
