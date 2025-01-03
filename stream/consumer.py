import json
import logging
from kafka import KafkaConsumer
from db.postgresdb import postgresDB
from datetime import datetime

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

db = postgresDB()

def get_first_key(d):
    return next(iter(d))

def to_timestamp(ts):
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def format_message(message_value):
    base_currency = get_first_key(message_value)
    quote_currency = get_first_key(message_value[base_currency])
        
    return {
        'base_currency': base_currency,
        'quote_currency': quote_currency,
        'price':message_value[base_currency][quote_currency],
        'price_last_updated_at': to_timestamp(message_value[base_currency]['last_updated_at']),
    }

if __name__ == '__main__':
    logger.info("Starting consumer")
    consumer = KafkaConsumer(
        'crypto_prices',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda v: v.decode('utf-8'),
        consumer_timeout_ms=60000,
    )
    
    logger.info("Read the messages in the topic")
    for message in consumer:
        message_value_json = json.loads(message.value.replace("\'", "\""))
        formatted_message =  format_message(message_value_json)
        logger.info(f"Message received: {formatted_message}. Insert in postgres...")
        db.insert_rows('crypto_prices', formatted_message)

    logger.info("Closing the consumer as it reached its timeout")
    db.close()