import time
from http.client import HTTPResponse
from urllib import request

class URL:
  def __init__(self, protocol: str, host: str, port: int = None):
    if not protocol or protocol == "":
      raise Exception("Invalid protocol")
    if not host or host == "":
      raise Exception("Invalid host")

    self.__protocol = protocol
    self.__host = host
    self.__port = port

  def get_endpoint(self, path: str) -> str:
    if not path.startswith("/"):
      path = f"/{path}"

    if self.__port:
      return f"{self.__protocol}://{self.__host}:{self.__port}{path}"
    return f"{self.__protocol}://{self.__host}{path}"


class Response:
  def __init__(self, response_code: int, start_time: int, end_time: int):
    self.__code = response_code
    self.__duration = end_time - start_time

  def success(self) -> bool:
    return self.__code == 200

  def duration(self) -> int:
    return int(self.__duration / 1000000)


class Service:
  def __init__(self, name: str, url: URL):
    self.__name = name
    self.__url = url

  def get_name(self) -> str:
    return self.__name

  def ping(self, path: str = "") -> Response:
    try:
      start_time = time.time_ns()
      response: HTTPResponse = request.urlopen(self.__url.get_endpoint(path))
      return Response(response.getcode(), start_time, time.time_ns())
    except:
      return Response(0, 0, 0)
