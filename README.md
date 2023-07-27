<div align="center">
  <h1 style="color: #0d47a1; font-size: 3em;">Webshare Proxy API Python Client</h1>
  
  <p>
    <a href="https://github.com/heromr/webshare-proxy/commits/main"><img src="https://img.shields.io/github/last-commit/heromr/webshare-proxy?label=last%20updated&color=blueviolet" alt="GitHub last commit"></a>
    <a href="https://pypi.org/project/webshare-proxy/"><img src="https://img.shields.io/pypi/dw/webshare-proxy?color=blueviolet" alt="PyPI - Downloads"></a>
  </p>


  <p style="font-size: 1.2em; color: #424242;">Python client library for interacting with the Webshare Proxy API. This library provides a convenient way to access various endpoints of the Webshare Proxy API and perform operations like managing proxies, IP authorizations, user profile, notifications, and more.</p>

  
  <h2 style="color: #0d47a1; font-size: 2em;">Installation</h2>
  
  <p style="font-size: 1.2em; color: #424242;">You can install the library via pip:</p>
  
  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">pip install webshare-proxy-client</code></pre>
  
  <p style="font-size: 1.2em; color: #424242;">Alternatively, you can clone the repository and install it manually:</p>
  
  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">git clone https://github.com/your_username/webshare-proxy-client.git
  cd webshare-proxy
  python setup.py install</code></pre>
  
</div>

<div>
  <h2 align="center">API Client Usage</h2>

  <pre><code class="language-python">
from webshareproxy import ApiClient

# Replace 'YOUR_API_KEY' with your actual API key from Webshare Proxy
api_key = "YOUR_API_KEY"

# Create an instance of the ApiClient class
api_client = ApiClient(api_key)

# Now, you can use various methods of the ApiClient to interact with the Webshare Proxy API.
# See examples and detailed documentation in the [API Client Usage Guide](docs/usage.md).

# Example: Get a list of proxies
proxies_list = api_client.get_proxy_list()
for proxy in proxies_list.get_results():
    print(f"Proxy ID: {proxy.id}, Address: {proxy.proxy_address}, Port: {proxy.port}, Country: {proxy.country_code}")
  </code></pre>
</div>

<div>
  <h2 align="center">Contributing</h2>

  <p>
    Contributions are welcome! If you find a bug, have any questions, or want to suggest an improvement, feel free to open an issue or submit a pull request.
  </p>
</div>

<div>
  <h2 align="center">License</h2>

  <p>
    This library is open-source and available under the [MIT License](LICENSE).
  </p>
</div>
