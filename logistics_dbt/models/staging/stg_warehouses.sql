select
    warehouse_id,
    warehouse_name,
    city,
    capacity,
    manager
from {{ source('raw', 'warehouses') }}
