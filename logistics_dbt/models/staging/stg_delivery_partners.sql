select
    partner_id,
    partner_name,
    vehicle_type,
    rating,
    joining_date
from {{ source('raw', 'delivery_partners') }}
