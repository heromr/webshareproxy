from typing import List

class IpAuthorization:
    def __init__(self, data: dict):
        self.data = data

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def ip_address(self) -> str:
        return self.data.get("ip_address")

    @property
    def created_at(self) -> str:
        return self.data.get("created_at")

    @property
    def last_used_at(self) -> str:
        return self.data.get("last_used_at")


class IpAuthorizationList:
    def __init__(self, data: dict):
        self.data = data

    @property
    def count(self) -> int:
        return self.data.get("count")

    @property
    def next(self) -> str:
        return self.data.get("next")

    @property
    def previous(self) -> str:
        return self.data.get("previous")

    def get_results(self) -> List[IpAuthorization]:
        return [IpAuthorization(item) for item in self.data.get("results", [])]


class Proxy:
    def __init__(self, data: dict):
        self.data = data

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def username(self) -> str:
        return self.data.get("username")

    @property
    def password(self) -> str:
        return self.data.get("password")

    @property
    def proxy_address(self) -> str:
        return self.data.get("proxy_address")

    @property
    def port(self) -> int:
        return self.data.get("port")

    @property
    def valid(self) -> bool:
        return self.data.get("valid")

    @property
    def last_verification(self) -> str:
        return self.data.get("last_verification")

    @property
    def country_code(self) -> str:
        return self.data.get("country_code")

    @property
    def city_name(self) -> str:
        return self.data.get("city_name")

    @property
    def created_at(self) -> str:
        return self.data.get("created_at")


class ProxiesList:
    def __init__(self, data: dict):
        self.data = data

    @property
    def count(self) -> int:
        return self.data.get("count")

    @property
    def next(self) -> str:
        return self.data.get("next")

    @property
    def previous(self) -> str:
        return self.data.get("previous")

    def get_results(self) -> List[Proxy]:
        return [Proxy(item) for item in self.data.get("results", [])]


class Activation:
    def __init__(self, data: dict):
        self.data = data

    @property
    def email_is_verified(self) -> bool:
        return self.data.get("email_is_verified")

    @property
    def last_time_email_verification_email_sent(self) -> str:
        return self.data.get("last_time_email_verification_email_sent")

    @property
    def created_at(self) -> str:
        return self.data.get("created_at")

    @property
    def updated_at(self) -> str:
        return self.data.get("updated_at")


class UserProfile:
    def __init__(self, data: dict):
        self.data = data

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def email(self) -> str:
        return self.data.get("email")

    @property
    def first_name(self) -> str:
        return self.data.get("first_name")

    @property
    def last_name(self) -> str:
        return self.data.get("last_name")

    @property
    def last_login(self) -> str:
        return self.data.get("last_login")

    @property
    def timezone(self) -> str:
        return self.data.get("timezone")

    @property
    def subscribed_bandwidth_usage_notifications(self) -> bool:
        return self.data.get("subscribed_bandwidth_usage_notifications")

    @property
    def subscribed_subscription_notifications(self) -> bool:
        return self.data.get("subscribed_subscription_notifications")

    @property
    def subscribed_proxy_usage_statistics(self) -> bool:
        return self.data.get("subscribed_proxy_usage_statistics")

    @property
    def subscribed_usage_warnings(self) -> bool:
        return self.data.get("subscribed_usage_warnings")

    @property
    def subscribed_guides_and_tips(self) -> bool:
        return self.data.get("subscribed_guides_and_tips")

    @property
    def subscribed_survey_emails(self) -> bool:
        return self.data.get("subscribed_survey_emails")

    @property
    def tracking_id(self) -> str:
        return self.data.get("tracking_id")

    @property
    def helpscout_beacon_signature(self) -> str:
        return self.data.get("helpscout_beacon_signature")

    @property
    def announce_kit_user_token(self) -> str:
        return self.data.get("announce_kit_user_token")

    @property
    def created_at(self) -> str:
        return self.data.get("created_at")

    @property
    def updated_at(self) -> str:
        return self.data.get("updated_at")


class Notification:
    def __init__(self, data: dict):
        self.data = data

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def type(self) -> str:
        return self.data.get("type")

    @property
    def is_dismissable(self) -> bool:
        return self.data.get("is_dismissable")

    @property
    def context(self) -> dict:
        return self.data.get("context")

    @property
    def created_at(self) -> str:
        return self.data.get("created_at")

    @property
    def updated_at(self) -> str:
        return self.data.get("updated_at")

    @property
    def dismissed_at(self) -> str:
        return self.data.get("dismissed_at")


