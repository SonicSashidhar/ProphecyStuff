{{
  config({    
    "materialized": "table",
    "alias": "targetout",
    "database": "tanmay",
    "schema": "sashi"
  })
}}

WITH addresses AS (

  SELECT * 
  
  FROM {{ source('tanmay_default', 'addresses') }}

),

Filter_1 AS (

  SELECT * 
  
  FROM addresses AS in0
  
  WHERE true

)

SELECT *

FROM Filter_1
