import asyncio
import websockets
import json

async def test_websocket():
    client_id = "test_user_1"
    
    async with websockets.connect(f"ws://localhost:8000/ws/{client_id}") as websocket:
        print(f"Connected as {client_id}")
        
        # Присоединяемся к комнате
        await websocket.send(json.dumps({
            "type": "join",
            "room": "test_room",
            "username": "Test User"
        }))
        
        # Тестовое сообщение
        await websocket.send(json.dumps({
            "type": "offer",
            "target": "test_user_2",
            "offer": {"sdp": "test_sdp", "type": "offer"}
        }))
        
        # Получаем сообщения
        async for message in websocket:
            data = json.loads(message)
            print(f"📨 Received: {data}")

if __name__ == "__main__":
    asyncio.run(test_websocket())
