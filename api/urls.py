from rest_framework import routers

from api.views import FinanceUserViewSet, AmountDetailsViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('users', FinanceUserViewSet, basename="users")
router.register('loans', AmountDetailsViewSet, basename="loans")


urlpatterns = router.urls
