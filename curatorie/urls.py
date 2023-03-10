"""curatorie URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from curatorieapi.views import register_user, check_user, BoardView, GiftCardView, InspoCardView, ListCardView, PurchaseCardView, SharedBoardView, UserView, BoardTypeView, IconView, ShareRequestView, TypeView, SearchUserView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'search_users', SearchUserView, 'search_user')
router.register(r'boards', BoardView, 'board')
router.register(r'gift_cards', GiftCardView, 'gift_card')
router.register(r'inspo_cards', InspoCardView, 'inspo_card')
router.register(r'list_cards', ListCardView, 'list_card')
router.register(r'purchase_cards', PurchaseCardView, 'purchase_card')
router.register(r'shared_boards', SharedBoardView, 'shared_board')
router.register(r'share_requests', ShareRequestView, 'share_request')
router.register(r'board_types', BoardTypeView, 'board_type')
router.register(r'icons', IconView, 'icon')
router.register(r'types', TypeView, 'type')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
