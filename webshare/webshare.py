import requests

from .util.objects import *
from typing import Optional, Dict, Union, List, Any

class Client:
    API_BASE_URL = "https://proxy.webshare.io/api/v2/"

    def __init__(self, api_key: str) -> None:
        """
        Initialize the Webshare Proxy API client.

        Parameters:
            api_key (str): The API key used for authentication.
        """
        self.headers: Dict[str, str] = {"Authorization": f"Token {api_key}"}
        self.session = requests.Session()

    def _request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make an HTTP request to the Webshare Proxy API.

        Parameters:
            method (str): The HTTP method ('GET', 'POST', 'PATCH', 'DELETE').
            endpoint (str): The API endpoint to call.
            data (dict, optional): The JSON data to send with the request (for 'POST' and 'PATCH' methods).
            params (dict, optional): Query parameters for the request.

        Returns:
            dict: The parsed JSON response from the API.

        Raises:
            ValueError: If the response status is not in the 2xx range or the JSON parsing fails.
        """
        url = self.API_BASE_URL + endpoint
        response = self.session.request(method, url, headers=self.headers, json=data, params=params)

        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"An error occurred while making the request: {e}")
        except ValueError as e:
            raise ValueError(f"Failed to parse JSON response: {e}")

    def create_ip(self, ip_address: str) -> IpAuthorization:
        """
        Create a new IP authorization entry.

        Parameters:
            ip_address (str): The IP address to authorize.

        Returns:
            IpAuthorization: The created IP authorization object.
        """
        data = {"ip_address": ip_address}
        return IpAuthorization(self._request("POST", "proxy/ipauthorization/", data=data))

    def get_ip(self) -> IpAuthorizationList:
        """
        Get a list of IP authorization entries.

        Returns:
            IpAuthorizationList: A list of IP authorization objects.
        """
        return IpAuthorizationList(self._request("GET", "proxy/ipauthorization/"))

    def delete_ip(self, id: str) -> int:
        """
        Delete an IP authorization entry.

        Parameters:
            id (str): The ID of the IP authorization entry to delete.

        Returns:
            int: The HTTP status code (200 if successful).
        """
        return self._request("DELETE", f"proxy/ipauthorization/{id}/").status_code

    def get_proxy_list(self,
                       mode: Optional[str] = "direct",
                       country_code_in: Optional[str] = None,
                       search: Optional[str] = None,
                       ordering: Optional[str] = None) -> ProxiesList:
        """
        Get a list of proxies with optional filters.

        Parameters:
            mode (str, optional): The proxy mode ('direct', 'residential', 'datacenter').
            country_code_in (str, optional): The country code to filter proxies by.
            search (str, optional): The search query to filter proxies by.
            ordering (str, optional): The ordering criteria for the proxy list.

        Returns:
            ProxiesList: A list of proxy objects.
        """
        params: Dict[str, Union[str, None]] = {
            "mode": mode,
            "country_code__in": country_code_in,
            "search": search,
            "ordering": ordering,
        }
        return ProxiesList(self._request("GET", "proxy/list/", params=params))

    def change_password(self, password: str, new_password: str) -> None:
        """
        Change the user's password.

        Parameters:
            password (str): The current password.
            new_password (str): The new password.
        """
        data = {
            "password": password,
            "new_password": new_password,
        }
        self._request("POST", "changepassword/", data=data)

    def change_email(self, new_email: str, password: str) -> None:
        """
        Change the user's email.

        Parameters:
            new_email (str): The new email address.
            password (str): The current password.
        """
        data = {
            "password": password,
            "new_email": new_email,
        }
        self._request("POST", "changeemail/", data=data)

    def change_email_complete(self, confirmation_code: str) -> None:
        """
        Complete the email change process.

        Parameters:
            confirmation_code (str): The confirmation code received after email change request.
        """
        data = {
            "confirmation_code": confirmation_code
        }
        self._request("POST", "changeemail/complete/", data=data)

    def get_activation_status(self) -> Activation:
        """
        Get the activation status of the user account.

        Returns:
            Activation: The activation status object.
        """
        return Activation(self._request("GET", "activation/"))

    def resend_activation_email(self) -> Activation:
        """
        Resend the activation email.

        Returns:
            Activation: The activation status object after resending the email.
        """
        return Activation(self._request("POST", "activation/resend/"))

    def complete_activation(self, activation_token: str) -> str:
        """
        Complete the user account activation process.

        Parameters:
            activation_token (str): The activation token received via email.

        Returns:
            str: The token for the activated user.
        """
        data = {
            "activation_token": activation_token
        }
        response = self._request("POST", "activation/complete/", data=data)
        return response.get("token")

    def logout(self) -> None:
        """Logout the user."""
        self._request("GET", "logout/")

    def get_profile(self) -> UserProfile:
        """
        Get the user's profile information.

        Returns:
            UserProfile: The user's profile information.
        """
        return UserProfile(self._request("GET", "profile/"))

    def update_profile(self, id: int = None, email: str = None, first_name: str = None, last_name: str = None, created_at: str = None, last_login: str = None, timezone: str = None, subscribed_bandwidth_usage_notifications: bool = None, subscribed_subscription_notifications: bool = None, subscribed_proxy_usage_statistics: bool = None, subscribed_usage_warnings: bool = None, subscribed_guides_and_tips: bool = None, subscribed_survey_emails: bool = None, tracking_id: str = None, helpscout_beacon_signature: str = None, announce_kit_user_token: str = None) -> UserProfile:
        """
        Update the user's profile information.

        Parameters:
            id (int, optional): The user's ID.
            email (str, optional): The user's email address.
            first_name (str, optional): The user's first name.
            last_name (str, optional): The user's last name.
            created_at (str, optional): The user's account creation date.
            last_login (str, optional): The user's last login date.
            timezone (str, optional): The user's timezone.
            subscribed_bandwidth_usage_notifications (bool, optional): Subscription status for bandwidth usage notifications.
            subscribed_subscription_notifications (bool, optional): Subscription status for subscription notifications.
            subscribed_proxy_usage_statistics (bool, optional): Subscription status for proxy usage statistics.
            subscribed_usage_warnings (bool, optional): Subscription status for usage warnings.
            subscribed_guides_and_tips (bool, optional): Subscription status for guides and tips.
            subscribed_survey_emails (bool, optional): Subscription status for survey emails.
            tracking_id (str, optional): The user's tracking ID.
            helpscout_beacon_signature (str, optional): The user's HelpScout beacon signature.
            announce_kit_user_token (str, optional): The user's Announce Kit user token.

        Returns:
            UserProfile: The updated user's profile information.
        """
        json_data = {
            "id": id,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "created_at": created_at,
            "last_login": last_login,
            "timezone": timezone,
            "subscribed_bandwidth_usage_notifications": subscribed_bandwidth_usage_notifications,
            "subscribed_subscription_notifications": subscribed_subscription_notifications,
            "subscribed_proxy_usage_statistics": subscribed_proxy_usage_statistics,
            "subscribed_usage_warnings": subscribed_usage_warnings,
            "subscribed_guides_and_tips": subscribed_guides_and_tips,
            "subscribed_survey_emails": subscribed_survey_emails,
            "tracking_id": tracking_id,
            "helpscout_beacon_signature": helpscout_beacon_signature,
            "announce_kit_user_token": announce_kit_user_token,
        }
        return UserProfile(self._request("PATCH", "profile/", data=json_data))

    def notifications(self) -> NotificationsList:
        """
        Get a list of notifications.

        Returns:
            NotificationsList: A list of notification objects.
        """
        return NotificationsList(self._request("GET", "notification/"))

    def get_notification(self, id: str) -> Notification:
        """
        Get a notification by its ID.

        Parameters:
            id (str): The ID of the notification.

        Returns:
            Notification: The notification object.
        """
        return Notification(self._request("GET", f"notification/{id}/"))

    def dismiss_notification(self, id: str) -> Notification:
        """
        Dismiss a notification.

        Parameters:
            id (str): The ID of the notification to dismiss.

        Returns:
            Notification: The dismissed notification object.
        """
        return Notification(self._request("GET", f"notification/{id}/dismiss/"))

    def restore_notification(self, id: str) -> Notification:
        """
        Restore a previously dismissed notification.

        Parameters:
            id (str): The ID of the notification to restore.

        Returns:
            Notification: The restored notification object.
        """
        return Notification(self._request("GET", f"notification/{id}/restore/"))

    def refresh(self) -> None:
        """Refresh the proxy list."""
        self._request("POST", "proxy/list/refresh/")

    def proxy_replacement(self, ordering: str = None, state: str = None, dry_run: bool = None) -> ProxyReplacementList:
        """
        Replace proxies with optional filters.

        Parameters:
            ordering (str, optional): The ordering criteria for the proxy replacement.
            state (str, optional): The state of the proxy replacement.
            dry_run (bool, optional): Whether to perform a dry run.

        Returns:
            ProxyReplacementList: A list of proxy replacement objects.
        """
        params = {}
        if ordering:
            params["ordering"] = ordering

        if state:
            params["state"] = state

        if dry_run:
            params["dry_run"] = dry_run

        return ProxyReplacementList(self._request("POST", "proxy/replace/", params=params))

    def get_proxy_replacement(self, id: str) -> ProxyReplacement:
        """
        Get a proxy replacement by its ID.

        Parameters:
            id (str): The ID of the proxy replacement.

        Returns:
            ProxyReplacement: The proxy replacement object.
        """
        return ProxyReplacement(self._request("POST", f"proxy/replace/{id}/"))

    def create_proxy_replacement(self, to_replace: dict = None, replace_with: list = None, dry_run: bool = None) -> ProxyReplacement:
        """
        Create a new proxy replacement.

        Parameters:
            to_replace (dict, optional): A dictionary of proxies to replace.
            replace_with (list, optional): A list of proxies to replace with.
            dry_run (bool, optional): Whether to perform a dry run.

        Returns:
            ProxyReplacement: The created proxy replacement object.
        """
        json_data = {}
        if to_replace:
            json_data["to_replace"] = to_replace

        if replace_with:
            json_data["replace_with"] = replace_with

        if dry_run:
            json_data["dry_run"] = dry_run

        return ProxyReplacement(self._request("POST", "proxy/replace/", data=json_data))

    def get_replaced_proxy(self, proxy_list_replacement: int = None) -> ProxyReplacementList:
        """
        Get a list of replaced proxies.

        Parameters:
            proxy_list_replacement (int, optional): The ID of the proxy list replacement.

        Returns:
            ProxyReplacementList: A list of replaced proxy objects.
        """
        params = {}
        if proxy_list_replacement:
            params["proxy_list_replacement"] = proxy_list_replacement

        return ProxyReplacementList(self._request("GET", "proxy/list/replaced/", params=params))

    def get_proxy_config(self) -> ProxyConfig:
        """
        Get the proxy configuration.

        Returns:
            ProxyConfig: The proxy configuration object.
        """
        return ProxyConfig(self._request("GET", "proxy/config/"))

    def update_proxy_config(self, new_username: str) -> ProxyConfig:
        """
        Update the proxy configuration with a new username.

        Parameters:
            new_username (str): The new username to set.

        Returns:
            ProxyConfig: The updated proxy configuration object.
        """
        data = {
            "username": new_username
        }
        return ProxyConfig(self._request("PATCH", "proxy/config/", data=data))

    def reset_download_token(self) -> ProxyConfig:
        """
        Reset the download token.

        Returns:
            ProxyConfig: The updated proxy configuration object.
        """
        return ProxyConfig(self._request("POST", "proxy/config/reset_download_token/"))

    def allocate_unallocated_countries(self, **countries) -> ProxyConfig:
        """
        Allocate unallocated countries.

        Parameters:
            **countries (dict): A dictionary of country codes and allocation values.

        Returns:
            ProxyConfig: The updated proxy configuration object.
        """
        data = {
            "new_countries": countries
        }
        return ProxyConfig(self._request("POST", "proxy/config/allocate_unallocated_countries/", data=data))

    def get_my_ip(self) -> str:
        """
        Get the user's IP address.

        Returns:
            str: The user's IP address.
        """
        response = self._request("GET", "proxy/ipauthorization/whatsmyip/")
        return response.get("ip_address")

    def create_api_key(self, label_name: str) -> ApiKey:
        """
        Create a new API key.

        Parameters:
            label_name (str): The label name for the new API key.

        Returns:
            ApiKey: The created API key object.
        """
        data = {
            "label": label_name
        }
        return ApiKey(self._request("POST", "apikey/", data=data))

    def update_api_key(self, id: str, label_name: str) -> ApiKey:
        """
        Update an existing API key.

        Parameters:
            id (str): The ID of the API key to update.
            label_name (str): The new label name for the API key.

        Returns:
            ApiKey: The updated API key object.
        """
        data = {
            "label": label_name
        }
        return ApiKey(self._request("PATCH", f"apikey/{id}/", data=data))

    def get_api_key(self, id: str) -> ApiKey:
        """
        Get an API key by its ID.

        Parameters:
            id (str): The ID of the API key.

        Returns:
            ApiKey: The API key object.
        """
        return ApiKey(self._request("GET", f"apikey/{id}/"))

    def api_keys(self) -> ApiKeyList:
        """
        Get a list of API keys.

        Returns:
            ApiKeyList: A list of API key objects.
        """
        return ApiKeyList(self._request("GET", "apikey/"))
