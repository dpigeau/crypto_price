# Crypto Prices Project

This project is designed to visualize and store streaming cryptocurrency price price data using a combination of Kafka, a postgre SQL database and a Streamlit front end app, with each component running into their own containers.

## Folder Structure

- `app/`: Contains the Streamlit application.
- `db/`: Contains the PostgreSQL database setup and configuration.
- `stream/`: Contains the Kafka stream setup and scripts to source Bitcoin price data from the Coingecko API.

## Getting Started

### Prerequisites

- Docker
- Python 3.10
- Pipenv

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/crypto_prices.git
    cd crypto_prices
    ```

2. Create an .env file and add
    ```sh
    PYTHONPATH=${PYTHONPATH}:${PWD}

    API_KEY = <your coingecko api key>
    POSTGRES_USER = 'postgres'
    POSTGRES_PASSWORD = 'postgres'
    POSTGRES_DB = 'coingecko'
    POSTGRES_PORT = '5432'
    POSTGRES_HOST = 'postgres'
    ```
    
2. Run 
    ```sh
    docker-compose up -d
    ```

3. In two separate terminals, run

    ```sh
    pipenv run python stream/consumer.py
    ```
    and
    ```sh
    pipenv run python stream/producer.py
    ```

4. Visit 0.0.0.0:8501 to visualize the streaming data

## Usage

- The Streamlit application will provide a visual representation of the streaming Bitcoin price data.
- The PostgreSQL database will store the streaming data for further analysis and historical reference.
- The Kafka stream will continuously source Bitcoin price data from the Coingecko API and feed it into the database and Streamlit application.

## License

This project is licensed under the MIT License.