#! /usr/bin/env python3

import json
from yacli import CLI, Command

from service import Service, URL

class CheckCommand(Command):
  def __init__(self):
    super().__init__("check", "", args_len=1)

  def handle(self, args: list[str]) -> None:
    path = args[0]
    if not path.endswith(".json"):
      raise Exception("Not a json file")

    with open(path, "r") as json_file:
      services_info: list[dict] = json.load(json_file)
      for service_info in services_info:
        url = URL(service_info.get("protocol"), service_info.get("host"), service_info.get("port"))
        service = Service(service_info.get("name"), url)
        print(f">>> Pinging: \033[33m{service.get_name()}\033[0m...")
        for path in service_info.get("path_list") or []:
          print(f"\t Route: {path}")
          reponse = service.ping(path)
          print(f"\t\t Elapsed time: {reponse.duration()}ms")
          if reponse.success():
            print(f"\t\t Status: \033[32msuccess!\033[0m")
          else:
            print(f"\t\t Status: \033[31mfail!\033[0m")


if __name__ == "__main__":
  cli = CLI("pingr", [CheckCommand()])
  cli.handle()
