# ---------------------------------------------------------------------------
# Pelion Device Reliability Testing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------

"""Example: listing endpoints and their resources using Connect API."""
from mbed_cloud import ConnectAPI
import subprocess
import re

def _main():

    # Setup API config
    #try:
    #    result = subprocess.check_output(["mbed", "config", "--list"], stderr=subprocess.STDOUT)
    #except Exception:
    #    self.logger.prn_err("ERROR: CLOUD_SDK_API_KEY global config is not set. ")
    #    return -1
    #
    #match = re.search(b'CLOUD_SDK_API_KEY=(.*)\n', result)
    #if match == None:
    #    self.logger.prn_err("ERROR: CLOUD_SDK_API_KEY global config is not set.")
    #    return -1
    #
    #api_key_val = match.group(1).strip()
    #api_config = {"api_key" : api_key_val, "host" : "https://api.us-east-1.mbedcloud.com"}
    # 
    #print(api_config)
	#
    # Instantiate Device and Connect API
    api = ConnectAPI()

    # Print all devices
    for idx, device in enumerate(api.list_connected_devices(order='desc', limit=10)):
        resources = api.list_resources(device.id)

        # Print endpoint name header
        header = device.id
        print(header)
        print(len(header) * "-")

        for r in resources:
            print("\t- %s (%s / Observable: %s)" %
                  (r.path, r.type if r.type else "-", r.observable))

        # Space between endpoints
        print("")


if __name__ == "__main__":
    _main()
