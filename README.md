# preltest
Pelion device reliability testing

### Configuration

Create file `.mbed_cloud_config.json` and add the API KEY

{
    "api_key": "..."
}


### Run - example:

```
$ python preltest.py -v
016a55b3ce78000000000001001003eb
--------------------------------
        - /3/0/13 (- / Observable: True)
        - /3/0/21 (- / Observable: True)
        - /3/0/18 (- / Observable: True)
        - /3/0/17 (- / Observable: True)
        - /3/0/2 (- / Observable: True)
        - /3/0/1 (- / Observable: True)
        - /3/0/0 (- / Observable: True)
        - /3/0/16 (- / Observable: True)
        - /3/0/11 (- / Observable: True)
        - /3/0/11/0 (- / Observable: True)
        - /3/0/4 (- / Observable: False)
        - /10255/0/5 (DeviceId / Observable: True)
        - /10255/0/4 (Class / Observable: True)
        - /10255/0/3 (Vendor / Observable: True)
        - /10255/0/2 (OEMBootloaderHash / Observable: True)
        - /10255/0/1 (BootloaderHash / Observable: True)
        - /10255/0/0 (ProtocolSupported / Observable: True)
        - /10252/0/9 (Update / Observable: False)
        - /10252/0/6 (PkgVersion / Observable: True)
        - /10252/0/5 (PkgName / Observable: True)
        - /10252/0/3 (UpdateResult / Observable: True)
        - /10252/0/2 (State / Observable: True)
        - /10252/0/1 (Package / Observable: False)
        - /3300 (- / Observable: False)
        - /3300/0 (- / Observable: False)
        - /3300/0/5605 (execute_function / Observable: False)
        - /3201 (- / Observable: False)
        - /3201/0 (- / Observable: False)
        - /3201/0/5853 (led_state / Observable: False)
        - /3200 (- / Observable: False)
        - /3200/0 (- / Observable: False)
        - /3200/0/5501 (button_count / Observable: True)
        - /1 (- / Observable: False)
        - /1/0 (- / Observable: False)
        - /1/0/8 (- / Observable: False)
        - /1/0/7 (- / Observable: True)
        - /1/0/6 (- / Observable: True)
        - /1/0/1 (- / Observable: True)
        - /1/0/0 (- / Observable: True)

```
