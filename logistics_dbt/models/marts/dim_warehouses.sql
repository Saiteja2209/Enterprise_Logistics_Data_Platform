select
    {{ dbt_utils.generate_surrogate_key(['warehouse_id']) }} as warehouse_key,
    warehouse_id,
    warehouse_name,
    city,
    capacity,
    manager
from {{ ref('stg_warehouses') }}
