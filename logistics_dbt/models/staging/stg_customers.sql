select
    customer_id,
    trim(first_name)          as first_name,
    trim(last_name)           as last_name,
    lower(email)              as email,
    phone,
    initcap(city)             as city,
    state,
    signup_date
from {{ source('raw', 'customers') }}
