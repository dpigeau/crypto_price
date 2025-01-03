CREATE OR REPLACE VIEW vw_crypto_prices AS
SELECT
    id,
    created_at,
    (row_data)['base_currency'] AS base_currency,
    (row_data)['quote_currency'] AS quote_currency,
    (row_data)['price'] AS price,
    (row_data)['price_last_updated_at'] AS price_last_updated_at
FROM crypto_prices
;

-- docker exec -it postgres psql -h localhost -U postgres -d coingecko -f views.sql 
-- must rebuilt the image to apply the sql changes to the database