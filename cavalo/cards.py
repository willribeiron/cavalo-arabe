import datetime
from cavalo.exceptions import BlockedUser, CampaignNotActive, UserReceivedStampsToday
from cavalo.models import Card, Campaign, Users, Bonus
from cavalo.models import Stamp, Card



def create_card(user, campaign):
    return Card.objects.create(user=user, campaign=campaign)


def check_if_campaign_is_active(campaign_id):
    campaign = Campaign.objects.filter(id=campaign_id).first()
    if campaign.end_date >= datetime.date.today() >= campaign.start_date:
        return campaign
    raise CampaignNotActive()


def check_if_user_is_allowed_to_receive_stamps_or_create_user(user_id):
    active_user = Users.objects.filter(id=user_id).first()
    if not active_user:
        new_user = Users.objects.create()
        return new_user
    if active_user.allowed_to_receive_stamps is False:
        raise BlockedUser()
    return active_user


def check_if_user_already_have_card(user, campaign):
    card = Card.objects.filter(user=user, campaign=campaign).first()
    if card:
        check_if_campaign_is_active(campaign_id=campaign)
        return card


def create_stamp(card):
    return Stamp.objects.create(card=card)


def check_if_user_received_stamps_today(card):
    if Stamp.objects.filter(card=card, created_at__gte=datetime.date.today()).exists():
        raise UserReceivedStampsToday


def generate_bonus(card):
    return Bonus.objects.create(card=card)


def check_if_card_is_complete_and_create_bonus(card):
    stamp = Stamp.objects.filter(card=card).count()
    if stamp == card.campaign.stamp_quantity:
        generate_bonus(card)


def check_if_card_has_bonus(card):
    return Bonus.objects.filter(card=card).exists()


def card_process(user_id, campaign_id):
    active_campaign = check_if_campaign_is_active(campaign_id=campaign_id)
    active_user = check_if_user_is_allowed_to_receive_stamps_or_create_user(user_id=user_id)
    card = check_if_user_already_have_card(user=user_id, campaign=campaign_id)
    if card:
        check_if_user_received_stamps_today(card)
    has_bonus = check_if_card_has_bonus(card=card)
    if not card or has_bonus is True:
        card = create_card(user=active_user, campaign=active_campaign)
        create_stamp(card)
    check_if_card_is_complete_and_create_bonus(card=card)
    return card
