import pytest
import support_functions as support_functions

@pytest.mark.order1
def test_pet_created_with_correct_data():
    data = support_functions.post_details(52, 'categoryname_52', 'petname_52', 'Available', 'Accelerate', 'www.google.com')
    try:
        # print(data)
        assert 52 == data['id']
        # category
        assert 52 == data['category']['id']
        assert 'categoryname_52' == data['category']['name']
        #tags
        assert 52 == data['tags'][0]['id']
        assert "Accelerate" == data['tags'][0]['name']
        #status
        assert "Available" == data['status']
    except Exception:
        raise AssertionError


@pytest.mark.order2
def test_verify_pet_name_update():
    data = support_functions.put_update_details(52, 'categoryname_52', 'doggie', 'Available', 'Accelerate', 'www.google.com')
    # print(data)
    try:
        assert 'doggie' == data['name']
    except Exception:
        raise AssertionError
    return data


@pytest.mark.order3
def test_demonstrate_delete_pet():
    data = support_functions.delete_details(52)
    assert data.status_code == 200