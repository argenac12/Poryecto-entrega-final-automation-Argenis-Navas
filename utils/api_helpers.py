def validate_api_response(response, expected_status, expected_fields=None, max_time=1.0):

    assert response.status_code == expected_status

    if expected_status != 204:
        assert 'application/json' in response.headers.get('Content-Type', '')

    if expected_fields and response.text:
        body = response.json()
        assert expected_fields <= set(body.keys())

    assert response.elapsed.total_seconds() <= max_time

    return response.json() if response.text else {}