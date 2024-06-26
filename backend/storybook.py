from fastapi import APIRouter
import asyncio
from dotenv import load_dotenv
import os

db = []
load_dotenv()
API_URL = os.getenv("API_URL")

# 목업 데이터, openAI API로 생성하고, json으로 정리를 마친 데이터
# 동화 스토리와, 뼈대 (선택지 트리구조)가 잡혀있는 형태의 데이터
mock_story_res = {
    "id": 2,
    "title": "The Adventures of Tiny Tim",
    "data": [
        {
            "page": 1,
            "content": "In a small, cozy house at the edge of the forest, there lived a tiny, curious mouse named Tim. Tim loved to explore and discover new things.",
            "nextPage": [2],
            "prevPage": 0,
        },
        {
            "page": 2,
            "content": "One sunny morning, Tim woke up with a big idea. He wanted to find the biggest cheese in the world! He packed his tiny backpack and set off on his adventure.",
            "nextPage": [3],
            "prevPage": 1,
        },
        {
            "page": 3,
            "content": 'As Tim walked through the forest, he met a friendly rabbit named Ruby. "Where are you going, Tim?" asked Ruby. "I\'m looking for the biggest cheese in the world!" said Tim excitedly. "Can I join you?" Ruby asked. "Of course!" said Tim.',
            "nextPage": [4],
            "prevPage": 2,
        },
        {
            "page": 4,
            "content": 'Tim and Ruby walked deeper into the forest and found a wise old owl named Oliver. "We\'re looking for the biggest cheese in the world. Do you know where it is?" asked Tim. Oliver thought for a moment. "You should visit the Cheese Castle beyond the hills," he said.',
            "nextPage": [5],
            "prevPage": 3,
        },
        {
            "page": 5,
            "content": "Tim and Ruby walked up and down the hills until they saw a grand castle made entirely of cheese! It was the Cheese Castle! They ran towards it with excitement.",
            "nextPage": [6],
            "prevPage": 4,
        },
        {
            "page": 6,
            "content": 'At the entrance of the Cheese Castle, they met a gentle cat named Luna. "Who goes there?" asked Luna. "We are Tim and Ruby. We are looking for the biggest cheese in the world," said Tim. "Come in, brave adventurers!" said Luna.',
            "nextPage": [7],
            "prevPage": 5,
        },
        {
            "page": 7,
            "content": "Inside the castle, everything was made of cheese - the floors, the walls, even the furniture! Tim and Ruby were amazed. Luna guided them to the Cheese Room where the biggest cheese was kept.",
            "nextPage": [8, 9],
            "prevPage": 6,
        },
        {
            "page": 8,
            "choice": "Explore the Secret Room",
            "content": "Tim and Ruby, who had entered the secret room, discovered a hidden door.",
            "nextPage": [10, 11],
            "prevPage": 7,
        },
        {
            "page": 9,
            "choice": "Follow Luna to the Cheese Room",
            "content": "Luna suggested to Tim and Ruby to take on the challenge of finding the “King’s Cheese” hidden in the castle.",
            "nextPage": [12, 13],
            "prevPage": 7,
        },
        {
            "page": 10,
            "choice": "Open the Secret Door",
            "content": "When they opened the door, they found a magical cheese garden. Each tree was bearing different kinds of cheese. Tim and Ruby were astonished by what they saw.",
            "nextPage": [14],
            "prevPage": 8,
        },
        {
            "page": 11,
            "choice": "Ignore the Door and Continue Exploring the Castle",
            "content": "Ignoring the door, Tim and Ruby discovered a hidden cheese cellar. It was filled with the finest cheeses. They were amazed at their luck!",
            "nextPage": [15],
            "prevPage": 8,
        },
        {
            "page": 12,
            "choice": "Accept the Challenge",
            "content": "Tim and Ruby entered the cheese maze to find the “King’s Cheese.” They wandered through the maze and finally discovered a golden cheese in the center.",
            "nextPage": [16],
            "prevPage": 9,
        },
        {
            "page": 13,
            "choice": "Refuse the Challenge and Explore the Castle",
            "content": "Refusing the challenge, Tim and Ruby decided to explore the castle. They found a treasure room filled with sparkling cheeses.",
            "nextPage": [17],
            "prevPage": 9,
        },
        {
            "page": 14,
            "content": "Luna appeared and said, “This is the secret cheese garden. Enjoy these wonderful cheeses.” Tim and Ruby spent a delightful time tasting various kinds of cheese.",
            "nextPage": [18],
            "prevPage": 10,
        },
        {
            "page": 15,
            "content": 'Luna guided them through the cellar and said, "This is where the finest cheeses are stored. Feel free to take some." Tim and Ruby took some fine cheeses and headed home.',
            "nextPage": [19],
            "prevPage": 11,
        },
        {
            "page": 16,
            "content": "Luna congratulated them and said, \"You have found the 'King's Cheese. It's a treasure for true adventurers.\" They proudly took the king's cheese and left the castle.",
            "nextPage": [20],
            "prevPage": 12,
        },
        {
            "page": 17,
            "content": 'Luna smiled and said, "You have discovered the treasure room. Feel free to take some sparkling cheese." Tim and Ruby took some and headed home.',
            "nextPage": [21],
            "prevPage": 13,
        },
        {
            "page": 18,
            "content": "Tim and Ruby returned home with various cheeses. They shared their wonderful experience with their friends and family, feeling happy and content.",
            "nextPage": [],
            "prevPage": 14,
        },
        {
            "page": 19,
            "content": "Back home, Tim and Ruby shared the finest cheeses with their friends and family. It was a wonderful feast, and Tim looked forward to many more adventures to come.",
            "nextPage": [],
            "prevPage": 15,
        },
        {
            "page": 20,
            "content": "Tim and Ruby returned home with the king’s cheese. Their friends were amazed, and they celebrated their successful adventure. Tim looked forward to many more adventures in the future.",
            "nextPage": [],
            "prevPage": 16,
        },
        {
            "page": 21,
            "content": "Tim and Ruby shared the sparkling cheese with their friends. It was a joyful celebration, and Tim looked forward to many more adventures to come.",
            "nextPage": [],
            "prevPage": 17,
        },
    ],
}

db.append(mock_story_res)
storybook_router = APIRouter()


@storybook_router.get("/storybook/{storybookId}")
async def get_storybook(storybookId: int) -> dict:
    # db 순회하면서 해당 id와 일치하는 동화 찾고,
    # 찾았으면 미리 생성해둔 storybook_id page_id에 해당되는 이미지, 비디오를 찾아 json에 링크를 추가하고 반환
    for item in db:
        if item["id"] == storybookId:
            return_storybook = item
            for page in return_storybook["data"]:
                page["image"] = (
                    f"{API_URL}/storybookimage/{return_storybook['id']}/{page['page']}"
                )
                page["talkinghead"] = (
                    f"{API_URL}/talkinghead/{return_storybook['id']}/{page['page']}"
                )
            await asyncio.sleep(1)  # 2초 지연, 실제 배포 시는 제거
            return return_storybook
