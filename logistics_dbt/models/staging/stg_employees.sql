select
    employee_id,
    trim(employee_name)       as employee_name,
    department,
    salary,
    warehouse_id,
    join_date,
    is_active
from {{ source('raw', 'employees') }}
