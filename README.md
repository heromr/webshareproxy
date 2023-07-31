<div align="center">
  <h1 style="color: #0d47a1; font-size: 3em;">Webshare Proxy API Python Client</h1>
  
  <p>
    <a href="https://github.com/heromr/webshareproxy/commits/main"><img src="https://img.shields.io/github/last-commit/heromr/webshareproxy?label=last%20updated&color=blueviolet" alt="GitHub last commit"></a>
    <a href="https://pypi.org/project/webshareproxy/"><img src="https://img.shields.io/pypi/dw/webshareproxy?color=blueviolet" alt="PyPI - Downloads"></a>
  </p>

  <p style="font-size: 1.2em; color: #424242;">A Python client library for the Webshare Proxy API, providing easy access to various operations like managing proxies, IP authorizations, user profile, notifications, and more.</p>
  
  <h2 style="color: #0d47a1; font-size: 2em;">Installation</h2>
  
  <p style="font-size: 1.2em; color: #424242;">Recommended installation method is via pip:</p>
  
  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">pip install webshareproxy</code></pre>
  
  <p style="font-size: 1.2em; color: #424242;">Alternatively, you can clone the repository and install it manually:</p>
  
  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">git clone https://github.com/heromr/webshareproxy.git
cd webshareproxy
python setup.py install</code></pre>
  
</div>

<div>
  <h2 align="center">Getting Started</h2>

  <p>
    To get started with the Webshare Proxy API Python client, you'll need an API key from Webshare Proxy. If you don't have one, you can obtain it by signing up on the Webshare Proxy website.
  </p>

  <p>
    Once you have the API key, you can create an instance of the <code>ApiClient</code> class and pass the API key as an argument:
  </p>

  <pre><code class="language-python">
from webshare import ApiClient

# Replace 'YOUR_API_KEY' with your actual API key from Webshare Proxy
api_key = "YOUR_API_KEY"

# Create an instance of the ApiClient class
api_client = ApiClient(api_key)
  </code></pre>
</div>

<div>
  <h2 align="center">Available Methods</h2>

  <p>
    The <code>ApiClient</code> class provides several methods to interact with the Webshare Proxy API. Each method corresponds to an API endpoint and performs specific operations. Here are some of the available methods:
  </p>

  <h3 style="color: #0d47a1;" align="center">create_ip</h3>
  <p>Create a new IP authorization entry.</p>

  <pre><code class="language-python">
ip_address = "123.45.67.89"
new_ip_auth = api_client.create_ip(ip_address)
print("New IP Authorization ID:", new_ip_auth.id)
  </code></pre>

  <h3 style="color: #0d47a1;" align="center">get_ip</h3>
  <p>Get a list of IP authorization entries.</p>

  <pre><code class="language-python">
ip_authorizations = api_client.get_ip()
for ip_auth in ip_authorizations.get_results:
    print("IP Address:", ip_auth.ip_address)
  </code></pre>

  <h3 style="color: #0d47a1;" align="center">get_proxy_list</h3>
  <p>Get a list of proxies with optional filters.</p>

  <pre><code class="language-python">
# Get a list of proxies country code 'US'
proxies = api_client.get_proxy_list(country_code_in='US')
for proxy in proxies.get_results:
    print("Proxy Host:", proxy.proxy_address)
    print("Proxy Port:", proxy.port)
    print("Proxy Username:", proxy.username)
    print("Proxy Password:", proxy.password)
    print("Country Code:", proxy.country_code)
    print()
  </code></pre>

</div>

<div align="center">
  <h2>Contributing</h2>

  <p>
    Contributions are welcome! If you find a bug, have any questions, or want to suggest an improvement, feel free to open an issue or submit a pull request.
  </p>
</div>

<div align="center">
  <h2>License</h2>

  <p>
    This library is open-source and available under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.
  </p>
</div>
