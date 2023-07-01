
""" DESCRIPTION
The code below makes use of the requests library to perform API requests and retrieve data from the UniSwap protocol. Here are the comments explaining each part of the code:

    The code starts by setting the parameters for the UniSwap transaction request. The uniSwap_api_url variable contains the API endpoint URL, and the uniSwap_query variable stores the GraphQL query string to retrieve the desired transactions.

    The requests.post function is used to send a POST request to the UniSwap API endpoint, passing the GraphQL query as the request payload. The response is then stored in the uniSwap_response variable.

    The JSON response data is extracted using the json() method and accessed to retrieve the swaps data.

    The UniSwap transactions are then printed by iterating over the uniSwap_data list and printing each swap object.

    After that, the code sets the parameters for the pending UniSwap transactions request. The uniSwap_query_pending variable contains the GraphQL query string to retrieve pending transactions.

    The pending UniSwap transactions request is executed similar to the previous request, and the response is stored in the uniSwap_response_pending variable.

    The JSON response data is extracted and accessed to retrieve the transactions data.

    Finally, the pending UniSwap transactions are printed by iterating over the uniSwap_data_pending list and printing each transaction object.

"""
import requests
# Setting parameters for UniSwap transaction request
uniSwap_api_url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
uniSwap_query = """
query {
  swaps(first: 10, orderBy: timestamp, orderDirection: desc, where: { pair: "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599" }) {
    transaction {
      id
      timestamp
      gasPrice
    }
    amount0In
    amount0Out
    amount1In
    amount1Out
    amountUSD
    pair {
      token0 {
        symbol
      }
      token1 {
        symbol
      }
    }
  }
}
"""

# Executing the UniSwap transaction request
uniSwap_response = requests.post(uniSwap_api_url, json={'query': uniSwap_query})
uniSwap_data = uniSwap_response.json()['data']['swaps']

# Printing UniSwap transactions
print('UniSwap Transactions:')
for swap in uniSwap_data:
    print(swap)
    print('-------------------------------------------')

# Setting parameters for pending UniSwap transactions request
uniSwap_query_pending = """
query {
  transactions(first: 10, orderBy: timestamp, orderDirection: desc, where: {status: "pending"}) {
    id
    from
    to
    gasPrice
    gas
    value
    input
    timestamp
  }
}
"""

# Executing the pending UniSwap transactions request
uniSwap_response_pending = requests.post(uniSwap_api_url, json={'query': uniSwap_query_pending})
uniSwap_data_pending = uniSwap_response_pending.json()['data']['transactions']

# Printing pending UniSwap transactions
print('Pending UniSwap Transactions:')
for tx in uniSwap_data_pending:
    print(tx)
    print('-------------------------------------------')

