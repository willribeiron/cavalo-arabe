from rest_framework.exceptions import APIException


class BlockedUser(APIException):
    status_code = 400
    default_detail = 'User is blocked and not allowed to receive stamps'
    default_code = 'blocked-user'


class CampaignNotActive(APIException):
    status_code = 400
    default_detail = 'Campaign is not active'
    default_code = 'campaign-is-not-active'


class UserReceivedStampsToday(APIException):
    status_code = 400
    default_detail = 'User already received stamps today'
    default_code = 'user-already-received-stamps-today'
