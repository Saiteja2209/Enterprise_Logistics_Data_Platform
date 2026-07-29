select
    {{ dbt_utils.generate_surrogate_key(['employee_id']) }}  as employee_key,
    employee_id,
    employee_name,
    department,
    salary,
    {{ dbt_utils.generate_surrogate_key(['warehouse_id']) }} as warehouse_key,
    warehouse_id,
    join_date,
    is_active
from {{ ref('stg_employees') }}
