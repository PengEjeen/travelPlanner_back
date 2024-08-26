from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json

API_KEY = settings.API_KEY


@api_view(['GET'])
def products(request):
    api_type = request.GET.get('api_type', 'areaCode1')

    if api_type == 'NoticeService2': #외교부 공지사항
        url = 'http://apis.data.go.kr/1262000/NoticeService2/getNoticeList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            'returnType': 'JSON'
        }
    elif api_type == 'LocalContactService2':   #외교부 현지연락처
        url = 'http://apis.data.go.kr/1262000/LocalContactService2/getLocalContactList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            'otherParam': 'value'
        }
    elif api_type == 'EntranceVisaService2': #외교부_국가.지역별 입국허가요건
        url = 'http://apis.data.go.kr/1262000/EntranceVisaService2/getEntranceVisaList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1'
        }
    elif api_type == 'SecurityEnvironmentService': #외교부_국가.지역별 치안환경
        url = 'http://apis.data.go.kr/1262000/SecurityEnvironmentService/getSecurityEnvironmentList'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1'
        }
    elif api_type == 'OverviewGnrlInfoService': #외교부_국가.지역별 일반사항
        url = 'http://apis.data.go.kr/1262000/OverviewGnrlInfoService/getOverviewGnrlInfoList'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1'
        }
    elif api_type == 'CountryFlagService2':  # 외교부_국가∙지역별 국기 이미지
        url = 'http://apis.data.go.kr/1262000/CountryFlagService2/getCountryFlagList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1'
        }
    elif api_type == 'SptravelWarningService2':  # 외교부_국가∙지역별 특별여행주의보
        url = 'http://apis.data.go.kr/1262000/SptravelWarningService2/getSptravelWarningList2'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1'
        }





    elif api_type == 'areaCode1':  # 지역코드조회 ##지역코드목록을 지역,시군구,읍면동 코드목록을 조회하는 기능
        url = 'http://apis.data.go.kr/B551011/KorService1/areaCode1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',

        }
    elif api_type == 'categoryCode1':  # 서비스분류코드조회 ##서비스분류코드목록을 대,중,소분류로 조회하는 기능
        url = 'http://apis.data.go.kr/B551011/KorService1/categoryCode1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',

        }
    elif api_type == 'areaBasedList1':  # 지역기반 관광정보조회 ##지역기반 관광정보파라미터 타입에 따라서 제목순,수정일순,등록일순 정렬검색목록을 조회하는 기능
        url = 'http://apis.data.go.kr/B551011/KorService1/areaBasedList1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
            'listYN': 'Y',

        }
    elif api_type == 'locationBasedList1':  #위치기반 관광정보조회 ##위치기반 관광정보파라미터 타입에 따라서 제목순,수정일순,등록일순 정렬검색목록을 조회하는 기능
        url = 'http://apis.data.go.kr/B551011/KorService1/locationBasedList1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
            'mapX': '126.981611',
            'mapY': '37.568477',
            'radius':'1000',
            'listYN': 'Y',
            'arrange':'E'

        }
    elif api_type == 'searchKeyword1':  #키워드 검색 조회 ##키워드로 검색을하며 전체별 타입정보별 목록을 조회한다
        url = 'http://apis.data.go.kr/B551011/KorService1/searchKeyword1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
            'listYN': 'Y',
            'keyword':'강원'


        }
    elif api_type == 'searchFestival1':  # 행사정보조회 ##행사정보목록을 조회한다. 컨텐츠 타입이 ‘행사’일 경우에만 유효하다
        url = 'http://apis.data.go.kr/B551011/KorService1/searchFestival1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type':'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
            'listYN': 'Y',
            'eventStartDate':'20240101'

        }
    elif api_type == 'searchStay1':  #숙박정보조회 ##숙박정보 검색목록을 조회한다. 컨텐츠 타입이 ‘숙박’일 경우에만 유효하다.
        url = 'http://apis.data.go.kr/B551011/KorService1/searchStay1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type':'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
            'listYN': 'Y',
            "arrange": 'A'
        }
    elif api_type == 'detailCommon1':  # 공통정보조회 ##타입별공통 정보기본정보,약도이미지,대표이미지,분류정보,지역정보,주소정보,좌표정보,개요정보,길안내정보,이미지정보,연계관광정보목록을 조회하는 기능
        url = 'http://apis.data.go.kr/B551011/KorService1/detailCommon1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
            'contentId': '126508',
            'defaultYN': 'Y',
            'firstImageYN':'Y',
            'addrinfoYN': 'Y',
            'mapinfoYN': 'Y',
            'overviewYN': 'Y',
            'areacodeYN':'Y',
            'catcodeYN':'Y'
        }
    elif api_type == 'detailIntro1':  # 소개정보조회 ##상세소개 쉬는날, 개장기간 등 내역을 조회하는 기능
        url = 'http://apis.data.go.kr/B551011/KorService1/detailIntro1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
            'contentId': '2674675',
            'contentTypeId': '15'
        }
    elif api_type == 'detailInfo1':  # 반복정보조회 ##추가 관광정보 상세내역을 조회한다. 상세반복정보를 안내URL의 국문관광정보 상세 매뉴얼 문서를 참고하시기 바랍니다.
        url = 'http://apis.data.go.kr/B551011/KorService1/detailInfo1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
            'contentId': '2674675',
            'contentTypeId': '15'
        }
    elif api_type == 'detailImage1':  #이미지정보조회 ##관광정보에 매핑되는 서브이미지목록 및 이미지 자작권 공공누리유형을 조회하는 기능
        url = 'http://apis.data.go.kr/B551011/KorService1/detailImage1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
            'contentId': '1095732',
            'imageYN' : 'Y',
            'subImageYN': 'Y'
        }
    elif api_type == 'areaBasedSyncList1':  #국문관광정보동기화목록조회 ##지역기반 관광정보파라미터 타입에 따라서 제목순,수정일순,등록일순 정렬검색목록을 조회하는 기능
        url = 'http://apis.data.go.kr/B551011/KorService1/areaBasedSyncList1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
        }
    elif api_type == 'detailPetTour1':  #반려동물 동반 여행 정보 ##타입별 반려동물 동반 여행 정보를 조회하는 기능입니다.
        url = 'http://apis.data.go.kr/B551011/KorService1/detailPetTour1'
        params = {
            'serviceKey': API_KEY,
            'numOfRows': '20',
            'pageNo': '1',
            '_type': 'json',
            'MobileOS': 'ETC',
            'MobileApp': 'AppTest',
        }



    else:
        return Response({'error': 'Invalid API type'}, status=status.HTTP_400_BAD_REQUEST)

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return Response({'error': 'Failed to fetch data from external API'}, status=response.status_code)

    products_data = response.json()
    return Response(products_data)
