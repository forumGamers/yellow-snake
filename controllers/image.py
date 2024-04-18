import generated.image_pb2 as ImageService
import generated.image_pb2_grpc as grpcImageService

class ImageService(grpcImageService.ImageServicer):
    def my():
        return