CREATE TABLE IF NOT EXISTS crypto_prices (
    id uuid DEFAULT gen_random_uuid(), 
    created_at TIMESTAMP DEFAULT NOW(),
    row_data JSONB,
    PRIMARY KEY (id)
);

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