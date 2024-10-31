import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GPSConsumer(AsyncWebsocketConsumer):
    connected_clients = set()

    async def connect(self):
        # Adiciona o cliente à lista de clientes conectados
        self.connected_clients.add(self)

        await self.accept()

    async def disconnect(self, close_code):
        # Remove o cliente da lista de clientes conectados
        self.connected_clients.remove(self)

    async def receive(self, text_data):
        try:
            gps_data = json.loads(text_data)
            print("Dados recebidos do cliente:", gps_data)

            # Envie o dado de volta para o cliente via WebSocket
            await self.send(text_data=json.dumps({
                "id": gps_data["id"],
                "latitude": gps_data["latitude"],
                "longitude": gps_data["longitude"]
            }))
            print("Dados enviados de volta para o cliente:", {
                "id": gps_data["id"],
                "latitude": gps_data["latitude"],
                "longitude": gps_data["longitude"]
            })

            # Chame a função para enviar dados para todos os clientes
            await self.send_to_all_clients(gps_data)
        except Exception as e:
            print("Erro ao processar os dados:", str(e))

    async def send_to_all_clients(self, message):
        # Envie a mensagem para todos os clientes conectados
        for client in self.connected_clients:
            await client.send(text_data=json.dumps(message))