import requests
import json

# 테스트 데이터 설정
base_url = 'http://34.64.132.0/api'  # API 서버의 기본 URL

#base_url = 'http://127.0.0.1:8000'


planner_data = {'user_id': 'Test user', 'title': 'Planner'}

# 플래너 생성 테스트
def test_create_planner():
    response = requests.post(f'{base_url}/planners/planner_create/', json=planner_data)
    if response.status_code == 201:
        print("success ! ! !")
        updated_planner = response.json()  # 업데이트된 플래너 정보 가져오기
        print("planner_info:", updated_planner)
    elif response.status_code == 404:
        print("error: create planner failed")
    else:
        print("error: create planner failed", response.text)

# 플래너 조회 테스트
def test_get_planner(planner_id):
    response = requests.get(f'{base_url}/planners/{planner_id}/')
    assert response.status_code == 200  # 성공적인 응답을 의미하는 상태 코드인 200을 기대
    assert response.json()['title'] == 'Test Planner'  # 응답 데이터의 title 필드 확인

def test_update_planner(planner_id):
    update_data = {'title': '한국어 테스트'}
    update_data = {
        "user_id": "테스트",
        "title": "안녕 하세요",
        "cells": [
        {
        "day": [
            {
            "status": 0,
            "place_id": "",
            "memo": ""
            },
            {
            "status": 0,
            "place_id": "place1",
            "memo": "Sample memo"
            }
        ]
        }
  ]
    }

    url = f'{base_url}/planners/{planner_id}/update/'  # 업데이트할 플래너의 URL
    response = requests.put(url, json=update_data)  # PUT 요청을 보냄
    
    # 응답 처리
    if response.status_code == 201:
        print("success ! ! !")
        updated_planner = response.json()  # 업데이트된 플래너 정보 가져오기
        print("planner_info:", updated_planner)
    elif response.status_code == 404:
        print("error: No planner")
    else:
        print("error: update planner failed", response.text)

# 플래너 삭제 테스트
def test_delete_planner(planner_id):
    response = requests.delete(f'{base_url}/planners/{planner_id}/delete/')
    if response.status_code == 201:  # 삭제됨을 의미하는 상태 코드인 204를 기대
        print("success: delete Planner")
    else:
        print("failed: delete Planner")

#detail
def test_placeDetail(place_id):
    response = requests.get(f"{base_url}/googlemaps/placeDetails/?place_id={place_id}")
    
    print(response.status_code)
    response_data = response.json()
    print(response_data)

test_placeDetail("ChIJQ2kZ0BZBezUR62P9J1qdarU")
