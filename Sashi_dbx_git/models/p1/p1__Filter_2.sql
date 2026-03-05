{{
  config({    
    "materialized": "ephemeral",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH airport AS (

  SELECT * 
  
  FROM {{ source('tanmay_default', 'airport') }}

),

Filter_2 AS (

  SELECT * 
  
  FROM airport AS in0
  
  WHERE true

)

SELECT *

FROM Filter_2
