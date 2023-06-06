from concurrent import futures
import logging
from dotenv import load_dotenv

import grpc
from proto.ai.text_generation import (
    text_generation_pb2,
    text_generation_pb2_grpc,
)
from apps.text_refiner.app.refiners import tone_modifier, clarifier

load_dotenv("/secrets/.env")


class TextRefiner(text_generation_pb2_grpc.TextRefinerServicer):
    def modify_tone(
        self, request: text_generation_pb2.ToneModificationRequest, context
    ) -> text_generation_pb2.MeteredTextResponse:
        # cast tone from grpc to internal values
        tone = getattr(
            tone_modifier.Tone,
            text_generation_pb2.ToneModificationRequest.Tone.Name(request.tone),
        )
        result_text = tone_modifier.run(
            text=request.text, tone=tone, requester_gid=request.requester_gid
        )
        return text_generation_pb2.MeteredTextResponse(text=result_text, token_count=10)

    def clarify(
        self, request: text_generation_pb2.ToneModificationRequest, context
    ) -> text_generation_pb2.MeteredTextResponse:
        result_text = clarifier.run(
            text=request.text, requester_gid=request.requester_gid
        )
        return text_generation_pb2.MeteredTextResponse(text=result_text, token_count=10)


def serve():
    logging.basicConfig()
    print("Starting server...")
    port = "5000"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    text_generation_pb2_grpc.add_TextRefinerServicer_to_server(TextRefiner(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)

    try:
        # Grpc has handled SIGINT/SIGTERM
        server.wait_for_termination()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    serve()
