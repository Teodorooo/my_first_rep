import platform
import psutil
import cpuinfo
import wmi
pc = wmi.WMI()
os_info = pc.Win32_OperatingSystem()[0]
print(os_info)
print(pc.Win32_Processor()[0])
print(pc.Win32_VideoController()[0])
print(f"Architecture: {platform.architecture()}")
print(f"Network Name: {platform.node()}")
print(f"Operating System: {platform.platform()}")
print(f"Procesor: {platform.processor()}")
My_CPUinfo = cpuinfo.get_cpu_info()
print(f"Full CPUName: {My_CPUinfo['brand_raw']}")
print(f"Full CPUName: {My_CPUinfo['hz_actual_friendly']}")
print(f"Full CPUName: {My_CPUinfo['hz_advertised_friendly']}")
print(f"Total RAM: {psutil.virtual_memory().total / 1024/ 1024/ 1024:.2f} Gigabytes")


import speedtest

test = speedtest.Speedtest()

print("Loading Server List...")
test.get_servers()
print("Choosing Best Server...")
best = test.get_best_server()
print(f"Found: {best['host']} located in {best['country']}")

print("Performing Download Test...")
download_result = test.download()
print("Performing Upload Test...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download Speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload Speed: {upload_result / 1024/1024:.2f} Mbit/s")
print(f"Ping: {ping_result:.2f} ms")