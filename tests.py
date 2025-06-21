from functions import get_files_info as gfi

print(gfi.get_files_info("calculator", "."))
print(gfi.get_files_info("calculator", "pkg"))
print(gfi.get_files_info("calculator", "/bin"))
print(gfi.get_files_info("calculator", "../"))