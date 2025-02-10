import uuid
from colorama import init, Fore

init(autoreset=True)

uuid1 = str(uuid.uuid4())
uuid2 = str(uuid.uuid4())

print(Fore.GREEN + "UUIDs Generated:")
print(Fore.RED + f"UUID 1: {uuid1}")
print(Fore.RED + f"UUID 2: {uuid2}")