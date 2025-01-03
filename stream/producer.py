from datetime import datetime
from time import sleep
import os
from stream.coingeckoapi import coinGeckoAPI
from kafka import KafkaProducer
import logging
# from dotenv import load_dotenv

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

# load environment variables
# load_dotenv() pipenv does this automatically
API_KEY = os.getenv('COINGECKO_API_KEY')

if __name__ == '__main__':
    logger.info('Starting producer')
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: str(v).encode('utf-8')    
    )

    logger.info('Connecting to CoinGecko API')
    coingecko = coinGeckoAPI(API_KEY)

    while True:
        logger.info(f'Fetching price for BTC at {datetime.now()}')
        price = coingecko.get_price('bitcoin')
        
        logger.info(f'Sending price to Kafka')
        producer.send('crypto_prices', price)
        sleep(15)
    
