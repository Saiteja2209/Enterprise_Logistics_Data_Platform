select
    tracking_id,
    partner_id,
    latitude,
    longitude,
    speed,
    timestamp                as tracking_timestamp
from {{ source('raw', 'gps_tracking') }}
