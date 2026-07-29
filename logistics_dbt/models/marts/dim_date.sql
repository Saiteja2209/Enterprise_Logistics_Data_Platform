with date_spine as (

    select dateadd(day, seq4(), '2020-01-01')::date as full_date
    from table(generator(rowcount => 4018))

),

final as (

    select
        cast(to_char(full_date, 'YYYYMMDD') as number)   as date_key,
        full_date,
        year(full_date)                                   as year,
        quarter(full_date)                                as quarter,
        month(full_date)                                  as month_number,
        monthname(full_date)                              as month_name,
        left(monthname(full_date), 3)                     as month_short,
        day(full_date)                                    as day_of_month,
        dayofweek(full_date)                              as day_of_week,
        dayname(full_date)                                as day_name,
        left(dayname(full_date), 3)                       as day_short,
        case
            when dayofweek(full_date) in (0, 6) then true
            else false
        end                                               as is_weekend,
        weekofyear(full_date)                             as week_of_year,
        concat(year(full_date), '-', lpad(month(full_date), 2, '0')) as year_month,
        concat(year(full_date), '-Q', quarter(full_date))            as year_quarter

    from date_spine

)

select * from final
