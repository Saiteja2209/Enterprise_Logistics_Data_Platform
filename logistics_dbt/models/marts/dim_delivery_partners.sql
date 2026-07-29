select
    {{ dbt_utils.generate_surrogate_key(['partner_id']) }}   as partner_key,
    partner_id,
    partner_name,
    vehicle_type,
    rating,
    joining_date
from {{ ref('stg_delivery_partners') }}
