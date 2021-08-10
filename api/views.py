from rest_framework import viewsets, mixins, status

# Create your views here.
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import FinanceUser, AmountDetails
from api.serializers import FinanceUserSerializer, AmountDetailsSerializer


class FinanceUserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = FinanceUser.objects.all()
    serializer_class = FinanceUserSerializer

    @permission_classes([AllowAny])
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = FinanceUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AmountDetailsViewSet(viewsets.ModelViewSet):
    queryset = AmountDetails.objects.all()
    serializer_class = AmountDetailsSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        lent_amounts = AmountDetails.objects.filter(lender=user)
        serialized_data = AmountDetailsSerializer(lent_amounts, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(methods=["PATCH"], detail=True)
    def close_loan(self, request, *args, **kwargs):
        loan = AmountDetails.objects.get(pk=kwargs.get("loan_id"))
        loan.is_closed = True
        loan.save()
        # send_lean_details_to_mail.delay(loan)
        # send_lean_details_to_mobile.delay(loan)

        return Response("Successfully closed loan", status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        interest_rate = data.get("interest_rate")
        interest_percentage = interest_rate * 12
        data["interest_percentage"] = interest_percentage

        serializer = AmountDetailsSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

