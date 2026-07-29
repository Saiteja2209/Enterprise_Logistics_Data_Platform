select
    {{ dbt_utils.generate_surrogate_key(['tracking_id']) }} as tracking_key,
    tracking_id,
    {{ dbt_utils.generate_surrogate_key(['partner_id']) }} as partner_key,
    cast(to_char(cast(tracking_timestamp as date), 'YYYYMMDD') as number) as tracking_date_key,
    latitude,
    longitude,
    speed,
    tracking_timestamp
from {{ ref('stg_gps_tracking') }}
