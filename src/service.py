from datetime import datetime
from http.client import HTTPResponse
from urllib import request

class URL:
  def __init__(self, protocol: str, host: str, port: int = None):
    self.__protocol = protocol
    self.__host = host
    self.__port = port

  def get_endpoint(self, path: str) -> str:
    if self.__port:
      return f"{self.__protocol}://{self.__host}:{self.__port}/{path}"

    return f"{self.__protocol}://{self.__host}/{path}"


class Response:
  def __init__(self, http_response: HTTPResponse, start_time: int, end_time: int):
    self.__code = http_response.getcode()
    self.__duration = end_time - start_time

  def success(self) -> bool:
    return self.__code == 200

  def duration(self) -> int:
    return self.__duration


class Service:
  def __init__(self, name: str, url: URL):
    self.__name = name
    self.__url = url

  def get_name(self) -> str:
    return self.__name

  def ping(self, path: str = "") -> Response:
    try:
      start_time = int(datetime.now().timestamp())
      response = request.urlopen(self.__url.get_endpoint(path))
      return Response(response, start_time, int(datetime.now().timestamp()))
    except:
      return Response(0, 0, 0)
