from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json

API_KEY = settings.API_KEY


@api_view(['GET'])
def products(request):
    api_type = request.GET.get('api_type', 'SptravelWarningService2')

    if api_type == 'NoticeService2': #외교부 공지사항
        url = 'http://apis.data.go.kr/1262000/NoticeService2/getNoticeList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '10',
            'pageNo': '1',
            'returnType': 'JSON'
        }
    elif api_type == 'LocalContactService2':   #외교부 현지연락처
        url = 'http://apis.data.go.kr/1262000/LocalContactService2/getLocalContactList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '10',
            'pageNo': '1',
            'otherParam': 'value'
        }
    elif api_type == 'EntranceVisaService2': #외교부_국가.지역별 입국허가요건
        url = 'http://apis.data.go.kr/1262000/EntranceVisaService2/getEntranceVisaList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '10',
            'pageNo': '1'
        }
    elif api_type == 'SecurityEnvironmentService': #외교부_국가.지역별 치안환경
        url = 'http://apis.data.go.kr/1262000/SecurityEnvironmentService/getSecurityEnvironmentList'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '10',
            'pageNo': '1'
        }
    elif api_type == 'OverviewGnrlInfoService': #외교부_국가.지역별 일반사항
        url = 'http://apis.data.go.kr/1262000/OverviewGnrlInfoService/getOverviewGnrlInfoList'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '10',
            'pageNo': '1'
        }
    elif api_type == 'CountryFlagService2':  # 외교부_국가∙지역별 국기 이미지
        url = 'http://apis.data.go.kr/1262000/CountryFlagService2/getCountryFlagList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '10',
            'pageNo': '1'
        }
    elif api_type == 'SptravelWarningService2':  # 외교부_국가∙지역별 특별여행주의보
        url = 'http://apis.data.go.kr/1262000/SptravelWarningService2/getSptravelWarningList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '10',
            'pageNo': '1'
        }





    else:
        return Response({'error': 'Invalid API type'}, status=status.HTTP_400_BAD_REQUEST)

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return Response({'error': 'Failed to fetch data from external API'}, status=response.status_code)

    products_data = response.json()
    return Response(products_data)
