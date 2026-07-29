{% macro generate_schema_name(custom_schema, node) -%}
    {%- set default_schema = target.schema -%}

    {%- if custom_schema is none -%}
        {{ default_schema }}

    {%- elif custom_schema == 'raw_mart' -%}
        {{ 'RAW_MART' }}

    {%- else -%}
        {{ default_schema }}_{{ custom_schema }}

    {%- endif -%}
{%- endmacro %}