class NotificationsList:
    def __init__(self, data: dict):
        self.data = data

    @property
    def count(self) -> int:
        return self.data.get("count")

    @property
    def next(self) -> str:
        return self.data.get("next")

    @property
    def previous(self) -> str:
        return self.data.get("previous")

    def get_results(self) -> List[Notification]:
        return [Notification(item) for item in self.data.get("results", [])]


class ProxyReplacement:
    def __init__(self, data: dict):
        self.data = data

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def reason(self) -> str:
        return self.data.get("reason")

    @property
    def to_replace(self) -> dict:
        return self.data.get("to_replace")

    @property
    def replace_with(self) -> List[str]:
        return self.data.get("replace_with")

    @property
    def dry_run(self) -> bool:
        return self.data.get("dry_run")

    @property
    def state(self) -> str:
        return self.data.get("state")

    @property
    def proxies_removed(self) -> List[str]:
        return self.data.get("proxies_removed")

    @property
    def proxies_added(self) -> List[str]:
        return self.data.get("proxies_added")

    @property
    def created_at(self) -> str:
        return self.data.get("created_at")

    @property
    def completed_at(self) -> str:
        return self.data.get("completed_at")


class ProxyReplacementList:
    def __init__(self, data: dict):
        self.data = data

    @property
    def count(self) -> int:
        return self.data.get("count")

    @property
    def next(self) -> str:
        return self.data.get("next")

    @property
    def previous(self) -> str:
        return self.data.get("previous")

    def get_results(self) -> List[ProxyReplacement]:
        return [ProxyReplacement(item) for item in self.data.get("results", [])]


class ProxyConfig:
    def __init__(self, data: dict):
        self.data = data

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def state(self) -> str:
        return self.data.get("state")

    @property
    def countries(self) -> List[str]:
        return self.data.get("countries")

    @property
    def available_countries(self) -> List[str]:
        return self.data.get("available_countries")

    @property
    def unallocated_countries(self) -> List[str]:
        return self.data.get("unallocated_countries")

    @property
    def ip_ranges_24(self) -> List[str]:
        return self.data.get("ip_ranges_24")

    @property
    def ip_ranges_16(self) -> List[str]:
        return self.data.get("ip_ranges_16")

    @property
    def ip_ranges_8(self) -> List[str]:
        return self.data.get("ip_ranges_8")

    @property
    def available_ip_ranges_24(self) -> List[str]:
        return self.data.get("available_ip_ranges_24")

    @property
    def available_ip_ranges_16(self) -> List[str]:
        return self.data.get("available_ip_ranges_16")

    @property
    def available_ip_ranges_8(self) -> List[str]:
        return self.data.get("available_ip_ranges_8")

    @property
    def asns(self) -> List[str]:
        return self.data.get("asns")

    @property
    def available_asns(self) -> List[str]:
        return self.data.get("available_asns")

    @property
    def username(self) -> str:
        return self.data.get("username")

    @property
    def password(self) -> str:
        return self.data.get("password")

    @property
    def request_timeout(self) -> int:
        return self.data.get("request_timeout")

    @property
    def request_idle_timeout(self) -> int:
        return self.data.get("request_idle_timeout")

    @property
    def ip_authorization_country_codes(self) -> List[str]:
        return self.data.get("ip_authorization_country_codes")

    @property
    def auto_replace_invalid_proxies(self) -> bool:
        return self.data.get("auto_replace_invalid_proxies")

    @property
    def auto_replace_low_country_confidence_proxies(self) -> bool:
        return self.data.get("auto_replace_low_country_confidence_proxies")

    @property
    def auto_replace_out_of_rotation_proxies(self) -> bool:
        return self.data.get("auto_replace_out_of_rotation_proxies")

    @property
    def auto_replace_failed_site_check_proxies(self) -> bool:
        return self.data.get("auto_replace_failed_site_check_proxies")

    @property
    def proxy_list_download_token(self) -> str:
        return self.data.get("proxy_list_download_token")

    @property
    def created_at(self) -> str:
        return self.data.get("created_at")

    @property
    def updated_at(self) -> str:
        return self.data.get("updated_at")


class ApiKey:
    def __init__(self, data: dict):
        self.data = data

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def key(self) -> str:
        return self.data.get("key")

    @property
    def label(self) -> str:
        return self.data.get("label")

    @property
    def created_at(self) -> str:
        return self.data.get("created_at")

    @property
    def updated_at(self) -> str:
        return self.data.get("updated_at")


class ApiKeyList:
    def __init__(self, data: dict):
        self.data = data

    @property
    def count(self) -> int:
        return self.data.get("count")

    @property
    def next(self) -> str:
        return self.data.get("next")

    @property
    def previous(self) -> str:
        return self.data.get("previous")

    def get_results(self) -> List[ApiKey]:
        return [ApiKey(item) for item in self.data.get("results", [])]
