"""Importing modules"""
from fastapi.testclient import TestClient
from main import app
from mock import patch

client = TestClient(app=app)


@patch('openai.Moderation.create')
def test_analize_sentiment(mock_openai):
    """Returns 200"""
    mock_openai.return_value = {
        "results": [{
            'flagged': True,
            'categories': {
                'hate': True
            }
        }]
    }

    response = client.post("/api/v1/sentiment-analysis",
                           json={'prompt': 'naturaleza'})
    assert response.status_code == 200
    assert response.json() == {'violates_content_policy': True}

# You need to create more test cases

# END
