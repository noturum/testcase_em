import asyncio
import os
from aiohttp import ClientSession
import pytest
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('TOKEN')
REPO_NAME = os.getenv('REPOSITORY')

GITHUB_API_URL = os.getenv('GITHUB_API_URL')

HEADERS = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
}


class ApiGitClient:

    def __init__(self, headers):
        self.headers = headers
        self.session = ClientSession(headers=headers)

    async def get(self, url) -> tuple[int, dict]:
        async with self.session.get(url) as response:
            return (
                response.status,
                await response.json(),
            )

    async def post(self, url, data) -> tuple[int, dict]:
        async with self.session.post(url, json=data) as response:
            return (
                response.status,
                await response.json(),
            )

    async def delete(self, url) -> int:
        async with self.session.delete(url) as response:
            return response.status

    async def check_repo_exists(self, repo_name) -> bool:
        url = f'{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
        status, response = await self.get(url)
        return status == 200


@pytest.fixture()
async def client():
    client = ApiGitClient(HEADERS)
    yield client
    await client.session.close()


@pytest.mark.asyncio
async def test_create_repository(client):
    url = f'{GITHUB_API_URL}/user/repos'
    data = {
        'name': REPO_NAME,
        'private': False
    }
    status, response = await client.post(url, data)
    assert status == 201, f"Failed to create repository: {response}"


@pytest.mark.asyncio
async def test_check_repo_exists(client):
    assert await client.check_repo_exists(REPO_NAME), \
        f"Repository {REPO_NAME} does not exist."


@pytest.mark.asyncio
async def test_repo_deletion(client):
    url = f'{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    status = await client.delete(url)
    assert status == 204, \
        f"Failed to delete repository: {REPO_NAME}"
    assert not await client.check_repo_exists(REPO_NAME), \
        f"Failed to delete repository: {REPO_NAME}"
